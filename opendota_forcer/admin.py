from django.contrib import admin

from . import models

class DotaProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "is_active"
    ]

class DotaMatchAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "adding_date",
    ]

class ScanAdmin(admin.ModelAdmin):
    list_display = [
        "profile_id",
        "match_id",
        "scan_date",
        "parsed_before"
    ]


# Register your models here.
admin.site.register(models.DotaProfile, DotaProfileAdmin)
admin.site.register(models.DotaMatch, DotaMatchAdmin)
admin.site.register(models.Scan, ScanAdmin)
