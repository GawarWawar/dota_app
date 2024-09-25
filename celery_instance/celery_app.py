from celery import Celery

# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karting_site.settings')

app = Celery("celery_instance")

app.config_from_object('celery_instance.settings')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()