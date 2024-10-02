
from celery import shared_task
from celery_instance.celery_app import app
import datetime


from opendota_forcer import models

from opendota_forcer.src.profile import DotaProfile
from opendota_forcer.src.match import DotaMatch

@shared_task(
    bind = True,
)
def process_user_last_match(
    self,
    profile_id: int
) -> str:
    """Celery task, that gets last match of the user, checks if it was parsed and then parse it.
    Also it creates models.DotaMatch for found match; it creates models.Scan to indicate an action of the scanning match

    Args:
        profile_id (int): id of DotaProfile for which we need to find and parse match

    Returns:
        str: message that parse_match sends after complition
    """
    profile = DotaProfile(profile_id)
    
    last_match = profile.get_last_match()
    get_match_result = models.DotaMatch.objects.get_or_create(
        id = last_match.MATCH_ID
    )
    match_object = get_match_result[0]
    if get_match_result[1]:
        match_object.save()
    
    parsed_before = last_match.check_parsed_status()
    self.message = last_match.parse_match()
    
    scan_object = models.Scan.objects.create(
        profile_id = models.DotaProfile.objects.get(id = profile.PROFILE_ID),
        match_id = match_object,
        parsed_before = parsed_before
    )
    scan_object.save()
    
    self.profile_id = profile.PROFILE_ID
    self.match_id = last_match.MATCH_ID
    
    return self.message 
    
        
        