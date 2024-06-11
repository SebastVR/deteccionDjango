from django.contrib.gis import admin
from detection import models


@admin.register(models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    # actions = [download_csv_action, download_xlsx_action]
    # extended_actions = ["download_csv", "download_xlsx"]
    icon_name = "local_drink"
    list_select_related = True
    fields = (
        ("codigo"),
        ("nombre"),
        ("director_proyecto"),
        ("administrador"),
        ("cliente"),
        ("estado"),
    )
    list_display = [
        "codigo",
        "nombre",
        "director_proyecto",
        "administrador",
        "cliente",
        "estado",
    ]
    list_display_links = [
        "codigo",
        "nombre",
        "director_proyecto",
        "administrador",
        "cliente",
        "estado",
    ]
    list_filter = ["codigo", "estado"]
    search_fields = ["nombre", "codigo"]
