from import_export import resources 
from .models import *


class DomainResource(resources.ModelResource):
    class Meta:
        model = Domain
        
        
class FieldResource(resources.ModelResource):
    class Meta:
        model = Field


class MainSpecialtyResource(resources.ModelResource):
    class Meta:
        model = MainSpecialty
         

class SpecialtyResource(resources.ModelResource):
    class Meta:
        model = Specialty
        
        
class MainCourseResource(resources.ModelResource):
    class Meta:
        model = MainCourse


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course


class PublishResource(resources.ModelResource):
    class Meta:
        model = Publish


class LevelResource(resources.ModelResource):
    class Meta:
        model = Level


class CampusResource(resources.ModelResource):
    class Meta:
        model = Campus
        

class ResultResource(resources.ModelResource):
    class Meta:
        model = Result


class SchoolInfoResource(resources.ModelResource):
    class Meta:
        model = SchoolInfo


class SchoolIdentificationResource(resources.ModelResource):
    class Meta:
        model = SchoolIdentification

class SysCategoryResource(resources.ModelResource):
    class Meta:
        model = SysCategory

class SysConstantResource(resources.ModelResource):
    class Meta:
        model = SysConstant
        
    
        