from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class TimeTableWeekAdmin(ImportExportModelAdmin):
    resource_class = TimeTableWeekResource
    list_display = ("id", "specialty", "year_week", "publish", "created_at", "updated_at")
    search_fields = ("specialty__main_specialty__specialty_name", "year_week", "id",)
    list_filter = ["year_week", "specialty_id", "publish"]
admin.site.register(TimeTableWeek, TimeTableWeekAdmin)


class TimeTableDayAdmin(ImportExportModelAdmin):
    resource_class = TimeTableDayResource
    list_display = ("id", "day", "timetableweek",)
    search_fields = ("date", "day", "timetableweek__year_week", "created_by", "created_at")
    list_filter = ["timetableweek__year_week", "timetableweek__specialty_id", "timetableweek__publish", "day", "date"]
admin.site.register(TimeTableDay, TimeTableDayAdmin)


class TimeSlotAdmin(ImportExportModelAdmin):
    resource_class = TimeSlotResource
    list_display = ("id", "title", "status", "start", "end", "course", "start_time", "end_time", "action", "session", "hours", "created_at",)
    search_fields = ("title", "start", "course__main_course__course_name", "course__assigned_to__full_name", "created_by", "created_at")
    list_filter = ["course__main_course__course_name", "timetableday__timetableweek__year_week", "timetableday__timetableweek__specialty_id", "timetableday__day", "timetableday__date"]
admin.site.register(TimeSlot, TimeSlotAdmin)
