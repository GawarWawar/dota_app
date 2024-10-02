from celery import shared_task

from opendota_forcer import models
from .process_user_last_match import process_user_last_match


@shared_task(
    bind = True,
)
def process_active_users(self) -> list[tuple[int, str]]:
    """ Celery task that gathers all active users in models.DotaProfile and then calls process_user_last_match for every one of them

    Returns:
        list[tuple[int, str]]: list with users.id and user.name chained in tuple. In other words, list of tuples with id and name of the user.
    """
    active_users = models.DotaProfile.objects.filter(is_active = True)
    
    users_processed = []
    for user in active_users:
        process_user_last_match.delay(user.id)
        users_processed.append((user.id, user.name))
    
    self.users_processed = users_processed
    
    return users_processed