from import_export import resources 
from .models import *


class PrimaryLevelResource(resources.ModelResource):
    class Meta:
        model = PrimaryLevel

class PrimaryClassRoomResource(resources.ModelResource):
    class Meta:
        model = PrimaryClassRoom
        