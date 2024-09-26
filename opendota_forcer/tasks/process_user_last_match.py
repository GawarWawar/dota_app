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
    PROFILE_ID
):
    profile = DotaProfile(PROFILE_ID)
    last_match = profile.get_last_match()
    match_object = models.DotaMatch().objects.create(
        id = last_match.MATCH_ID
    )
    match_object.save()
    parced_before = last_match.check_parsed_status()
    
    self.message = last_match.parse_match()
    
    scan_object = models.Scan.objects.create(
        profile_id = PROFILE_ID,
        match_id = last_match.MATCH_ID,
        parced_before = parced_before
    )
    scan_object.save()
    
    self.profile_id = PROFILE_ID
    self.match_id = last_match.MATCH_ID
    
    return self.message 
    
        
        