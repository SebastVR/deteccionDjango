from celery.schedules import crontab

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "10.62.1.86",
    "sigranp.antioquia.gov.co",
    "geopiragua.corantioquia.gov.co",
    "piragua.corantioquia.gov.co",
]

SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# CORS_ORIGIN_ALLOW_ALL = FALSE


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "{levelname} {asctime} {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/django.log",
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
        "file_backends": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/django_backends.log",
            "formatter": "simple",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
        "celery_logger": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/celery.log",
            "formatter": "simple",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["file_backends"],
            "level": "WARNING",
            "propagate": True,
        },
        "celery": {
            "handlers": ["celery_logger"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

CELERY_BEAT_SCHEDULE = {
    "clear_tokens": {
        "task": "red.tasks.clear_tokens",
        "schedule": crontab(hour=1, minute=3),
        "options": {"queue": "worker"},
    }
}
