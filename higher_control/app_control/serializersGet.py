from rest_framework import serializers
from .models import *
from tenant.serializers import *
from tenant.views import *


class GetSchoolIdentificationSerializer(SchoolIdentificationSerializer):
    logo = serializers.ImageField(read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)  

    class Meta:
        model = SchoolIdentification 
        fields = ( "__all__")



class GetSchoolInfoSerializer(DynamicFieldsModelSerializer):
    school_identification_id = serializers.IntegerField(source="school_identification.id", read_only=True)
    director = serializers.CharField(source="school_identification.director", read_only=True)
    logo = serializers.ImageField(source="school_identification.logo", read_only=True)
    school_name = serializers.CharField(read_only=True)
    short_name = serializers.CharField(read_only=True)
    main_school = serializers.BooleanField(read_only=True)
    address = serializers.CharField(read_only=True)
    town = serializers.CharField(read_only=True)
    region = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    po_box = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    niu = serializers.CharField(read_only=True)
    ca_limit = serializers.IntegerField(read_only=True)
    exam_limit = serializers.IntegerField(read_only=True)
    resit_limit = serializers.IntegerField(read_only=True)
    telephone = serializers.CharField(source="school_identification.telephone", read_only=True)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=7, read_only=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=7, read_only=True)
    website = serializers.CharField(read_only=True)
    bg_logo_transcript = serializers.CharField(read_only=True)
    bg_logo_slip = serializers.CharField(read_only=True)
    colors = serializers.CharField(read_only=True)
    version = serializers.CharField(source="school_identification.version", read_only=True)
    platform_charges = serializers.CharField(source="school_identification.platform_charges", read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    logo_url = serializers.SerializerMethodField()
    bg_logo_transcript_url = serializers.SerializerMethodField()
    bg_logo_slip_url = serializers.SerializerMethodField()
    
    def get_logo_url(self, obj):
        return obj.school_identification.logo.url if obj.school_identification.logo else None

    def get_bg_logo_transcript_url(self, obj):
        return obj.bg_logo_transcript.url if obj.bg_logo_transcript else None

    def get_bg_logo_slip_url(self, obj):
        return obj.bg_logo_slip.url if obj.bg_logo_slip else None
    
    class Meta:
        model = SchoolInfoHigher  # Replace with your actual model name
        fields = [
            'id',
            'school_identification_id', 'director', 'logo', 'school_name', 'main_school', 'address', 'town', 'region', 'country', 'po_box', 'email', 'niu', 'ca_limit', 'exam_limit', 'resit_limit', 'telephone', 'latitude', 'longitude', 'website', 'bg_logo_transcript', 'bg_logo_slip', 'colors', 'version',
            'platform_charges',
            'school_name',
            'short_name',
            'school_type',
            'main_school',
            'address',
            'campus',
            'town', 'region', 'country',
            'po_box', 'email', 'niu',
            'ca_limit', 'exam_limit', 'resit_limit',
            'telephone',
            'latitude',
            'longitude',
            'website',
            'created_by_full_name',
            'updated_by_full_name',
            'logo_url', 'bg_logo_transcript_url', 'bg_logo_slip_url',
            'colors',
        ]


class GetSchoolSettingSerializer(DynamicFieldsModelSerializer):
    school_identification = SchoolIdentificationSerializer(read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    logo_url = serializers.SerializerMethodField()
    bg_logo_transcript_url = serializers.SerializerMethodField()
    bg_logo_slip_url = serializers.SerializerMethodField()
    
    def get_logo_url(self, obj):
        return obj.school_identification.logo.url if obj.school_identification.logo else None

    def get_bg_logo_transcript_url(self, obj):
        return obj.bg_logo_transcript.url if obj.bg_logo_transcript else None

    def get_bg_logo_slip_url(self, obj):
        return obj.bg_logo_slip.url if obj.bg_logo_slip else None
    
    class Meta:
        model = SchoolInfoHigher  # Replace with your actual model name
        fields = "__all__"



class GetDomainSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_name = serializers.CharField(read_only=True)

    class Meta:
        model = Domain  # Updated to match your model
        fields = [
            'id', 
            'domain_name'
        ]



class GetFieldSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    field_name = serializers.CharField(read_only=True)
    domain_id = serializers.IntegerField(source='domain.id', read_only=True)
    domain_name = serializers.CharField(source='domain.domain_name', read_only=True)
    
    class Meta:
        model = Field  # Updated to match your model
        fields = [
            'id', 
            'field_name', 
            'domain_id', 
            "domain_name"
        ]



class GetMainSpecialtySerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="field.id", read_only=True)
    field_name = serializers.CharField(source="field.field_name", read_only=True)

    class Meta:
        model = MainSpecialty  # Updated to match your model
        fields = [
            'id', 
            'domain_id',
            'domain_name',
            'field_id',
            'field_name',

            'specialty_name', 
            'specialty_name_short',
        ]



class GetSpecialtySerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="main_specialty.field.field_name", read_only=True)
    specialty_name = serializers.CharField(source="main_specialty.specialty_name", read_only=True)
    specialty_name_short = serializers.CharField(source="main_specialty.specialty_name_short", read_only=True)
    level_id = serializers.IntegerField(source="level.id", read_only=True)
    level = serializers.IntegerField(source="level.level", read_only=True)
    school_id = serializers.IntegerField(source="school.id", read_only=True)
    campus = serializers.CharField(source="school.campus", read_only=True)
    region = serializers.CharField(source="school.region", read_only=True)
    academic_year = serializers.CharField(read_only=True)
    tuition = serializers.IntegerField(read_only=True)
    registration = serializers.IntegerField(read_only=True)
    payment_one = serializers.IntegerField(read_only=True)
    payment_two = serializers.IntegerField(read_only=True)
    payment_three = serializers.IntegerField(read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = Specialty  # Updated to match your model
        fields = [
            'id', 
            'domain_id', 
            'domain_name', 
            'field_id', 
            'field_name', 
            'specialty_name',  
            'specialty_name_short',  
            'level_id', 
            'level', 
            'school_id', 
            'campus', 
            'region', 

            'academic_year', 
            'tuition', 
            'registration', 
            'payment_one', 
            'payment_two',
            'payment_three', 
            'created_by_full_name',
            "updated_by_full_name",
        ]



class GetMainCourseSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    course_name = serializers.CharField(read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = MainCourse
        fields = [
            'id', 
            'course_name', 
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",
        ]

class GetCourseSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="specialty.main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="specialty.main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="specialty.main_specialty.field.field_name", read_only=True)
    specialty_id = serializers.IntegerField(source="specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="specialty.main_specialty.specialty_name", read_only=True)
    course_name = serializers.CharField(source="main_course.course_name", read_only=True)
    level_id = serializers.IntegerField(source="specialty.level.id", read_only=True)
    level = serializers.IntegerField(source="specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="specialty.academic_year", read_only=True)
    school_id = serializers.IntegerField(source="specialty.school.id", read_only=True)
    campus = serializers.CharField(source="specialty.school.campus", read_only=True)
    region = serializers.CharField(source="specialty.school.region", read_only=True)
    assigned_to_id = serializers.IntegerField(source='assigned_to.id', read_only=True)
    assigned_to_full_name = serializers.CharField(source='assigned_to.full_name', read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    course_code = serializers.CharField(read_only=True)
    course_type = serializers.CharField(read_only=True)
    semester = serializers.CharField(read_only=True)
    course_credit = serializers.IntegerField(read_only=True)
    completed = serializers.BooleanField(read_only=True)
    assigned = serializers.BooleanField(read_only=True)
    paid = serializers.BooleanField(read_only=True)
    hours = serializers.IntegerField(read_only=True)
    hours_left = serializers.IntegerField(read_only=True)
    date_assigned = serializers.CharField(read_only=True)
    
    class Meta:
        model = Course
        fields = [
            'id', 
            'course_code', 'course_type', 'semester','course_credit', 'completed', 'assigned', 'paid', 'hours', 'hours_left', 'date_assigned',
            'domain_id', 
            'domain_name', 
            'field_id', 
            'field_name', 
            'specialty_id', 
            'specialty_name', 
            'level_id', 
            'level', 
            'academic_year', 
            'school_id', 
            'campus', 
            'region', 
            'course_name', 
            'main_course_id', 
            'assigned_to_id', 
            'assigned_to_full_name', 
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",
        ]


class GetCourseUploadSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.IntegerField(read_only=True)
    main_course_id = serializers.IntegerField(read_only=True)
    course__main_course__course_name = serializers.CharField(read_only=True)
    course__specialty_id = serializers.IntegerField(read_only=True)
    course__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    course__specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    course__specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    course__specialty__school__region = serializers.CharField(read_only=True)
    course__specialty__school__campus = serializers.CharField(read_only=True)
    course__course_code = serializers.CharField(read_only=True)
    course__course_type = serializers.CharField(read_only=True)
    course__semester = serializers.CharField(read_only=True)
    course__course_credit = serializers.CharField(read_only=True)
    course__completed = serializers.CharField(read_only=True)
    course__assigned = serializers.BooleanField(read_only=True)
    course__paid = serializers.CharField(read_only=True)
    course__assigned_to__id = serializers.CharField(read_only=True)
    course__assigned_to__full_name = serializers.CharField(read_only=True)
    course__hours = serializers.IntegerField(read_only=True)
    course__hours_left = serializers.IntegerField(read_only=True)
    course__date_assigned = serializers.CharField(read_only=True)
    course__created_by__id = serializers.CharField(read_only=True)
    course__created_by__full_name = serializers.CharField(read_only=True)
    course__main_course__course_name = serializers.CharField(read_only=True)
    course__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    course__specialty__academic_year = serializers.CharField(read_only=True)
    course__specialty__level__level = serializers.IntegerField(read_only=True)
    course__specialty__id = serializers.IntegerField(read_only=True)

    class Meta:
        models = CourseUpload


class GetCourseModuleSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    module_title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)
    course__main_course__id = serializers.IntegerField(read_only=True)
    course__main_course__course_name = serializers.CharField(read_only=True)
    course__specialty__id = serializers.IntegerField(read_only=True)
    course__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    course__specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    course__specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    course__specialty__school__region = serializers.CharField(read_only=True)
    course__specialty__school__campus = serializers.CharField(read_only=True)
    course__course_code = serializers.CharField(read_only=True)
    course__course_type = serializers.CharField(read_only=True)
    course__semester = serializers.CharField(read_only=True)
    course__course_credit = serializers.CharField(read_only=True)
    course__completed = serializers.CharField(read_only=True)
    course__assigned = serializers.BooleanField(read_only=True)
    course__paid = serializers.CharField(read_only=True)
    course__assigned_to__id = serializers.CharField(read_only=True)
    course__assigned_to__full_name = serializers.CharField(read_only=True)
    course__hours = serializers.IntegerField(read_only=True)
    course__hours_left = serializers.IntegerField(read_only=True)
    course__date_assigned = serializers.CharField(read_only=True)
    course__created_by__id = serializers.CharField(read_only=True)
    course__created_by__full_name = serializers.CharField(read_only=True)
    course__main_course__course_name = serializers.CharField(read_only=True)
    course__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    course__specialty__academic_year = serializers.CharField(read_only=True)
    course__specialty__level__level = serializers.IntegerField(read_only=True)
    course__specialty__id = serializers.IntegerField(read_only=True)



class GetCourseModuleDetailSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    detail_title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)
    course_module__course__main_course__id = serializers.IntegerField(read_only=True)
    course_module__course__main_course__course_name = serializers.CharField(read_only=True)
    course_module__course__specialty__id = serializers.IntegerField(read_only=True)
    course_module__course__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    course_module__course__specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    course_module__course__specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    course_module__course__specialty__school__region = serializers.CharField(read_only=True)
    course_module__course__specialty__school__campus = serializers.CharField(read_only=True)
    course_module__course__course_code = serializers.CharField(read_only=True)
    course_module__course__course_type = serializers.CharField(read_only=True)
    course_module__course__semester = serializers.CharField(read_only=True)
    course_module__course__course_credit = serializers.CharField(read_only=True)
    course_module__course__completed = serializers.CharField(read_only=True)
    course_module__course__assigned = serializers.BooleanField(read_only=True)
    course_module__course__paid = serializers.CharField(read_only=True)
    course_module__course__assigned_to__id = serializers.CharField(read_only=True)
    course_module__course__assigned_to__full_name = serializers.CharField(read_only=True)
    course_module__course__hours = serializers.IntegerField(read_only=True)
    course_module__course__hours_left = serializers.IntegerField(read_only=True)
    course_module__course__date_assigned = serializers.CharField(read_only=True)
    course__created_by__id = serializers.CharField(read_only=True)
    course_module__course__created_by__full_name = serializers.CharField(read_only=True)
    course_module__course__main_course__course_name = serializers.CharField(read_only=True)
    course_module__course__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    course_module__course__specialty__academic_year = serializers.CharField(read_only=True)
    course_module__course__specialty__level__level = serializers.IntegerField(read_only=True)
    course_module__course__specialty__id = serializers.IntegerField(read_only=True)


class GetResultSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(source="student.user.id", read_only=True)
    domain_id = serializers.IntegerField(source="course.specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="course.specialty.main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="course.specialty.main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="course.specialty.main_specialty.field.field_name", read_only=True)
    specialty_id = serializers.IntegerField(source="course.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="course.specialty.main_specialty.specialty_name", read_only=True)
    level_id = serializers.IntegerField(source="course.specialty.level.id", read_only=True)
    level = serializers.IntegerField(source="course.specialty.level.level", read_only=True)
    course_id = serializers.IntegerField(source="course.id", read_only=True)
    course_name = serializers.CharField(source="course.main_course.course_name", read_only=True)
    academic_year = serializers.CharField(source="course.specialty.academic_year", read_only=True)
    school_id = serializers.IntegerField(source="course.specialty.school.id", read_only=True)
    campus = serializers.CharField(source="course.specialty.school.campus", read_only=True)
    region = serializers.CharField(source="course.specialty.school.region", read_only=True)
    course_code = serializers.CharField(source='course.course_code', read_only=True)
    semester= serializers.CharField(source='course.semester', read_only=True)
    course_credit= serializers.IntegerField(source='course.course_credit', read_only=True)
    course_type= serializers.CharField(source='course.course_type', read_only=True)
    user_id = serializers.IntegerField(source='student.user.id', read_only=True)
    student_id = serializers.IntegerField(source='student.id', read_only=True)
    first_name = serializers.CharField(source='student.user.first_name', read_only=True)
    full_name = serializers.CharField(source='student.user.full_name', read_only=True)
    assigned_to_id = serializers.IntegerField(source='course.assigned_to.id', read_only=True)
    assigned_to_full_name = serializers.CharField(source='course.assigned_to.full_name', read_only=True)

    ca = serializers.IntegerField(read_only=True)
    exam = serializers.IntegerField(read_only=True)
    resit = serializers.IntegerField(read_only=True)
    average = serializers.IntegerField(read_only=True)

    validated = serializers.BooleanField(read_only=True)
    publish_ca = serializers.BooleanField(read_only=True)
    publish_exam = serializers.BooleanField(read_only=True)
    publish_resit = serializers.BooleanField(read_only=True)
    closed = serializers.BooleanField(read_only=True)
    active = serializers.BooleanField(read_only=True)

    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = Result
        fields = [
            'id', 'user_id',
            'domain_id', 'domain_name', 'field_id', 'field_name', 'specialty_id', 'specialty_name', 'level_id', 'level', 'course_id', 'course_name', 'academic_year', 
            'school_id', 'campus', 'region',
            'course_code', 'semester', 'course_credit', 'course_type', 'user_id', 'student_id', 'first_name', 'full_name', 'assigned_to_id', 'assigned_to_full_name', 
            'ca',
            'exam', 
            'resit', 
            'average', 
            'validated', 
            'publish_ca', 'publish_exam', 'publish_resit', 'closed', 'active', 
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",
        ]
                    


class GetPublishSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="specialty.main_specialty.field.domain.domain_name", read_only=True)
    specialty_id = serializers.IntegerField(source="specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="specialty.main_specialty.specialty_name", read_only=True)
    school_id = serializers.IntegerField(source="specialty.school.id", read_only=True)
    campus = serializers.CharField(source="specialty.school.campus", read_only=True)
    region = serializers.CharField(source="specialty.school.region", read_only=True)
    level = serializers.IntegerField(source="specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="specialty.academic_year", read_only=True)

    semester = serializers.CharField(read_only=True)
    ca = serializers.BooleanField(read_only=True)
    exam = serializers.BooleanField(read_only=True)
    resit = serializers.BooleanField(read_only=True)
    portal_ca = serializers.BooleanField(read_only=True)
    portal_exam = serializers.BooleanField(read_only=True)
    portal_resit = serializers.BooleanField(read_only=True)

    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
                       
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


class GetLevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    level = serializers.IntegerField(read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    

    class Meta:
        model = Level  # Replace with your actual model name
        fields = [
            'id',
            'level',
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",
        ] 

class GetSysCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
                    

class GetSysConstantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    sys_category__id = serializers.IntegerField(read_only=True)
    sys_category__name = serializers.CharField(read_only=True)
    
    