from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class PrimaryLevelAdmin(ImportExportModelAdmin):
    resource_class = PrimaryLevelResource
    list_display = ("id", "level")
admin.site.register(PrimaryLevel, PrimaryLevelAdmin)


class PrimaryClassRoomAdmin(ImportExportModelAdmin):
    resource_class = PrimaryClassRoomResource
    list_display = ("id", "school", "level", "tuition", "payment_one", "payment_two", "payment_three", "registration", "academic_year", "created_at", "updated_at")
    search_fields = ("academic_year", "id", "main_classroom__classroom_name",)
admin.site.register(PrimaryClassRoom, PrimaryClassRoomAdmin)

