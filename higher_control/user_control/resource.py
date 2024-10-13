from import_export import resources 
from .models import * 

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

class PreInscriptionResource(resources.ModelResource):
    class Meta:
        model = PreInscription
        
class AppearanceResource(resources.ModelResource):
    class Meta:
        model = Appearance
        
class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile
        
class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
    
class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        
class PageResource(resources.ModelResource):
    class Meta:
        model = Page
        
        
        
