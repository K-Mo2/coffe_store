from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from store import tasks 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffe_store.settings')

app = Celery('coffe_store')

app.config_from_object('django.conf:settings', namespace='CELERY')

#crontab(hour=12, minute=0)

app.conf.beat_schedule = {
    'reset-stock-every-day-afternoon': {
        'task': 'store.tasks.reset_coffe_beans',
        'schedule':crontab(hour=12, minute=0) ,
    },
}

app.autodiscover_tasks()
