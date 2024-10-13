from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class SecSchoolFeesAdmin(ImportExportModelAdmin):
    resource_class = SecSchoolFeesResource
    list_display = ("id", "secondaryprofile", "platform_charges", "platform_paid", "balance", "created_at", "updated_at")
    search_fields = ("id", "secondaryprofile__user__full_name", "userprofile__user__username", "userprofile__specialty__main_specialty__specialty_name", "userprofile__specialty__academic_year", "userprofile__specialty__level__level",)
admin.site.register(SecSchoolFees, SecSchoolFeesAdmin)


class SecTransactionsAdmin(ImportExportModelAdmin):
    resource_class = SecTransactionsResource
    list_display = ("id", "secschoolfees", "reason", "payment_method", "amount", "telephone", "payer_name", "status", "operator", "created_by", "updated_by")
    search_fields = (
        "id", 
        "platform_charges", 
        "schoolfees__userprofile__specialty__main_specialty__specialty_name", 
        "schoolfees__userprofile__specialty__academic_year", 
        "schoolfees__userprofile__user__full_name",
        "payment_method",
        "ref"
    )
admin.site.register(SecTransactions, SecTransactionsAdmin)


class ActivationKeyAdmin(ImportExportModelAdmin):
    resource_class = ActivationKeyResource
    list_display = ("id", "key", "is_used", "created_by", "updated_by")
    search_fields = (
        "id", 
        "key", 
    )
admin.site.register(ActivationKey, ActivationKeyAdmin)

