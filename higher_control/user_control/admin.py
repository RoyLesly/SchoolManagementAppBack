from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin


class UserProfileAdmin(ImportExportModelAdmin):
    resource_class = UserProfileResource
    list_display = ("id", "user", "specialty", "program", "session", "active", "created_at", "updated_at")
    search_fields = ("specialty__main_specialty__specialty_name", "id", "user__first_name", "user__matricle",)
    list_filter = ["user__role", "user__is_active", "specialty__academic_year", "user__is_staff", "user__school__id", "specialty__school__id", "specialty__id"]
admin.site.register(UserProfile, UserProfileAdmin)


class AppearanceAdmin(ImportExportModelAdmin):
    resource_class = AppearanceResource
    list_display = ("id", "user", "dark_mode", "lang", "created_at", "updated_at")
    search_fields = ('id', "user__username", "user__matricle", "user__first_name")
admin.site.register(Appearance, AppearanceAdmin)


class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ('id', 'name', "created_by", "created_at", "updated_at")
    search_fields = ('name',)
admin.site.register(Department, DepartmentAdmin)


class PageAdmin(ImportExportModelAdmin):
    resource_class = PageResource
    list_display = ('id', 'name', "created_by", "created_at", "updated_at")
    search_fields = ('name',)
admin.site.register(Page, PageAdmin)


class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource
    list_display = ('id', 'name', "created_by", "created_at", "updated_at")
    search_fields = ('name',)
admin.site.register(Program, ProgramAdmin)


class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource
    list_display = ('id', 'matricle', 'username', "full_name", "role", "email", "email_confirmed", 
                    "hod", "sex", "parent", "address", "telephone", "parent_telephone", "title", "dob", "pob",)
    search_fields = ('id', 'username', "full_name", 'matricle')
    list_filter = ["role", "is_active", "is_staff", "school__id", "school__id"]
admin.site.register(CustomUser, CustomUserAdmin)


class PreInscriptionAdmin(ImportExportModelAdmin):
    resource_class = PreInscriptionResource
    list_display = ('id', 'registration_number', "full_name", "campus", "email", "sex", "status", "admission_status", "emergency_name", "address", "telephone", "dob", "pob", "created_at",)
    search_fields = ('id', "full_name", 'registration_number')
admin.site.register(PreInscription, PreInscriptionAdmin)

