from celery import shared_task

from opendota_forcer import models
from .process_user_last_match import process_user_last_match


@shared_task(
    bind = True,
)
def process_active_users(self) -> list[tuple[int, str]]:

    active_users = models.DotaProfile.objects.filter(is_active = True)
    
    users_processed = []
    for user in active_users:
        process_user_last_match.delay(user.id)
        users_processed.append((user.id, user.name))
    
    self.users_processed = users_processed
    
    return users_processed