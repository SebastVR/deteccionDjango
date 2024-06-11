from django.contrib.gis import admin
from detection import models


# class FotoEstacionMantenimientoInline(admin.TabularInline):
#     model = models.FotoMantenimiento
#     extra = 1
#     fields = ["mantenimiento", "nombre", "foto"]


@admin.register(models.SST)
class SSTAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("nombre"),
        ("codigo"),
        ("descripcion"),
        ("imagen"),
    )
    list_display = [
        "nombre",
        "codigo",
        "descripcion",
        "imagen",
    ]
    list_display_links = [
        "nombre",
        "codigo",
        "descripcion",
        "imagen",
    ]
    list_filter = ["nombre"]
    search_fields = ["nombre"]


@admin.register(models.DetectionSST)
class DetectionSSTAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("proyecto", "deteccion"),
        ("imagen_original", "imagen_procesada"),
        ("cantidad", "descripcion"),
        ("latitud", "longitud"),
        ("created_at"),
    )
    list_display = [
        "proyecto",
        "deteccion",
        "imagen_original",
        "imagen_procesada",
        "cantidad",
        "descripcion",
        "latitud",
        "longitud",
        "created_at",
    ]
    list_display_links = [
        "proyecto",
        "deteccion",
        "imagen_original",
        "imagen_procesada",
        "cantidad",
        "descripcion",
        "latitud",
        "longitud",
        "created_at",
    ]
    list_filter = ["proyecto", "deteccion"]
    search_fields = ["proyecto", "deteccion"]
