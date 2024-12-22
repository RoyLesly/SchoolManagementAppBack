from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ("id", "main_course", "specialty", "course_code", "course_credit",  "semester", "course_type", "hours", "hours_left", "date_assigned",
                    "completed", "paid", "assigned_to", "assigned", "created_at", "updated_at")
    search_fields = ("id", "main_course__course_name", "specialty__school__campus__name", "assigned_to__first_name",)
    list_filter = ("main_course__course_name", "specialty__academic_year", "specialty__level__level", "specialty__school__campus", "assigned_to__first_name",)
admin.site.register(Course, CourseAdmin)


class CourseModuleAdmin(ImportExportModelAdmin):
    resource_class = CourseModuleResource
    list_display = ("id", "module_title", "description", "content", "created_at")
    search_fields = ("id", "module_title", "description", "content", "created_at")
    list_filter = ("id", "module_title", "description", "content", "created_at")
admin.site.register(CourseModule, CourseModuleAdmin)


class CourseModuleDetailAdmin(ImportExportModelAdmin):
    resource_class = CourseModuleDetailResource
    list_display = ("id", "detail_title", "description", "content", "created_at")
    search_fields = ("id", "detail_title", "description", "content", "created_at")
    list_filter = ("id", "detail_title", "description", "content", "created_at")
admin.site.register(CourseModuleDetail, CourseModuleDetailAdmin)


class CourseUploadAdmin(ImportExportModelAdmin):
    resource_class = CourseUploadResource
    list_display = ("id", "title", "created_at")
    search_fields = ("id", "title", "created_at")
    list_filter = ("id", "title", "created_at",)
admin.site.register(CourseUpload, CourseUploadAdmin)


class PublishAdmin(ImportExportModelAdmin):
    resource_class = PublishResource
    list_display = ("id", "specialty", "semester", "ca", "exam", "resit", "portal_ca", "portal_exam", "portal_resit", "created_at", "updated_at", "updated_by")
    search_fields = ("id", "specialty",)
    list_filter = ("semester", "specialty__academic_year", "specialty__level__level", "specialty__school__campus", "specialty__main_specialty__field__domain__domain_name")
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
    search_fields = ("id", "specialty_name", "field__field_name", "field__domain__domain_name",)
    list_filter = ("id", "specialty_name", "field__field_name", "field__domain__domain_name",)
admin.site.register(MainSpecialty, MainSpecialtyAdmin)


class SpecialtyAdmin(ImportExportModelAdmin):
    resource_class = SpecialtyResource
    list_display = ("id", "main_specialty", "school", "academic_year", "level", "tuition", "registration", "payment_one", "payment_two", "created_at", "updated_at")
    search_fields = ("academic_year", "id", "main_specialty__specialty_name",)
    list_filter = ("level__level", "academic_year", "main_specialty__specialty_name", "school__campus",)
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
    list_filter = ("student__user__username", "student__user__matricle", "student__user__first_name", "course__main_course__course_name", "course__assigned_to__matricle", "course__specialty__level__level", "course__specialty__school__campus",)
admin.site.register(Result, ResultAdmin)


class SchoolInfoHigherAdmin(ImportExportModelAdmin):
    resource_class = SchoolInfoHigherResource
    list_display = ("id", "school_name", "school_identification", "short_name", "niu", "town", "campus", "region", "email", "website", "address", "telephone", "created_at")
    search_fields = ("id", "school_name",)
admin.site.register(SchoolInfoHigher, SchoolInfoHigherAdmin)


class SchoolIdentificationHigherAdmin(ImportExportModelAdmin):
    resource_class = SchoolIdentificationHigherResource
    list_display = ("id", "code", "name", "status", "back_end", "created_by", "created_at")
    search_fields = ("id", "code", "name",)
admin.site.register(SchoolIdentificationHigher, SchoolIdentificationHigherAdmin)


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


