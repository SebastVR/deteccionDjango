from celery.schedules import crontab

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "10.62.1.91",
    "sigran.antioquia.gov.co",
    "dagran.antioquia.gov.co",
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
    },
    "estadoRed": {
        "task": "instrumentacion.tasks.network_state",
        "schedule": crontab(hour=6, minute=0),
        "options": {"queue": "worker"},
    },
    # "umbralesNivel": {
    #     "task": "umbral.tasks.umbrales_nivel",
    #     "schedule": crontab(minute="*/5"),
    #     "options": {"queue": "worker"},
    # },
    # "umbralesPPT": {
    #     "task": "umbral.tasks.umbrales_precipitacion",
    #     "schedule": crontab(minute="*/5"),
    #     "options": {"queue": "worker"},
    # },
    "hourlyResample": {
        "task": "red.tasks.hourly_resample",
        "schedule": crontab(minute="2,7"),
        "options": {"queue": "worker"},
    },
    "dailyResample": {
        "task": "red.tasks.daily_resample",
        "schedule": crontab(hour="0,6,12,18", minute="3,8"),
        "options": {"queue": "worker"},
    },
    "populate_cameras": {
        "task": "red.tasks.populate_cameras",
        "schedule": crontab(minute="1,11,21,31,41,51"),
        "options": {"queue": "worker"},
    },
    "clean_cameras": {
        "task": "red.tasks.clean_cameras",
        "schedule": crontab(hour=1, minute="8"),
        "options": {"queue": "worker"},
    },
    "fetch_facebook": {
        "task": "web.tasks.fetch_and_process_new_facebook_posts",
        "schedule": crontab(hour="3", minute="0"),
        "options": {"queue": "worker"},
    },
}
