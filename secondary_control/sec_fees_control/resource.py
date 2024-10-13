from import_export import resources 
from .models import *


class SecSchoolFeesResource(resources.ModelResource):
    class Meta:
        model = SecSchoolFees

class SecTransactionsResource(resources.ModelResource):
    class Meta:
        model = SecTransactions

class ActivationKeyResource(resources.ModelResource):
    class Meta:
        model = ActivationKey
         
 
