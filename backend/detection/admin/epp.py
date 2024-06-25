from django.contrib.gis import admin
from detection import models

# from django.conf import settings as _settings

# condition = (
#     _settings.MEDIA_URL if _settings.ENVIRONMENT != "testing" else _settings.STATIC_URL
# )


# class BaseAdmin(admin.ModelAdmin):
#     class Media:
#         css_path = f"{condition}css/custom_styles.css"
#         css = {"all": (css_path,)}


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


class AuxSSTInline(admin.TabularInline):
    model = models.AuxSST
    extra = 1


@admin.register(models.DetectionSST)
class DetectionSSTAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    inlines = [AuxSSTInline]

    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("proyecto"),
        ("imagen_original", "imagen_procesada"),
        ("descripcion"),
        ("latitud", "longitud"),
        ("created_at"),
    )
    list_display = [
        "proyecto",
        # "deteccion",
        "imagen_original",
        "imagen_procesada",
        # "cantidad",
        "descripcion",
        "latitud",
        "longitud",
        "created_at",
    ]
    list_display_links = [
        "proyecto",
        # "deteccion",
        "imagen_original",
        "imagen_procesada",
        # "cantidad",
        "descripcion",
        "latitud",
        "longitud",
        "created_at",
    ]
    list_filter = ["proyecto"]
    search_fields = ["proyecto"]
