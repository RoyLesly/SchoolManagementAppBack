from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin


class NotificationAdmin(ImportExportModelAdmin):
    resource_class = NotificationResource
    list_display = ("id", "message", "role", "noti_type", "custom", "status", "ending_at", "created_at", "updated_at")
    search_fields = ("role", "message_one", "status", "noti_type", "custom",)
admin.site.register(Notification, NotificationAdmin)


class ComplainAdmin(ImportExportModelAdmin):
    resource_class = ComplainResource
    list_display = ("id", "message", "status", "complain_type", "ending_at", "created_at", "updated_at")
    search_fields = ("message_one", "status", "complain_type",)
admin.site.register(Complain, ComplainAdmin)


class UserActivityAdmin(ImportExportModelAdmin):
    resource_class = UserActivityResource
    list_display = ("id", "user", "action", "item", "details", "updated_at")
    search_fields = ('user',)
admin.site.register(UserActivity, UserActivityAdmin)

