import datetime

from django.db import models

class DotaProfile (models.Model):
    id = models.IntegerField("Profile", primary_key=True)
    name = models.CharField("Player name", max_length=50)
    is_active = models.BooleanField("Active status", default=True)
    
class DotaMatch (models.Model):
    id = models.IntegerField("Match", primary_key=True)
    adding_date = models.DateField("Adding date", auto_now=False, auto_now_add=False, default=datetime.datetime.now)
    
class Scan (models.Model):
    profile_instance = models.ForeignKey(DotaProfile, verbose_name="Profile", on_delete=models.CASCADE)
    match_instance = models.ForeignKey(DotaMatch, verbose_name="Match", on_delete=models.CASCADE)
    scan_date = models.DateField("Date of Scan", auto_now=False, auto_now_add=False, default=datetime.datetime.now)
    parsed_before = models.BooleanField("Was match parsed before")
