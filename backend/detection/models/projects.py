from django.db import models
from detection.info import TIPO_PROJECT


class Projects(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    director_proyecto = models.CharField(max_length=100, blank=True)
    administrador = models.CharField(max_length=100, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    estado = models.CharField(
        max_length=50, choices=TIPO_PROJECT, default="Activo", blank=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = "detection"
        db_table = "projects"
        # ordering = ["name"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"
