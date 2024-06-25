from django.db import models
from datetime import datetime
from .projects import Projects


class SST(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True)
    imagen = models.ImageField(upload_to="image/sst", blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = "detection"
        db_table = "sst"
        # ordering = ["nombre"]
        verbose_name = "SST"
        verbose_name_plural = "SST"


class DetectionSST(models.Model):
    proyecto = models.ForeignKey(
        Projects, related_name="proyecto_sst", on_delete=models.CASCADE
    )
    # deteccion = models.ForeignKey(
    #     SST, related_name="detection_sst", on_delete=models.CASCADE
    # )
    imagen_original = models.ImageField(
        upload_to="original/sst",
        blank=True,
        null=True,
    )
    imagen_procesada = models.ImageField(
        upload_to="procesada/sst", blank=True, null=True
    )
    # cantidad = models.PositiveIntegerField(default=0)
    descripcion = models.CharField(max_length=255, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.proyecto

    class Meta:
        app_label = "detection"
        db_table = "detections_sst"
        # ordering = ["nombre"]
        verbose_name = "Deteccion SST"
        verbose_name_plural = "Detecciones SST"


class AuxSST(models.Model):
    deteccion = models.ForeignKey(
        SST, related_name="detection", on_delete=models.CASCADE
    )
    deteccion_sst = models.ForeignKey(
        DetectionSST, related_name="detection_sst", on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.deteccion

    class Meta:
        app_label = "detection"
        db_table = "aux_sst"
        # ordering = ["nombre"]
        verbose_name = "Aux SST"
        verbose_name_plural = "Aux SST"
