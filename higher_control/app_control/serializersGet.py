from rest_framework import serializers
from .models import *
from tenant.serializers import *


class GetSchoolIdentificationSerializer(SchoolIdentificationSerializer):
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)  

    class Meta:
        model = SchoolIdentification 
        fields = ( "__all__")



class GetSchoolInfoSerializer(serializers.ModelSerializer):
    school_identification_id = serializers.IntegerField(source="school_identification.id", read_only=True)
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
            'school_identification_id',
            'version',
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



class GetDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain  # Updated to match your model
        fields = [
            'id', 
            'domain_name'
        ]



class GetFieldSerializer(serializers.ModelSerializer):
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



class GetMainSpecialtySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="field.domain.domain_name", read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    field_id = serializers.IntegerField(source="field.id", read_only=True)
    field_name = serializers.CharField(source="field.field_name", read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = MainSpecialty  # Updated to match your model
        fields = [
            'id', 
            'domain_id',
            'domain_name',
            'field_id',
            'field_name',
            'created_by_full_name',
            'updated_by_full_name',

            'specialty_name', 
            'specialty_name_short',
        ]



class GetSpecialtySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    main_specialty = GetMainSpecialtySerializer(read_only=True)

    domain_id = serializers.IntegerField(source="main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="main_specialty.field.field_name", read_only=True)
    main_specialty_id = serializers.IntegerField(source="main_specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="main_specialty.specialty_name", read_only=True)
    specialty_name_short = serializers.CharField(source="main_specialty.specialty_name_short", read_only=True)
    level_id = serializers.IntegerField(source="level.id", read_only=True)
    level_level = serializers.IntegerField(source="level.level", read_only=True)
    school_id = serializers.IntegerField(source="school.id", read_only=True)
    school_campus = serializers.CharField(source="school.campus", read_only=True)
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
            'main_specialty',  
            'main_specialty_id',  
            'specialty_name',  
            'specialty_name_short',  
            'level_id', 
            'level_level', 
            'school_id', 
            'school_campus', 

            'academic_year', 
            'tuition', 
            'registration', 
            'payment_one', 
            'payment_two',
            'payment_three', 
            'created_by_full_name',
            "updated_by_full_name",
        ]



class GetMainCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)



class GetCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="specialty.main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="specialty.main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="specialty.main_specialty.field.field_name", read_only=True)
    specialty_id = serializers.IntegerField(source="specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="specialty.main_specialty.specialty_name", read_only=True)
    course_name = serializers.CharField(source="main_course.course_name", read_only=True)
    level_id = serializers.IntegerField(source="specialty.level.id", read_only=True)
    level_level = serializers.IntegerField(source="specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="specialty.academic_year", read_only=True)
    school_id = serializers.IntegerField(source="specialty.school.id", read_only=True)
    school_campus = serializers.CharField(source="specialty.school.campus", read_only=True)
    school_region = serializers.CharField(source="specialty.school.region", read_only=True)
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
    


class GetCourseUploadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.IntegerField(read_only=True)
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



class GetCourseModuleSerializer(serializers.Serializer):
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



class GetCourseModuleDetailSerializer(serializers.Serializer):
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


class GetResultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="course.specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="course.specialty.main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="course.specialty.main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="course.specialty.main_specialty.field.field_name", read_only=True)
    specialty_id = serializers.IntegerField(source="course.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="course.specialty.main_specialty.specialty_name", read_only=True)
    course_name = serializers.CharField(source="course.main_course.course_name", read_only=True)
    level_id = serializers.IntegerField(source="course.specialty.level.id", read_only=True)
    level = serializers.IntegerField(source="course.specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="course.specialty.academic_year", read_only=True)
    school_id = serializers.IntegerField(source="course.specialty.school.id", read_only=True)
    school_campus = serializers.CharField(source="course.specialty.school.campus", read_only=True)
    school_region = serializers.CharField(source="course.specialty.school.region", read_only=True)
    assigned_to_id = serializers.IntegerField(source='course.assigned_to.id', read_only=True)
    assigned_to_full_name = serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    course_code = serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    course_semester= serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    course_credit= serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    course_type= serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    assigned_to_full_name = serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    student_id = serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    student_first_name = serializers.CharField(source='course.assigned_to.full_name', read_only=True)
    student_full_name = serializers.CharField(source='course.assigned_to.full_name', read_only=True)

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
    
                    


class GetPublishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    specialty_id = serializers.IntegerField(source="specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="specialty.main_specialty.specialty_name", read_only=True)
    school_id = serializers.IntegerField(source="specialty.school.id", read_only=True)
    school_campus = serializers.CharField(source="specialty.school.campus", read_only=True)
    school_region = serializers.CharField(source="specialty.school.region", read_only=True)
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
                       



class GetLevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    level = serializers.CharField(read_only=True)
                    

class GetSysCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
                    

class GetSysConstantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    sys_category__id = serializers.IntegerField(read_only=True)
    sys_category__name = serializers.CharField(read_only=True)
    
    