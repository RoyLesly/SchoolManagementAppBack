from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ("id", "main_course", "specialty", "course_code", "course_credit",  "semester", "course_type", "hours", "hours_left", "date_assigned",
                    "completed", "paid", "assigned_to", "assigned", "created_at", "updated_at")
    search_fields = ("main_course__course_name", "course_code", "semester",)
admin.site.register(Course, CourseAdmin)


class PublishAdmin(ImportExportModelAdmin):
    resource_class = PublishResource
    list_display = ("id", "specialty", "semester", "ca", "exam", "resit", "portal_ca", "portal_exam", "portal_resit", "created_at", "updated_at", "updated_by")
    search_fields = ("id", "specialty",)
admin.site.register(Publish, PublishAdmin)


class DomainAdmin(ImportExportModelAdmin):
    resource_class = DomainResource
    list_display = ("id", "domain_name", "created_by", "created_at", "updated_at")
    search_fields = ("domain_name", )
admin.site.register(Domain, DomainAdmin)


class FieldAdmin(ImportExportModelAdmin):
    resource_class = FieldResource
    list_display = ("id", "field_name", "domain", "created_at", "updated_at")
    search_fields = ("field_name", "domain",)
admin.site.register(Field, FieldAdmin)


class MainSpecialtyAdmin(ImportExportModelAdmin):
    resource_class = MainSpecialtyResource
    list_display = ("id", "specialty_name", "specialty_name_short", "field", "created_at", "updated_at")
    search_fields = ("specialty_name", "domain", "field")
admin.site.register(MainSpecialty, MainSpecialtyAdmin)


class SpecialtyAdmin(ImportExportModelAdmin):
    resource_class = SpecialtyResource
    list_display = ("id", "main_specialty", "school", "academic_year", "level", "tuition", "registration", "payment_one", "payment_two", "created_at", "updated_at")
    search_fields = ("academic_year", "id", "main_specialty__specialty_name",)
admin.site.register(Specialty, SpecialtyAdmin)


class MainCourseAdmin(ImportExportModelAdmin):
    resource_class = MainCourseResource
    list_display = ("id", "course_name", "created_at", "updated_at")
    search_fields = ("course_name", "id",)
admin.site.register(MainCourse, MainCourseAdmin)


class LevelAdmin(ImportExportModelAdmin):
    resource_class = LevelResource
    list_display = ("id", "level", "created_at", "updated_at")
    search_fields = ("level", "id",)
admin.site.register(Level, LevelAdmin)


class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource
    list_display = ("id", "student", "course", "ca", "exam", "resit", "average", "validated", "active",
                    "publish_ca", "publish_exam", "publish_resit","closed", "created_at", "updated_at", "updated_by")
    search_fields = ("student__user__username", "student__user__matricle", "student__user__first_name", "course__main_course__course_name",)
admin.site.register(Result, ResultAdmin)


class CampusAdmin(ImportExportModelAdmin):
    resource_class = CampusResource
    list_display = ("id", "name", "region", "created_by", "created_at")
    search_fields = ("name", "region",)
admin.site.register(Campus, CampusAdmin)


class SchoolInfoAdmin(ImportExportModelAdmin):
    resource_class = SchoolInfoResource
    list_display = ("id", "school_name", "school_identification", "short_name", "niu", "town", "campus", "region", "email", "website", "address", "telephone_one", "created_at")
    search_fields = ("id", "school_name",)
admin.site.register(SchoolInfo, SchoolInfoAdmin)


class SchoolIdentificationAdmin(ImportExportModelAdmin):
    resource_class = SchoolIdentificationResource
    list_display = ("id", "code", "name", "status", "back_end", "created_by", "created_at")
    search_fields = ("id", "code", "name",)
admin.site.register(SchoolIdentification, SchoolIdentificationAdmin)


class SysCategoryAdmin(ImportExportModelAdmin):
    resource_class = SysCategoryResource
    list_display = ("id", "name",)
    search_fields = ("id", "name",)
admin.site.register(SysCategory, SysCategoryAdmin)


class SysConstantAdmin(ImportExportModelAdmin):
    resource_class = SysConstantResource
    list_display = ("id", "name", "created_by", "created_at")
    search_fields = ("id", "name",)
admin.site.register(SysConstant, SysConstantAdmin)


