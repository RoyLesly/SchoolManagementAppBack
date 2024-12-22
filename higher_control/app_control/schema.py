import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from higher_control.user_control.schema import CustomUserType, UserProfileType
from .models import *
from .schemaFilter import *


class SchoolIdentificationHigherType(DjangoObjectType):
    class Meta:
        model = SchoolIdentificationHigher
        filter_fields = ['id',]
        interfaces = (graphene.relay.Node,) 
        fields = ('id', 'logo', 'code', 'version', 'director', 'platform_charges', 'name', 'support_number_one', 'support_number_two', 'status',)


class SchoolInfoHigherType(DjangoObjectType):
    school_identification = graphene.Field(SchoolIdentificationHigherType) 
    class Meta:
        model = SchoolInfoHigher
        filter_fields = ['id',]
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "campus",
            "school_identification",
            "ca_limit",
            "exam_limit",
            "resit_limit",
            "bg_logo_transcript",
            "bg_logo_slip",
            "colors",
            "prefix",
            "method",
            "school_type",
            "school_name",
            "short_name",
            "main_school",
            "address",
            "region",
            "town",
            "country",
            "po_box",
            "niu",
            "website",
            "latitude",
            "longitude",
            "landing_message_main",
            "logo_campus",
            "registration_seperate_tuition",
            "schoolfees_control",
            "welcome_message",
            "radius",
            "email",
            "telephone",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )

class DomainType(DjangoObjectType):
    class Meta:
        model = Domain
        filter_fields = ['id', 'domain_name']
        interfaces = (graphene.relay.Node,) 
        fields = ['domain_name', 'id']


class FieldType(DjangoObjectType):
    domain = graphene.Field(DomainType)  # Return a list of UserProfiles
    class Meta:
        model = Field
        filter_fields = ['id', 'field_name']
        interfaces = (graphene.relay.Node,) 
        fields = [ 'id', 'domain', 'field_name' ]


class MainSpecialtyType(DjangoObjectType):
    field = graphene.Field(FieldType)  # Return a list of UserProfiles
    class Meta:
        model = MainSpecialty
        filter_fields = ['id', 'specialty_name']
        interfaces = (graphene.relay.Node,) 
        fields = [ 'id', 'field', 'specialty_name', 'specialty_name_short' ]

class LevelType(DjangoObjectType):
    class Meta:
        model = Level
        interfaces = (graphene.relay.Node,) 
        fields = ['id', 'level']

class SpecialtyType(DjangoObjectType):
    school = graphene.Field(SchoolInfoHigherType)  # Return a list of UserProfiles
    main_specialty = graphene.Field(MainSpecialtyType)  # Return a list of UserProfiles
    level = graphene.Field(LevelType)  # Return a list of UserProfiles
    class Meta:
        model = Specialty
        interfaces = (graphene.relay.Node,) 
        fields = [ 'id', 'school', 'main_specialty', 'level', 'academic_year', 'tuition', 'registration', 'payment_one', 'payment_two', 'payment_three' ]


class MainCourseType(DjangoObjectType):
    class Meta:
        model = MainCourse
        interfaces = (graphene.relay.Node,) 
        fields = [ 'id', 'course_name' ]


class CourseType(DjangoObjectType):
    main_course = graphene.Field(MainCourseType)  # Return a list of MainCourseType
    specialty = graphene.Field(SpecialtyType)  # Return a list of SpecialtyType
    assigned_to = graphene.Field(CustomUserType)  # Return a list of CustomUserType

    class Meta:
        model = Course
        interfaces = (graphene.relay.Node,) 
        fields = [ 
            'id', 'main_course', 'specialty', 'course_name', 'course_code', 'course_type', 'course_credit', 'semester',
            'completed', 'paid', 'hours', 'hours_left', 'assigned_to' 
        ]

class CourseUploadType(DjangoObjectType):
    class Meta:
        model = CourseUpload


class CourseModuleType(DjangoObjectType):
    class Meta:
        model = CourseModule


class CourseModuleDetailType(DjangoObjectType):
    class Meta:
        model = CourseModuleDetail


class ResultType(DjangoObjectType):
    student = graphene.Field(UserProfileType)  # Return a list of UserProfileType
    course = graphene.Field(CourseType)  # Return a list of CourseType
    created_by = graphene.Field(CustomUserType)  # Return a list of CustomUserType
    updated_by = graphene.Field(CustomUserType)  # Return a list of CustomUserType
    class Meta:
        model = Result
        interfaces = (graphene.relay.Node,) 
        filter_fields = [
            'id', 
            'student__user__id', 
            'student__id', 
            'student__user__full_name', 
            'student__user__matricle', 
            'student__specialty__main_specialty__field__domain__domain_name', 
            'student__specialty__main_specialty__Specialty_name', 
            'student__specialty__academic_year', 
            'student__specialty__level__level', 
            'student__specialty__school__campus', 
            'student__specialty__school__id', 
            'course__id', 
            'course__main_course__course_name', 
        ]
        fields = [ 
            'id', 'student', 'course', 
            'matricle', 'ca', 'exam', 'resit', 'average', 'validated', 'closed', 'active'
            'publish_ca', 'publish_exam', 'publish_resit', 
            'created_by', 'created_at', 'updated_by', 'updated_at',
        ]

