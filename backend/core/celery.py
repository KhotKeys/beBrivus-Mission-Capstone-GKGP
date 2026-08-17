import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Read CELERY_* keys from Django settings (CELERY_BROKER_URL -> broker_url, etc.)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Pick up tasks.py from every installed app.
app.autodiscover_tasks()
