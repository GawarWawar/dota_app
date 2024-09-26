from celery import Celery
from celery.schedules import crontab

# Launching comands:
# 1. Celery worker:
    # celery -A celery_instance worker --loglevel=INFO 
# 2. Celery-beat instance:
    # celery -A celery_instance beat -l info 

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dota_stats.settings')

app = Celery("celery_instance")

app.config_from_object('celery_instance.settings')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()