class PublishType(DjangoObjectType):
    specialty = graphene.Field(SpecialtyType)  # Return a list of UserProfileType
    class Meta:
        model = Publish
        interfaces = (graphene.relay.Node,) 
        fields = [ 
            'id', 'specialty', 'semester', 'ca', 'exam', 'resit', 'portal_ca', 'portal_exam', 'portal_resit',
            'created_by', 'created_at', 'updated_by', 'updated_at',
        ]

class SysCategoryType(DjangoObjectType):
    class Meta:
        model = SysCategory


class SysConstantType(DjangoObjectType):
    class Meta:
        model = SysConstant


class Query(graphene.ObjectType):
    all_school_identifications = DjangoFilterConnectionField(SchoolIdentificationHigherType, filterset_class=SchoolIdentificationFilter)
    all_school_infos = DjangoFilterConnectionField(SchoolInfoHigherType, filterset_class=SchoolInfoHigherFilter)
    all_domains = DjangoFilterConnectionField(DomainType, filterset_class=DomainFilter)
    all_fields = DjangoFilterConnectionField(FieldType, filterset_class=FieldFilter)
    all_main_specialties = DjangoFilterConnectionField(MainSpecialtyType, filterset_class=MainSpecialtyFilter)
    all_specialties = DjangoFilterConnectionField(SpecialtyType, filterset_class=SpecialtyFilter)
    all_main_courses = DjangoFilterConnectionField(MainCourseType, filterset_class=MainCourseFilter)
    all_courses = DjangoFilterConnectionField(CourseType, filterset_class=CourseFilter)
    all_results = DjangoFilterConnectionField(ResultType, filterset_class=ResultFilter)
    all_publishes = DjangoFilterConnectionField(PublishType, filterset_class=PublishFilter)

    all_course_uploads = graphene.List(CourseUploadType)
    all_course_modules = graphene.List(CourseModuleType)
    all_course_module_details = graphene.List(CourseModuleDetailType)

    all_sys_categories = graphene.List(SysCategoryType)
    all_sys_constants = graphene.List(SysConstantType)

    def resolve_all_school_identifications(self, info, **kwargs):
        return SchoolIdentificationHigher.objects.all()

    def resolve_all_school_infos(self, info, **kwargs):
        return SchoolInfoHigher.objects.all()

    def resolve_all_domains(self, info, **kwargs):
        return Domain.objects.all()

    def resolve_all_fields(self, info, **kwargs):
        return Field.objects.all()

    def resolve_all_main_specialties(self, info, **kwargs):
        return MainSpecialty.objects.all()

    def resolve_all_levels(self, info, **kwargs):
        return Level.objects.all()

    def resolve_all_specialties(self, info, **kwargs):
        return Specialty.objects.all()

    def resolve_all_main_courses(self, info, **kwargs):
        return MainCourse.objects.all()

    def resolve_all_courses(self, info, **kwargs):
        return Course.objects.all()

    def resolve_all_course_uploads(self, info, **kwargs):
        return CourseUpload.objects.all()

    def resolve_all_course_modules(self, info, **kwargs):
        return CourseModule.objects.all()

    def resolve_all_course_module_details(self, info, **kwargs):
        return CourseModuleDetail.objects.all()

    def resolve_all_results(self, info, **kwargs):
        return Result.objects.all()

    def resolve_all_publishes(self, info, **kwargs):
        return Publish.objects.all()

    def resolve_all_sys_categories(self, info, **kwargs):
        return SysCategory.objects.all()

    def resolve_all_sys_constants(self, info, **kwargs):
        return SysConstant.objects.all()
    
    
    school_identifications_count = graphene.Int()
    school_infos_count = graphene.Int()
    domains_count = graphene.Int()
    fields_count = graphene.Int()
    main_specialties_count = graphene.Int()
    specialties_count = graphene.Int()
    main_courses_count = graphene.Int()
    courses_count = graphene.Int()
    results_count = graphene.Int()
    publishes_count = graphene.Int()
    course_uploads_count = graphene.Int()
    course_modules_count = graphene.Int()
    course_module_details_count = graphene.Int()
    sys_categories_count = graphene.Int()
    sys_constants_count = graphene.Int()

    # Resolvers for the count fields
    def resolve_school_identifications_count(self, info):
        return SchoolIdentificationHigher.objects.count()

    def resolve_school_infos_count(self, info):
        return SchoolInfoHigher.objects.count()

    def resolve_domains_count(self, info):
        return Domain.objects.count()

    def resolve_fields_count(self, info):
        return Field.objects.count()

    def resolve_main_specialties_count(self, info):
        return MainSpecialty.objects.count()

    def resolve_specialties_count(self, info):
        return Specialty.objects.count()

    def resolve_main_courses_count(self, info):
        return MainCourse.objects.count()

    def resolve_courses_count(self, info):
        return Course.objects.count()

    def resolve_results_count(self, info):
        return Result.objects.count()

    def resolve_publishes_count(self, info):
        return Publish.objects.count()

    def resolve_course_uploads_count(self, info):
        return CourseUpload.objects.count()

    def resolve_course_modules_count(self, info):
        return CourseModule.objects.count()

    def resolve_course_module_details_count(self, info):
        return CourseModuleDetail.objects.count()

    def resolve_sys_categories_count(self, info):
        return SysCategory.objects.count()

    def resolve_sys_constants_count(self, info):
        return SysConstant.objects.count()


schema = graphene.Schema(query=Query)
