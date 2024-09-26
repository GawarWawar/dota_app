from celery import shared_task
from celery_instance.celery_app import app
import datetime

from opendota_forcer import models

from opendota_forcer.src.profile import DotaProfile
from opendota_forcer.src.match import DotaMatch

from .process_user_last_match import process_user_last_match


@shared_task(
    bind = True,
)
def process_active_users(self):
    active_users = models.DotaProfile.objects.filter(status = True)
    
    users_processed = []
    for user in active_users:
        process_user_last_match.delay(user.id)
        users_processed.append((user.id, user.name))
    
    self.users_processed = users_processed