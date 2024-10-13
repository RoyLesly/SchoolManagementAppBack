from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class PrimSchoolFeesAdmin(ImportExportModelAdmin):
    resource_class = PrimSchoolFeesResource
    list_display = ("id", "primaryprofile", "platform_charges", "platform_paid", "balance", "created_at", "updated_at")
    search_fields = ("id", "primaryprofile__user__full_name", "userprofile__user__username", "userprofile__specialty__main_specialty__specialty_name", "userprofile__specialty__academic_year", "userprofile__specialty__level__level",)
admin.site.register(PrimSchoolFees, PrimSchoolFeesAdmin)


class PrimTransactionsAdmin(ImportExportModelAdmin):
    resource_class = PrimTransactionsResource
    list_display = ("id", "primschoolfees", "reason", "payment_method", "amount", "telephone", "payer_name", "status", "operator", "created_by", "updated_by")
    search_fields = (
        "id", 
        "platform_charges", 
        "schoolfees__userprofile__specialty__main_specialty__specialty_name", 
        "schoolfees__userprofile__specialty__academic_year", 
        "schoolfees__userprofile__user__full_name",
        "payment_method",
        "ref"
    )
admin.site.register(PrimTransactions, PrimTransactionsAdmin)


class PrimActivationKeyAdmin(ImportExportModelAdmin):
    resource_class = PrimActivationKeyResource
    list_display = ("id", "key", "is_used", "created_by", "updated_by")
    search_fields = (
        "id", 
        "key", 
    )
admin.site.register(PrimActivationKey, PrimActivationKeyAdmin)

