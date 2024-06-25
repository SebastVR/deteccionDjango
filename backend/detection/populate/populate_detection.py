import os

# from decimal import *
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings as _settings
from detection.models import (
    SST,
    Projects,
    TypeSigns,
    Signs,
)
from detection.info import TIPO_PROJECT

PATH_DATA_APP = os.path.join(_settings.STATIC_ROOT, "files/")


df_type_sign = pd.read_csv(
    PATH_DATA_APP + "tipo_sign.csv",
    sep=",",
    decimal=".",
    na_values=[
        "<NA>",
        "ND",
        "-",
        "",
        "Faltan datos",
        "N/D",
        "No Se Puede Determinar",
        "No Se puede Determinar",
        "No Se Puede Calcular",
        "No calcular",
        "0/01/1900",
        "No Aplica",
    ],
)

df_type_sign["tipo"] = df_type_sign["tipo"].str.strip()
df_type_sign["codigo"] = df_type_sign["codigo"].str.strip().str.lower()
df_type_sign["descripcion"] = df_type_sign["descripcion"].str.strip()


def main_type_sign():
    for index, row in df_type_sign.iterrows():
        try:
            type_sign = TypeSigns.objects.get(nombre=row.tipo)
        except ObjectDoesNotExist:
            type_sign = TypeSigns(nombre=row.tipo)
        type_sign.full_clean()
        type_sign.save()
        print(type_sign)
        try:
            sign = Signs.objects.get(codigo=row.codigo)
        except ObjectDoesNotExist:
            sign = Signs(codigo=row.codigo)
        sign.tipo = type_sign
        sign.descripcion = row.descripcion
        type_sign.full_clean()
        type_sign.save()
        sign.full_clean()
        sign.save()
        print(type_sign)


main_type_sign()


df_type_sst = pd.read_csv(
    PATH_DATA_APP + "sst.csv",
    sep=",",
    decimal=".",
    na_values=[
        "<NA>",
        "ND",
        "-",
        "",
        "Faltan datos",
        "N/D",
        "No Se Puede Determinar",
        "No Se puede Determinar",
        "No Se Puede Calcular",
        "No calcular",
        "0/01/1900",
        "No Aplica",
    ],
)


def main_type_sst():
    for index, row in df_type_sst.iterrows():
        try:
            type_sst = SST.objects.get(codigo=row.codigo)
        except ObjectDoesNotExist:
            type_sst = SST(codigo=row.codigo)
        type_sst.nombre = row.nombre
        type_sst.descripcion = row.descripcion
        type_sst.full_clean()
        type_sst.save()
        print(type_sst)


main_type_sst()

df_project = pd.read_csv(
    PATH_DATA_APP + "projects.csv",
    sep=",",
    decimal=".",
    na_values=[
        "<NA>",
        "ND",
        "-",
        "",
        "Faltan datos",
        "N/D",
        "No Se Puede Determinar",
        "No Se puede Determinar",
        "No Se Puede Calcular",
        "No calcular",
        "0/01/1900",
        "No Aplica",
    ],
)

df_project["nombre"] = df_project["nombre"].str.strip().apply(lambda x: x.capitalize())
df_project["director_proyecto"] = (
    df_project["director_proyecto"].str.strip().str.title()
)
df_project["administrador"] = df_project["administrador"].str.strip().str.title()

df_project["estado"] = df_project["estado"].str.strip()
df_project.loc[df_project["estado"] == "Terminado", "estado"] = TIPO_PROJECT[4][0]
df_project.loc[df_project["estado"] == "Activo", "estado"] = TIPO_PROJECT[0][0]
df_project.loc[df_project["estado"] == "Suspendido", "estado"] = TIPO_PROJECT[3][0]
df_project.loc[df_project["estado"] == "Inactivo/ No ejecutado", "estado"] = (
    TIPO_PROJECT[2][0]
)
df_project.loc[df_project["estado"] == "En Liquidación", "estado"] = TIPO_PROJECT[1][0]


def main_projects():
    for index, row in df_project.iterrows():
        try:
            project = Projects.objects.get(codigo=row.codigo)
        except ObjectDoesNotExist:
            project = Projects(codigo=row.codigo)
        project.nombre = row.nombre
        project.director_proyecto = row.director_proyecto
        project.administrador = row.administrador
        project.cliente = row.cliente
        project.estado = row.estado
        project.full_clean()
        project.save()
        print(project)


main_projects()
