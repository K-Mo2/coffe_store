from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from store.tasks import add

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffe_store.settings')

app = Celery('coffe_store')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': 2,
        'args': (16, 16),
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

