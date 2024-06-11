from django.db import models
from datetime import datetime
from .projects import Projects


class Materials(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    unidad = models.CharField(max_length=255, blank=True)
    imagen = models.ImageField(upload_to="image/materials", blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = "detection"
        db_table = "materials"
        # ordering = ["nombre"]
        verbose_name = "Material"
        verbose_name_plural = "Materiales"


class DetectionMaterials(models.Model):
    proyecto = models.ForeignKey(
        Projects, related_name="proyecto_materials", on_delete=models.CASCADE
    )
    material = models.ForeignKey(
        Materials, related_name="detection_materials", on_delete=models.CASCADE
    )
    imagen_original = models.ImageField(
        upload_to="original/materials", blank=True, null=True
    )
    imagen_procesada = models.ImageField(
        upload_to="procesada/materials", blank=True, null=True
    )
    cantidad = models.FloatField(default=0)
    descripcion = models.CharField(max_length=255, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.material

    class Meta:
        app_label = "detection"
        db_table = "detections_materials"
        # ordering = ["nombre"]
        verbose_name = "Detección Material"
        verbose_name_plural = "Detección Materiales"
