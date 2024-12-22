from django_filters import rest_framework as filters
from .models import *


class SchoolIdentificationHigherFilter(filters.FilterSet):
    id = filters.NumberFilter()
    logo = filters.CharFilter(method="filter_logo")
    code = filters.CharFilter(lookup_expr='icontains')
    version = filters.CharFilter(lookup_expr='icontains')
    director = filters.CharFilter(lookup_expr='icontains')
    platform_charges = filters.RangeFilter()
    name = filters.CharFilter(lookup_expr='icontains')
    support_number_one = filters.CharFilter(lookup_expr='icontains')
    support_number_two = filters.CharFilter(lookup_expr='icontains')
    status = filters.BooleanFilter()
    back_end = filters.CharFilter(lookup_expr='icontains')
    front_end = filters.CharFilter(lookup_expr='icontains')
    created_by = filters.NumberFilter(field_name='created_by__id')
    created_by_full_name = filters.CharFilter(field_name='created_by__full_name', lookup_expr='icontains')
    updated_by = filters.NumberFilter(field_name='updated_by__id')
    updated_by_full_name = filters.CharFilter(field_name='updated_by__full_name', lookup_expr='icontains')
    created_at = filters.DateTimeFromToRangeFilter()
    updated_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = SchoolIdentificationHigher
        fields = [
            'id', 'logo', 'code', 'version', 'director', 'platform_charges', 'name',
            'support_number_one', 'support_number_two', 'status', 'back_end', 'front_end',
            'created_by', 'created_by_full_name', 'updated_by', 'updated_by_full_name',
            'created_at', 'updated_at'
        ]
    
    def filter_logo(self, queryset, name, value):
        """Custom filter to check if logo exists or not."""
        if value.lower() == "true":
            return queryset.filter(logo__isnull=False)
        elif value.lower() == "false":
            return queryset.filter(logo__isnull=True)
        return queryset


class SchoolInfoHigherFilter(filters.FilterSet):
    campus = filters.CharFilter(lookup_expr='icontains')
    school_identification_id = filters.NumberFilter(field_name='school_identification__id')
    version = filters.CharFilter(field_name='school_identification__version', lookup_expr='icontains')
    platform_charges = filters.NumberFilter(field_name='school_identification__platform_charges', lookup_expr='iexact')
    school_name = filters.CharFilter(lookup_expr='icontains')
    short_name = filters.CharFilter(lookup_expr='icontains')
    main_school = filters.BooleanFilter()
    address = filters.CharFilter(lookup_expr='icontains')
    town = filters.CharFilter(lookup_expr='icontains')
    region = filters.CharFilter(lookup_expr='icontains')
    country = filters.CharFilter(lookup_expr='icontains')
    po_box = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    niu = filters.CharFilter(lookup_expr='icontains')
    website = filters.CharFilter(lookup_expr='icontains')
    telephone = filters.CharFilter(lookup_expr='icontains')

    created_by_id = filters.NumberFilter(field_name='created_by__id', lookup_expr="exact")
    updated_by_id = filters.NumberFilter(field_name='updated_by__id', lookup_expr="exact")
    created_by_full_name = filters.CharFilter(field_name='created_by__full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by__full_name', lookup_expr="icontains") 
    created_at = filters.DateTimeFromToRangeFilter()
    updated_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = SchoolInfoHigher
        fields = [
            'id', 'campus', 'school_identification_id', 'version', 'platform_charges',
            'school_name', 'short_name', 'main_school', 'address', 'town',
            'region', 'country', 'po_box', 'email', 'niu', 'website', 'telephone',
            'created_at', 'updated_at'
        ]


class DomainFilter(filters.FilterSet):
    domain_name = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateTimeFromToRangeFilter()
    updated_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Domain
        fields = ['domain_name', 'created_at', 'updated_at']


class FieldFilter(filters.FilterSet):
    field_name = filters.CharFilter(lookup_expr='icontains')
    domain_id = filters.NumberFilter(field_name='domain__id')
    domain_name = filters.CharFilter(field_name='domain__domain_name', lookup_expr='icontains')
       
    created_by_id = filters.NumberFilter(field_name='created_by__id', lookup_expr="exact")
    updated_by_id = filters.NumberFilter(field_name='updated_by__id', lookup_expr="exact")
    created_by_full_name = filters.CharFilter(field_name='created_by__full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by__full_name', lookup_expr="icontains")
     

    class Meta:
        model = Field
        fields = ['field_name', 'domain', 'domain_name', 'created_at', 'updated_at']


class MainSpecialtyFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    specialty_name = filters.CharFilter(lookup_expr="icontains")
    specialty_name_short = filters.CharFilter(lookup_expr="icontains")
    field_id = filters.NumberFilter(field_name="field__id", lookup_expr="exact")
    field_name = filters.CharFilter(field_name="field__field_name", lookup_expr="icontains")
    domain_id = filters.NumberFilter(field_name="field__domain__id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="field__domain__domain_name", lookup_expr="icontains")
      
    created_by_id = filters.NumberFilter(field_name='created_by__id', lookup_expr="exact")
    updated_by_id = filters.NumberFilter(field_name='updated_by__id', lookup_expr="exact")
    created_by_full_name = filters.CharFilter(field_name='created_by__full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by__full_name', lookup_expr="icontains")
     

    class Meta:
        model = MainSpecialty
        fields = [
            "id",
            "specialty_name",
            "specialty_name_short",
            "field_id",
            "field_name",
            "domain_id",
            "domain_name",
            "created_at",
            "created_by",
            "updated_by",
        ]


class SpecialtyFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    domain_id = filters.NumberFilter(field_name="main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="main_specialty__field__domain__domain_name", lookup_expr="icontains")
    field_id = filters.NumberFilter(field_name="main_specialty__field__id", lookup_expr="exact")
    field_name = filters.CharFilter(field_name="main_specialty__field__field_name", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="school__id", lookup_expr="exact")
    school_campus = filters.CharFilter(field_name="school__campus", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="school__id", lookup_expr="exact")
    school_campus = filters.CharFilter(field_name="school__campus", lookup_expr="icontains")
    academic_year = filters.CharFilter(lookup_expr="icontains")
    tuition = filters.NumberFilter(lookup_expr="exact")
    registration = filters.NumberFilter(lookup_expr="exact")
    level_id = filters.NumberFilter(field_name="level__id", lookup_expr="exact")
    level = filters.NumberFilter(field_name="level__level", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="main_specialty__specialty_name", lookup_expr="icontains")

    class Meta:
        model = Specialty
        fields = [
            "id",
            "domain_id",
            "domain_name",
            "field_id",
            "field_name",
            "school_id",
            "school_campus",
            "academic_year",
            "tuition",
            "registration",
            "level_id",
            "level",
            "specialty_name",
        ]


class MainCourseFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    course_name = filters.CharFilter(lookup_expr="icontains")
    created_at = filters.DateFilter(lookup_expr="exact")
    created_by = filters.NumberFilter(field_name="created_by__id", lookup_expr="exact")

    class Meta:
        model = MainCourse
        fields = [
            "id",
            "course_name",
            "created_at",
            "created_by",
        ]


class CourseFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    course_name = filters.CharFilter(lookup_expr="icontains")
    course_code = filters.CharFilter(lookup_expr="icontains")
    course_type = filters.CharFilter(lookup_expr="exact")
    semester = filters.CharFilter(lookup_expr="exact")
    course_credit = filters.NumberFilter(lookup_expr="exact")
    specialty_id = filters.NumberFilter(field_name="specialty__id", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="specialty__main_specialty__specialty_name", lookup_expr="icontains")
    course_name = filters.CharFilter(field_name="main_course__course_name", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="specialty__school__id", lookup_expr="exact")
    academic_year = filters.CharFilter(field_name="specialty__academic_year", lookup_expr="exact")
    level_id = filters.NumberFilter(field_name="specialty__level__id", lookup_expr="exact")
    level = filters.NumberFilter(field_name="specialty__level__level", lookup_expr="exact")
    school_campus = filters.CharFilter(field_name="specialty__school__campus", lookup_expr="icontains")
    assigned_to_id = filters.NumberFilter(field_name="assigned_to__id", lookup_expr="exact")
    completed = filters.BooleanFilter(lookup_expr="exact")
    paid = filters.BooleanFilter(lookup_expr="exact")

    class Meta:
        model = Course
        fields = [
            "id",
            "course_name",
            "course_code",
            "course_type",
            "semester",
            "course_credit",
            "specialty_id",
            "specialty_name",
            "school_id",
            "academic_year",
            "level_id",
            "level",
            "school_campus",
            "assigned_to_id",
            "completed",
            "paid",
        ]



class CourseUploadFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    title = filters.CharFilter(lookup_expr="icontains")
    course_id = filters.CharFilter(field_name="course__id", lookup_expr="exact")
    created_at = filters.DateFilter(lookup_expr="exact")

    class Meta:
        model = CourseUpload
        fields = ["id", "title", "course_id", "created_at"]



class CourseModuleFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    course_id = filters.CharFilter(field_name="course__id", lookup_expr="exact")
    module_title = filters.CharFilter(lookup_expr="icontains")
    description = filters.CharFilter(lookup_expr="icontains")
    created_at = filters.DateFilter(lookup_expr="exact")

    class Meta:
        model = CourseModule
        fields = ["id", "course_id", "module_title", "description", "created_at"]



class CourseModuleDetailFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    course_id = filters.CharFilter(field_name="course_module__course__id", lookup_expr="exact")
    detail_title = filters.CharFilter(lookup_expr="icontains")
    description = filters.CharFilter(lookup_expr="icontains")
    created_at = filters.DateFilter(lookup_expr="exact")

    class Meta:
        model = CourseModuleDetail
        fields = ["id", "course_id", "detail_title", "description", "created_at"]



class ResultFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    domain_id = filters.NumberFilter(field_name="course__specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="course__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    field_id = filters.NumberFilter(field_name="course__specialty__main_specialty__field__id", lookup_expr="exact")
    specialty_id = filters.NumberFilter(field_name="course__specialty__id", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="specialty__main_specialty__specialty_name", lookup_expr="icontains")
    level_id = filters.NumberFilter(field_name="course__specialty__level__id", lookup_expr="exact")
    level = filters.NumberFilter(field_name="course__specialty__level__level", lookup_expr="exact")
    academic_year = filters.CharFilter(field_name="course__specialty__level__level", lookup_expr="iexact")
    school_id = filters.NumberFilter(field_name="course__specialty__school__id", lookup_expr="exact")
    campus = filters.CharFilter(field_name="course__specialty__campus", lookup_expr="icontains")
    course_name = filters.CharFilter(field_name="course__main_course__course_name", lookup_expr="icontains")
    course_id = filters.NumberFilter(field_name="course__id", lookup_expr="exact")
    semester = filters.CharFilter(field_name="course__semester", lookup_expr="iexact")
    assigned_to_id = filters.NumberFilter(field_name="course__assigned_to__id", lookup_expr="exact")
    user_id = filters.CharFilter(field_name="student__user__id", lookup_expr="icontains")
    full_name = filters.CharFilter(field_name="student__user__full_name", lookup_expr="icontains")
    matricle = filters.CharFilter(field_name="student__user__matricle", lookup_expr="icontains")
    student_id = filters.NumberFilter(field_name="student__id", lookup_expr="exact")

    ca = filters.NumberFilter(lookup_expr="exact")
    exam = filters.NumberFilter(lookup_expr="exact")
    resit = filters.NumberFilter(lookup_expr="exact")
    average = filters.NumberFilter(lookup_expr="exact")

    validated = filters.BooleanFilter(lookup_expr="exact")
    publish_ca = filters.BooleanFilter(lookup_expr="exact")
    publish_exam = filters.BooleanFilter(lookup_expr="exact")
    publish_resit = filters.BooleanFilter(lookup_expr="exact")
    closed = filters.BooleanFilter(lookup_expr="exact")
    active = filters.BooleanFilter(lookup_expr="exact")

    created_by_id = filters.NumberFilter(field_name='created_by__id', lookup_expr="exact")
    updated_by_id = filters.NumberFilter(field_name='updated_by__id', lookup_expr="exact")
    created_by_full_name = filters.CharFilter(field_name='created_by__full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by__full_name', lookup_expr="icontains")
     

    class Meta:
        model = Result
        fields = [
            "id",
            "domain_id", 'domain_name',"field_id", "specialty_id", 'specialty_name', "level_id", 'level', 'academic_year',
            "school_id", 'campus',
            'course_name',
            'course_id',
            'semester',
            "assigned_to_id",
            'user_id',
            "full_name",
            "matricle",
            "student_id",
            "ca",
            "exam",
            "resit",
            "average",
            "validated",
            "publish_ca",
            "publish_exam",
            "publish_resit",
            "closed",
            "active",
            "created_by_id",
            "updated_by_id",
        ]


class PublishFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    domain_id = filters.NumberFilter(field_name="domain_id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    specialty_id = filters.NumberFilter(field_name="specialty__id", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="specialty__main_specialty__specialty_name", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="specialty__school__id", lookup_expr="exact")
    campus = filters.CharFilter(field_name="specialty__school__campus", lookup_expr="icontains")
    region = filters.CharFilter(field_name="specialty__school__region", lookup_expr="icontains")
    level = filters.NumberFilter(field_name="specialty__level__level", lookup_expr='exact')
    academic_year = filters.CharFilter(field_name="specialty__academic_year", lookup_expr="icontains")

    semester = filters.CharFilter(lookup_expr="iexact")
    ca = filters.BooleanFilter(lookup_expr="exact")
    exam = filters.BooleanFilter(lookup_expr="exact")
    resit = filters.BooleanFilter(lookup_expr="exact")
    portal_ca = filters.BooleanFilter(lookup_expr="exact")
    portal_exam = filters.BooleanFilter(lookup_expr="exact")
    portal_resit = filters.BooleanFilter(lookup_expr="exact")

    created_by_id = filters.NumberFilter(field_name='created_by__id', lookup_expr="exact")
    updated_by_id = filters.NumberFilter(field_name='updated_by__id', lookup_expr="exact")
    created_by_full_name = filters.CharFilter(field_name='created_by__full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by__full_name', lookup_expr="icontains")
     

    class Meta:
        model = Publish
        fields = [
            'id', 
            'domain_id', 'domain_name', 'specialty_id','specialty_name', 'school_id', 'campus', 'region', 'level', 'academic_year',
            'semester', 
            'ca', 
            'exam', 
            'resit', 
            'portal_ca', 
            'portal_exam', 
            'portal_resit', 
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",        
        ]

class LevelFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    level = filters.NumberFilter(lookup_expr="exact")

    class meta:
        model = Level


class SysCategoryFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    name = filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = SysCategory


class SysConstantFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="exact")
    name = filters.CharFilter(lookup_expr="icontains")
    sys_category_id = filters.NumberFilter(field_name="sys_category__id", lookup_expr="icontains")
    sys_category_name = filters.CharFilter(field_name="sys_category__name", lookup_expr="icontains")

    class meta:
        model = SysConstant

        
        