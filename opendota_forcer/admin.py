from django.contrib import admin

from . import models

class DotaUserAdmin(admin.ModelAdmin):
    ...

class DotaMatchAdmin(admin.ModelAdmin):
    ...

class ScanAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(models.DotaUser, DotaUserAdmin)
admin.site.register(models.DotaMatch, DotaMatchAdmin)
admin.site.register(models.Scan, ScanAdmin)
