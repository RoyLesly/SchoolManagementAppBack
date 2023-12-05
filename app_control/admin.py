from django.contrib import admin
from .models import *


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("id", "domain_name", "created_at", "updated_at")
    search_fields = ("", "id",)

@admin.register(MainCourse)
class MainCourseAdmin(admin.ModelAdmin):
    list_display = ("id", "course_name", "created_at", "updated_at")
    search_fields = ("", "id",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "specialty", "course_code", "course_credit",  "semester", "course_type",
                    "completed", "assigned_to", "assigned", "created_at", "updated_at")
    search_fields = ("", "id",)

@admin.register(MainSpecialty)
class MainSpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "specialty_name", "domain", "created_at", "updated_at")
    search_fields = ("", "id",)

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "main_specialty", "academic_year", "level", "created_at", "updated_at")
    search_fields = ("", "id",)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "ca", "exam", "resit",
                    "average", "validated", "closed", "paid", "created_at", "updated_at")
    search_fields = ("", "id",)
