from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class SecondaryPublishAdmin(ImportExportModelAdmin):
    resource_class = SecondaryPublishResource
    list_display = ("id", "secondary_classroom", "portal", "publish_type", "publish_item", "publish", "created_at", "updated_at", "updated_by")
    search_fields = ("id", "secondary_classroom",)
admin.site.register(SecondaryPublish, SecondaryPublishAdmin)


class SecondaryLevelAdmin(ImportExportModelAdmin):
    resource_class = SecondaryLevelResource
    list_display = ("id", "level", "option")
admin.site.register(SecondaryLevel, SecondaryLevelAdmin)


class SecondaryClassRoomAdmin(ImportExportModelAdmin):
    resource_class = SecondaryClassRoomResource
    list_display = ("id", "school", "level", "domain", "tuition", "payment_one", "payment_two", "payment_three", "registration", "academic_year", "created_at", "updated_at")
    search_fields = ("academic_year", "id", "main_classroom__classroom_name",)
admin.site.register(SecondaryClassRoom, SecondaryClassRoomAdmin)


class SecondaryMainSubjectAdmin(ImportExportModelAdmin):
    resource_class = SecondaryMainSubjectResource
    list_display = ("id", "subject_name", "created_at", "updated_at")
    search_fields = ("subject_name", "id",)
admin.site.register(SecondaryMainSubject, SecondaryMainSubjectAdmin)


class SecondarySubjectAdmin(ImportExportModelAdmin):
    resource_class = SecondarySubjectResource
    list_display = ("id", "classroom", "subject_code", "subject_type",  "subject_coefficient", "date_assigned",
                    "assigned_to", "assigned", "created_at", "updated_at")
    search_fields = ("classroom__main_classroom", "main_subject__subject_name", "subject_code", "id",)
admin.site.register(SecondarySubject, SecondarySubjectAdmin)


class SecondaryResultAdmin(ImportExportModelAdmin):
    resource_class = SecondaryResultResource
    list_display = ("id", "student", "subject", "active", 
                    "seq_1", "seq_2", "seq_3", "seq_4", "seq_5", "seq_6",
                    # "exam_1", "exam_2", "exam_3", 
                    # "test_1", "test_2",
                    "passed_1", "passed_2", "passed_3", 
                    "average_term_1", "average_term_2", "average_term_3",
                    "publish_term_1", "publish_term_2", "publish_term_3",
                    "publish_seq_1", "publish_seq_2", "publish_seq_3", "publish_seq_4", "publish_seq_5", "publish_seq_6",
                    "created_at", "updated_at", "updated_by")
    search_fields = ("id", "student__user__username", "student__user__full_name", "subject__main_subject__subject_name",)
admin.site.register(SecondaryResult, SecondaryResultAdmin)

