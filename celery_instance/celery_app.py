from celery import Celery
from celery.schedules import crontab

import os

# Launching comands:
# 1. Celery worker:
    # celery -A celery_instance worker --loglevel=INFO 
# 2. Celery-beat instance:
    # celery -A celery_instance beat -l info 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dota_stats.settings')

app = Celery(
    "celery_instance", 
    backend='django_celery_results.backends.database:DatabaseBackend'
)

app.config_from_object('celery_instance.settings')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()