import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dploy.settings.prod')

app = Celery('dploy')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'restart_counter_every_minute': {
        'task': 'app.tasks.restart_counter',
        'schedule': crontab(minute='*/1'),  # Runs every minute
    },
}