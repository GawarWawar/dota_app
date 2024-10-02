import datetime

from django.db import models

class DotaProfile (models.Model):
    """ Model for DotaProfile that stores its id as a PK, name as a displayed name, and is_active to determine if there is a need to parse matches for this user 
    """
    id = models.IntegerField("Profile", primary_key=True)
    name = models.CharField("Player name", max_length=50)
    is_active = models.BooleanField("Active status", default=True)
    
class DotaMatch (models.Model):
    """ Model for DotaMatch that stores its id as a PK and when it was added
    """
    id = models.IntegerField("Match", primary_key=True)
    adding_date = models.DateField("Adding date", auto_now=False, auto_now_add=False, default=datetime.datetime.now)
    
class Scan (models.Model):
    """ Model for Scan instance that indicates action of Scaning a match for a certain user. This stores DotaProfile and DotaMatch, scan_date as a date of the check, and parsed_before - status of parse before scan.
    """
    profile_instance = models.ForeignKey(DotaProfile, verbose_name="Profile", on_delete=models.CASCADE)
    match_instance = models.ForeignKey(DotaMatch, verbose_name="Match", on_delete=models.CASCADE)
    scan_date = models.DateField("Date of Scan", auto_now=False, auto_now_add=False, default=datetime.datetime.now)
    parsed_before = models.BooleanField("Was match parsed before")
