from django.contrib.gis import admin
from detection import models


@admin.register(models.TypeSigns)
class TypeSignsAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("nombre"),
        ("imagen"),
    )
    list_display = [
        "nombre",
        "imagen",
    ]
    list_display_links = [
        "nombre",
        "imagen",
    ]
    list_filter = ["nombre"]
    search_fields = ["nombre"]


@admin.register(models.Signs)
class SignsAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("tipo"),
        ("codigo"),
        ("descripcion"),
    )
    list_display = [
        "tipo",
        "codigo",
        "descripcion",
    ]
    list_display_links = [
        "tipo",
        "codigo",
        "descripcion",
    ]
    list_filter = ["tipo"]
    search_fields = ["tipo", "descripcion"]


class AuxSignsInline(admin.TabularInline):
    model = models.AuxSigns
    extra = 1


@admin.register(models.DetectionSigns)
class DetectionSignsAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    inlines = [AuxSignsInline]
    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("proyecto", "senal"),
        ("imagen_original", "imagen_procesada"),
        ("descripcion"),
        ("latitud", "longitud"),
        ("created_at"),
    )
    list_display = [
        "proyecto",
        "senal",
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
        "senal",
        "imagen_original",
        "imagen_procesada",
        "cantidad",
        "descripcion",
        "latitud",
        "longitud",
        "created_at",
    ]
    list_filter = ["proyecto"]
    search_fields = ["proyecto"]
