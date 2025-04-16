from __future__ import absolute_import
import os
import dotenv
from celery import Celery

if os.path.isfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")):
    dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funtech.settings.' + os.environ.get("ENVIRONMENT"))

app = Celery('funtech')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
