from django.contrib.gis import admin
from detection import models


# class DetectionMaterialsInline(admin.TabularInline):
#     model = models.DetectionMaterials
#     extra = 1  # Esto evita la creación de elementos adicionales en blanco


@admin.register(models.Materials)
class Materialsdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    # inlines = [DetectionMaterialsInline]

    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("nombre"),
        ("descripcion"),
        ("unidad"),
        ("imagen"),
        ("created_at"),
    )
    list_display = [
        "nombre",
        "descripcion",
        "unidad",
        "imagen",
        "created_at",
    ]
    list_display_links = [
        "nombre",
        "descripcion",
        "unidad",
        "imagen",
        "created_at",
    ]
    list_filter = ["nombre"]
    search_fields = ["nombre"]


@admin.register(models.DetectionMaterials)
class DetectionMaterialsAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]

    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("proyecto", "material"),
        ("imagen_original", "imagen_procesada"),
        ("cantidad", "descripcion"),
        ("latitud", "longitud"),
        ("created_at"),
    )
    list_display = [
        "proyecto",
        "material",
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
        "material",
        "imagen_original",
        "imagen_procesada",
        "cantidad",
        "descripcion",
        "latitud",
        "longitud",
        "created_at",
    ]
    list_filter = ["proyecto", "material"]
    search_fields = ["proyecto", "material"]
