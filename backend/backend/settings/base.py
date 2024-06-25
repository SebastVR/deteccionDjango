"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

from pathlib import Path

with open("/run/secrets/CREDS") as f:
    import json

    creds = json.load(f)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = creds["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*",
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
]
# Application definition

MATERIAL_ADMIN_SITE = {
    "HEADER": _("SIGRAN"),  # Admin site header
    "TITLE": _("SIGRAN"),  # Admin site title
    # Admin site favicon (path to static should be specified)
    "FAVICON": "files/favicon.ico",
    "MAIN_BG_COLOR": "#007676",  # Admin site main color, css color should be specified
    # "#ffd100",  # "#987b07", # Admin site main hover color, css color should be specified
    "MAIN_HOVER_COLOR": "#007676",
    # "PROFILE_PICTURE": "files/dagran2.png",  # Admin site profile picture (path to static should be specified)
    # Admin site profile background (path to static should be specified)
    "PROFILE_BG": "files/logo_integral.png",
    # Admin site logo on login page (path to static should be specified)
    "LOGIN_LOGO": "",
    # Admin site background on login/logout pages (path to static should be specified)
    "LOGOUT_BG": "files/banner.png",
    "SHOW_THEMES": True,  # Show default admin themes button
    "TRAY_REVERSE": False,  # Hide object-tools and additional-submit-line by default
    "NAVBAR_REVERSE": False,  # Hide side navbar by default
    "SHOW_COUNTS": False,  # Show instances counts for each model
    "APP_ICONS": {
        "auth": "icons/autorizacion-autenticacion",
        "oauth2_provider": "icons/django-oauth-toolkit",
    },  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
    "MODEL_ICONS": {
        "user": "icons/usuarios",
        "group": "icons/grupos",
        "accesstoken": "icons/acces-tokens",
        "application": "icons/applications",
        "grant": "icons/grants",
        "idtoken": "icons/id-token",
        "refreshtoken": "icons/refresh-token",
    },  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
}


INSTALLED_APPS = [
    "material",
    "material.admin",
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "detection",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {}

DATABASES["default"] = {
    "ENGINE": "django.contrib.gis.db.backends.postgis",
    "NAME": creds["POSTGRES_DB"],
    "USER": creds["POSTGRES_USER"],
    "PASSWORD": creds["POSTGRES_PASSWORD"],
    "HOST": creds["POSTGRES_HOST"],
    "PORT": creds["POSTGRES_PORT"],
    "TEST": {
        "MIRROR": "default",
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

STATIC_ROOT = os.path.join(BASE_DIR, "data/staticfiles/")
STATIC_URL = "/staticfiles/"

MEDIA_ROOT = os.path.join(BASE_DIR, "data/mediafiles/")
MEDIA_URL = "/mediafiles/"

STATICFILES_DIRS = [
    ("css", os.path.join(BASE_DIR, "static/css/")),
    ("files", os.path.join(BASE_DIR, "static/files/")),
]
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "es-co"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": (
#         "rest_framework.permissions.IsAuthenticatedOrReadOnly",
#     ),
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
#         "rest_framework.authentication.SessionAuthentication",
#     ),
#     "TEST_REQUEST_DEFAULT_FORMAT": "json",
#     "TEST_REQUEST_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
# }


if "MINIO_ACCESS_KEY" in creds:
    MINIO_ACCESS_KEY = creds["MINIO_ACCESS_KEY"]

if "MINIO_SECRET_KEY" in creds:
    MINIO_SECRET_KEY = creds["MINIO_SECRET_KEY"]

if "MINIO_ENDPOINT" in creds:
    MINIO_ENDPOINT = creds["MINIO_ENDPOINT"]


# MINIO_ENDPOINT = "http://localhost:9095"
# MINIO_ACCESS_KEY = "your-minio-access-key"
# MINIO_SECRET_KEY = "your-minio-secret-key"
