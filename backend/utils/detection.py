# from pathlib import Path
# import json
# from detection.models import Detection
# from ultralytics import YOLO
# from datetime import datetime
# from utils.save_s3 import SaveS3
# import logging

# logger = logging.getLogger(__name__)


# EPP_ITEMS = [
#     "arnes",
#     "barbuquejo",
#     "botas",
#     "casco",
#     "chaleco",
#     "eslingas",
#     "guantes",
#     "personas",
#     "proteccion_auditiva",
#     "proteccion_respiratoria",
#     "proteccion_visual",
# ]


# def save_image(file):
#     image_dir = Path("data/media")
#     image_dir.mkdir(parents=True, exist_ok=True)
#     file_location = image_dir / file.name
#     with file_location.open("wb") as buffer:
#         for chunk in file.chunks():
#             buffer.write(chunk)
#     return file_location


# def process_image(file, project):
#     s3_saver = SaveS3()
#     local_image_path = save_image(file)

#     try:
#         bucket_name = "project-ppe-detection-datalake"
#         object_name_original = f"original/{file.name}"
#         with local_image_path.open("rb") as img_file:
#             datalake_image_path = s3_saver.write_image_to_minio(
#                 bucket_name, object_name_original, img_file.read()
#             )
#     except Exception as e:
#         logger.error(f"Error uploading original image to MinIO: {e}")
#         raise

#     try:
#         processed_dir = Path("data/processed")
#         processed_dir.mkdir(parents=True, exist_ok=True)
#         model = YOLO("data/staticfiles/best.pt")
#         results = model.predict(
#             [local_image_path.as_posix()], save=True, project=processed_dir.as_posix()
#         )

#         processed_files = list(processed_dir.glob("**/*"))
#         if processed_files:
#             for processed_file in processed_files:
#                 if processed_file.is_file():
#                     with processed_file.open("rb") as processed_img_file:
#                         datalake_image_processed = s3_saver.write_image_to_minio(
#                             bucket_name,
#                             f"processed/{processed_file.name}",
#                             processed_img_file.read(),
#                         )
#                     break
#         else:
#             datalake_image_processed = "No processed image found"
#     except Exception as e:
#         logger.error(f"Error processing image with YOLO: {e}")
#         raise

#     try:
#         detections = results[0].tojson()
#         detection_counts = {item: 0 for item in EPP_ITEMS}
#         for detection in json.loads(detections):
#             if detection["name"] in EPP_ITEMS:
#                 detection_counts[detection["name"]] += 1

#         new_detection = Detection.objects.create(
#             datalake_image_path=datalake_image_path,
#             datalake_image_processed=datalake_image_processed,
#             project=project,
#             created_at=datetime.utcnow(),
#             **detection_counts,
#         )
#     except Exception as e:
#         logger.error(f"Error saving detection to database: {e}")
#         raise

#     return new_detection
