import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')

# Celery app
app = Celery('celeryapp')

app.config_from_object('django.conf:settings')

# Autodiscover <app.task.py> tasks
app.autodiscover_tasks()


# Debug task
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
