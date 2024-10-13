from import_export import resources 
from .models import * 


class NotificationResource(resources.ModelResource):
    class Meta:
        model = Notification


class ComplainResource(resources.ModelResource):
    class Meta:
        model = Complain

        
class UserActivityResource(resources.ModelResource):
    class Meta:
        model = UserActivity
        