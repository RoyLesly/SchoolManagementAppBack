from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin


class SecondaryProfileAdmin(ImportExportModelAdmin):
    resource_class = SecondaryProfileResource
    list_display = ("id", "user", "secondary_classroom", "active", "created_at", "updated_at")
    search_fields = ("specialty__main_specialty__specialty_name", "id", "user__first_name", "user__matricle",)
admin.site.register(SecondaryProfile, SecondaryProfileAdmin)


