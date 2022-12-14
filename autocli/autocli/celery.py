# Python import:
import os

# Celery import:
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocli.settings')

app = Celery('autocli')

# Celery settings are in settings.py using a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
# Change default queue name:
app.conf.task_default_queue = 'default'
