from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin



class PrimaryProfileAdmin(ImportExportModelAdmin):
    resource_class = PrimaryProfileResource
    list_display = ("id", "user", "primary_classroom", "active", "created_at", "updated_at")
    search_fields = ("classroom__main_classroom", "id", "user__full_name",)
admin.site.register(PrimaryProfile, PrimaryProfileAdmin)

