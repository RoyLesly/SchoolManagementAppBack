from import_export import resources 
from .models import *


class SchoolFeesResource(resources.ModelResource):
    class Meta:
        model = SchoolFees

class TransactionsResource(resources.ModelResource):
    class Meta:
        model = Transactions

class AccountResource(resources.ModelResource):
    class Meta:
        model = Account

class TranscriptApplicationResource(resources.ModelResource):
    class Meta:
        model = TranscriptApplication

class ActivationKeyResource(resources.ModelResource):
    class Meta:
        model = ActivationKey
         
 
