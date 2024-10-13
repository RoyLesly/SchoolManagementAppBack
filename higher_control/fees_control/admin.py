from django.contrib import admin
from .models import *
from .resource import *
from import_export.admin import ImportExportModelAdmin


class ActivationKeyAdmin(ImportExportModelAdmin):
    resource_class = ActivationKeyResource
    list_display = ("id", "key", "is_used", "created_by", "updated_by")
    search_fields = (
        "id", 
        "key", 
    )
admin.site.register(ActivationKey, ActivationKeyAdmin)


class SchoolFeesAdmin(ImportExportModelAdmin):
    resource_class = SchoolFeesResource
    list_display = ("id", "userprofile", "platform_charges", "platform_paid", "balance", "created_at", "updated_at")
    search_fields = ("id", "userprofile__user__matricle", "userprofile__user__full_name", "userprofile__user__username", "userprofile__specialty__main_specialty__specialty_name", "userprofile__specialty__academic_year", "userprofile__specialty__level__level",)
admin.site.register(SchoolFees, SchoolFeesAdmin)


class AccountAdmin(ImportExportModelAdmin):
    resource_class = AccountResource
    list_display = ( "id", "name", "number", "year", "balance" )
    search_fields = ( "id", "name", "number", "balance" )
admin.site.register(Account, AccountAdmin)


class TransactionsAdmin(ImportExportModelAdmin):
    resource_class = TransactionsResource
    list_display = ("id", "schoolfees", "account", "reason", "operation_type", "from_account", "to_account", "payment_method", "amount", "telephone", 
                    "payer_name", "status", "operator", "created_by", "updated_by")
    search_fields = (
        "id", 
        "platform_charges", 
        "schoolfees__userprofile__specialty__main_specialty__specialty_name", 
        "schoolfees__userprofile__specialty__academic_year", 
        "schoolfees__userprofile__user__full_name",
        "payment_method",
        "ref"
    )
admin.site.register(Transactions, TransactionsAdmin)


class TranscriptApplicationAdmin(ImportExportModelAdmin):
    resource_class = TranscriptApplicationResource
    list_display = ( "id", "userprofile", "status", "approved_by", "approved_at", "created_at", "printed_by", "printed_at" )
    search_fields = ( "id", "status" )
admin.site.register(TranscriptApplication, TranscriptApplicationAdmin)

