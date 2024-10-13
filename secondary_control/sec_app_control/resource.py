from import_export import resources 
from .models import *


class SecondaryLevelResource(resources.ModelResource):
    class Meta:
        model = SecondaryLevel

class SecondaryClassRoomResource(resources.ModelResource):
    class Meta:
        model = SecondaryClassRoom
        
        
class SecondaryMainSubjectResource(resources.ModelResource):
    class Meta:
        model = SecondaryMainSubject


class SecondarySubjectResource(resources.ModelResource):
    class Meta:
        model = SecondarySubject


class SecondaryPublishResource(resources.ModelResource):
    class Meta:
        model = SecondaryPublish

class SecondaryResultResource(resources.ModelResource):
    class Meta:
        model = SecondaryResult

