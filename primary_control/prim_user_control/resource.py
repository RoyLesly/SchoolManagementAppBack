from import_export import resources 
from .models import *


class PrimaryProfileResource(resources.ModelResource):
    class Meta:
        model = PrimaryProfile
