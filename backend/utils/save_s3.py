import s3fs

import mimetypes
from django.conf import settings as _settings

import logging

logger = logging.getLogger(__name__)


class SaveS3:
    def __init__(self):
        self.endpoint_url = _settings.MINIO_ENDPOINT
        self.fs = s3fs.S3FileSystem(
            client_kwargs={"endpoint_url": self.endpoint_url},
            key=_settings.MINIO_ACCESS_KEY,
            secret=_settings.MINIO_SECRET_KEY,
            use_ssl=False,
        )

    def upload_file_to_minio(self, bucket_name, object_name, file_data, content_type):
        if not file_data:
            raise ValueError("No hay datos para escribir en el archivo.")

        metadata = {
            "Content-Type": content_type,
            "Content-Disposition": "inline",
        }

        try:
            with self.fs.open(
                f"{bucket_name}/{object_name}",
                "wb",
                metadata=metadata,
            ) as f:
                f.write(file_data)
                f.flush()
        except Exception as e:
            logger.error(f"Error al escribir el archivo en MinIO: {str(e)}")
            raise Exception(f"Error al escribir el archivo en MinIO: {str(e)}")

        return f"{bucket_name}/{object_name}"

    def write_image_to_minio(self, bucket_name, object_name, file_data):
        if not file_data:
            raise ValueError("El contenido del archivo está vacío.")

        mime_type, _ = mimetypes.guess_type(object_name)
        if not mime_type:
            mime_type = "application/octet-stream"

        self.fs.makedirs(bucket_name, exist_ok=True)
        file_path = self.upload_file_to_minio(
            bucket_name, object_name, file_data, mime_type
        )
        return f"http://localhost:9095/{file_path}"
