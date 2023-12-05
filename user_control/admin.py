from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdminConfig(admin.ModelAdmin):
    # model = CustomUser
    list_display = (  'id', 'username', "first_name", "last_name", "role", "email", "email_confirmed", 
                    "hod", "sex", "address", "telephone", "title", "dob", )
    search_fields = ('username',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "specialty", "created_at", "updated_at")
    search_fields = ("", "id",)


@admin.register(Appearance)
class AppearanceAdmin(admin.ModelAdmin):
    list_display = ("id", "dark_mode", "lang", "created_at", "updated_at")
    search_fields = ("", "id",)


@admin.register(PasswordToken)
class PasswordTokenAdmin(admin.ModelAdmin):
    list_display = ("id", "user_profile", "token", "expired", "sent_mail", "created_at", "updated_at")
    search_fields = ("", "id",)


admin.site.register(UserActivities,)
# admin.site.register(( CustomUser, UserActivities, ))
