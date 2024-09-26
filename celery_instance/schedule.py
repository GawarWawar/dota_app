from celery.signals import celeryd_after_setup
from .celery_app import app

from opendota_forcer.tasks.process_active_users import process_active_users

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(1800.0, process_active_users.s(), name="Starts a scan for active users every 30 mins")