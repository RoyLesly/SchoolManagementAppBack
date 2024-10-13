from import_export import resources 
from .models import *


class TenantResource(resources.ModelResource):
    class Meta:
        model = Tenant

class DomainResource(resources.ModelResource):
    class Meta:
        model = Domain
