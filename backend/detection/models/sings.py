from django.db import models
from datetime import datetime
from .projects import Projects


class TypeSigns(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to="image/signs", blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = "detection"
        db_table = "types_signs"
        # ordering = ["nombre"]
        verbose_name = "Tipo Señal"
        verbose_name_plural = "Tipos Señales"


class Signs(models.Model):
    tipo = models.ForeignKey(TypeSigns, related_name="signs", on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    # nombre = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.tipo}"

    class Meta:
        app_label = "detection"
        db_table = "signs"
        # ordering = ["nombre"]
        verbose_name = "Señal"
        verbose_name_plural = "Señales"


class DetectionSigns(models.Model):
    proyecto = models.ForeignKey(
        Projects, related_name="proyecto_signs", on_delete=models.CASCADE
    )
    senal = models.ForeignKey(
        TypeSigns, related_name="detection_signs", on_delete=models.CASCADE
    )
    imagen_original = models.ImageField(
        upload_to="original/signs", blank=True, null=True
    )
    imagen_procesada = models.ImageField(
        upload_to="procesada/signs", blank=True, null=True
    )
    cantidad = models.PositiveIntegerField(default=0)
    descripcion = models.CharField(max_length=255, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"{self.proyecto} - {self.senal} - {self.created_at}"

    class Meta:
        app_label = "detection"
        db_table = "detections_signs"
        # ordering = ["nombre"]
        verbose_name = "Detección Señales"
        verbose_name_plural = "Detección Señales"


class AuxSigns(models.Model):
    deteccion = models.ForeignKey(
        TypeSigns, related_name="detection", on_delete=models.CASCADE
    )
    deteccion_signs = models.ForeignKey(
        DetectionSigns, related_name="detection_sst", on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.deteccion

    class Meta:
        app_label = "detection"
        db_table = "aux_sing"
        # ordering = ["nombre"]
        verbose_name = "Aux Sing"
        verbose_name_plural = "Aux Sing"
