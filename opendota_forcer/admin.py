from django.contrib import admin

from . import models

class DotaProfileAdmin(admin.ModelAdmin):
    """ Admin for DotaProfile model
    """
    list_display = [
        "id",
        "name",
        "is_active"
    ]

class DotaMatchAdmin(admin.ModelAdmin):
    """ Admin for DotaMatch model
    """
    list_display = [
        "id",
        "adding_date",
    ]

class ScanAdmin(admin.ModelAdmin):
    """ Admin for Scan model
    """
    list_display = [
        "profile_instance",
        "match_instance",
        "scan_date",
        "parsed_before"
    ]


# Register your models here.
admin.site.register(models.DotaProfile, DotaProfileAdmin)
admin.site.register(models.DotaMatch, DotaMatchAdmin)
admin.site.register(models.Scan, ScanAdmin)
