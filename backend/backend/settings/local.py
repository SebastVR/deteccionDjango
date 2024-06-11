from celery.schedules import crontab
from .base import *

DEBUG = False


CELERY_BEAT_SCHEDULE = {
    "hourlyResample": {
        "task": "red.tasks.hourly_resample",
        "schedule": crontab(minute="2,7"),  # execute every 5 minute
        "options": {"queue": "worker"},
    },
    "dailyResample": {
        "task": "red.tasks.daily_resample",
        "schedule": crontab(minute="3,8"),  # execute every 5 minute
        "options": {"queue": "worker"},
    },
    "fetch_facebook": {
        "task": "web.tasks.fetch_and_process_new_facebook_posts",
        "schedule": crontab(hour="10", minute="0"),
        "options": {"queue": "worker"},
    },
}
