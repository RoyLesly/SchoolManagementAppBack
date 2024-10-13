from import_export import resources 
from .models import *


class PrimSchoolFeesResource(resources.ModelResource):
    class Meta:
        model = PrimSchoolFees

class PrimTransactionsResource(resources.ModelResource):
    class Meta:
        model = PrimTransactions

class PrimActivationKeyResource(resources.ModelResource):
    class Meta:
        model = PrimActivationKey
         
 
