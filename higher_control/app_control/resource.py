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


class CourseUploadResource(resources.ModelResource):
    class Meta:
        model = CourseUpload


class CourseModuleResource(resources.ModelResource):
    class Meta:
        model = CourseModule


class CourseModuleDetailResource(resources.ModelResource):
    class Meta:
        model = CourseModuleDetail


class PublishResource(resources.ModelResource):
    class Meta:
        model = Publish


class LevelResource(resources.ModelResource):
    class Meta:
        model = Level


class ResultResource(resources.ModelResource):
    class Meta:
        model = Result


class SchoolInfoHigherResource(resources.ModelResource):
    class Meta:
        model = SchoolInfoHigher


class SchoolIdentificationHigherResource(resources.ModelResource):
    class Meta:
        model = SchoolIdentificationHigher
        

class SysCategoryResource(resources.ModelResource):
    class Meta:
        model = SysCategory

class SysConstantResource(resources.ModelResource):
    class Meta:
        model = SysConstant
        
    
        