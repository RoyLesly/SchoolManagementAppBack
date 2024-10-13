from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import get_public_schema_name
from import_export.admin import ImportExportModelAdmin
from .resource import *


from .models import Domain, Tenant


class PublicTenantOnlyMixin:
    #Allow Access to public Tenant Only
    def __only_public_tenant_access(self, request):
        return True if request.tenant.schema_name == get_public_schema_name() else False
    
    def has_view_permission(self, request, view=None):
        return self.__only_public_tenant_access(request)
    
    def has_add_permission(self, request, view=None):
        return self.__only_public_tenant_access(request)
    
    def has_change_permission(self, request, view=None):
        return self.__only_public_tenant_access(request)
    
    def has_delete_permission(self, request, view=None):
        return self.__only_public_tenant_access(request)
    
    def has_view_or_change_permission(self, request, view=None):
        return self.__only_public_tenant_access(request)
    

class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1


@admin.register(Tenant)
class TenantAdmin(PublicTenantOnlyMixin, TenantAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "school_name",
        "is_active",
        "description",
        "created_on",
    )
    inlines = [DomainInline]


class DomainAdmin(ImportExportModelAdmin):
    resource_class = DomainResource
    list_display = ( "id", "domain", "is_primary", "tenant" )
    search_fields = ( "id", "domain" )
admin.site.register(Domain, DomainAdmin)
