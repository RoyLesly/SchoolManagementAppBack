from rest_framework import serializers
from .models import *
from tenant.views import DynamicFieldsModelSerializer


class GetActivationKeySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)    
    name = serializers.CharField(read_only=True)
    account_name = serializers.CharField(read_only=True)
  
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetSchoolFeesSerializer(DynamicFieldsModelSerializer):

    id = serializers.IntegerField(read_only=True)
    school_identification_id = serializers.IntegerField(source="userprofile.specialty.school.school_identification.id", read_only=True)
    school_identification_code = serializers.CharField(source="userprofile.specialty.school.school_identification.code", read_only=True)
    version = serializers.CharField(source="userprofile.specialty.school.school_identification.version", read_only=True)
    director = serializers.CharField(source="userprofile.specialty.school.school_identification.director", read_only=True)
    platform_charges = serializers.IntegerField(source="userprofile.specialty.school.school_identification.platform_charges", read_only=True)
    name = serializers.CharField(source="userprofile.specialty.school.school_identification.name", read_only=True)
    support_number_one = serializers.CharField(source="userprofile.specialty.school.school_identification.support_number_one", read_only=True)
    support_number_two = serializers.CharField(source="userprofile.specialty.school.school_identification.support_number_two", read_only=True)
    status = serializers.BooleanField(source="userprofile.specialty.school.school_identification.status", read_only=True)
    back_end = serializers.CharField(source="userprofile.specialty.school.school_identification.back_end", read_only=True)
    front_end = serializers.CharField(source="userprofile.specialty.school.school_identification.front_end", read_only=True)
    
    campus = serializers.CharField(source="userprofile.specialty.school.campus", read_only=True)
    ca_limit = serializers.IntegerField(source="userprofile.specialty.school.ca_limit", read_only=True)
    exam_limit = serializers.IntegerField(source="userprofile.specialty.school.exam_limit", read_only=True)
    resit_limit = serializers.IntegerField(source="userprofile.specialty.school.resit_limit", read_only=True)
    bg_logo_transcript = serializers.CharField(source="userprofile.specialty.school.bg_logo_transcript", read_only=True)
    bg_logo_slip = serializers.CharField(source="userprofile.specialty.school.bg_logo_slip", read_only=True)
    colors = serializers.CharField(source="userprofile.specialty.school.colors", read_only=True)
    prefix = serializers.CharField(source="userprofile.specialty.school.prefix", read_only=True)
    method = serializers.IntegerField(source="userprofile.specialty.school.method", read_only=True)
    school_type = serializers.CharField(source="userprofile.specialty.school.school_type", read_only=True)
    school_name = serializers.CharField(source="userprofile.specialty.school.school_name", read_only=True)
    short_name = serializers.CharField(source="userprofile.specialty.school.short_name", read_only=True)
    school_address = serializers.CharField(source="userprofile.specialty.school.region", read_only=True)
    town = serializers.CharField(source="userprofile.specialty.school.town", read_only=True)
    region = serializers.CharField(source="userprofile.specialty.school.region", read_only=True)
    country = serializers.CharField(source="userprofile.specialty.school.country", read_only=True)
    po_box = serializers.CharField(source="userprofile.specialty.school.po_box", read_only=True)
    niu = serializers.CharField(source="userprofile.specialty.school.niu", read_only=True)
    latitude = serializers.DecimalField(source="userprofile.specialty.school.latitude", max_digits=9, decimal_places=7, read_only=True)
    longitude = serializers.DecimalField(source="userprofile.specialty.school.longitude", max_digits=9, decimal_places=7, read_only=True)
    radius = serializers.IntegerField(source="userprofile.specialty.school.radius", read_only=True)
    school_id = serializers.IntegerField(source="userprofile.specialty.school.id", read_only=True)
    school_email = serializers.CharField(source="userprofile.specialty.school.email", read_only=True)
    school_telephone = serializers.CharField(source="userprofile.specialty.school.email", read_only=True)
    website = serializers.CharField(source="userprofile.specialty.school.website", read_only=True)
    campus = serializers.CharField(source="userprofile.specialty.school.campus", read_only=True)

    schoolfees_control = serializers.CharField(source="userprofile.specialty.school.schoolfees_control", read_only=True)
    registration_seperate_tuition = serializers.BooleanField(source="userprofile.specialty.school.registration_seperate_tuition", read_only=True)

    user_id = serializers.IntegerField(source="userprofile.user.id", read_only=True)
    userprofile_id = serializers.IntegerField(source="userprofile.id", read_only=True)
    full_name = serializers.CharField(source="userprofile.user.full_name", read_only=True)
    matricle = serializers.CharField(source="userprofile.user.matricle", read_only=True)
    username = serializers.CharField(source="userprofile.user.username", read_only=True)
    role = serializers.CharField(source="userprofile.user.role", read_only=True)
    dob = serializers.CharField(source="userprofile.user.dob", read_only=True)
    pob = serializers.CharField(source="userprofile.user.pob", read_only=True)
    telephone = serializers.CharField(source="userprofile.user.telephone", read_only=True)
    email = serializers.CharField(source="userprofile.user.email", read_only=True)
    address = serializers.CharField(source="userprofile.user.address", read_only=True)
    domain_id = serializers.IntegerField(source="userprofile.specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="userprofile.specialty.main_specialty.field.domain.domain_name", read_only=True)
    field_id = serializers.IntegerField(source="userprofile.specialty.main_specialty.field.id", read_only=True)
    field_name = serializers.CharField(source="userprofile.specialty.main_specialty.field.field_name", read_only=True)
    specialty_id = serializers.IntegerField(source="userprofile.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="userprofile.specialty.main_specialty.specialty_name", read_only=True)
    level_id = serializers.IntegerField(source="userprofile.specialty.level.id", read_only=True)
    level = serializers.IntegerField(source="userprofile.specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="userprofile.specialty.academic_year", read_only=True)
    tuition = serializers.IntegerField(source="userprofile.specialty.tuition", read_only=True)
    payment_one = serializers.IntegerField(source="userprofile.specialty.payment_one", read_only=True)
    payment_two = serializers.IntegerField(source="userprofile.specialty.payment_two", read_only=True)
    payment_three = serializers.IntegerField(source="userprofile.specialty.payment_three", read_only=True)
    school_logo = serializers.CharField(source="userprofile.specialty.school.logo", read_only=True)
    code = serializers.CharField(source="userprofile.code", read_only=True)

    platform_paid = serializers.BooleanField(read_only=True)
    balance = serializers.IntegerField(read_only=True)
    
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    created_by_id = serializers.IntegerField(source="created_by.id", read_only=True)
    created_by_full_name = serializers.CharField(source="created_by.full_name", read_only=True)
    updated_by_id = serializers.IntegerField(source="created_by.id", read_only=True)
    updated_by_full_name = serializers.CharField(source="created_by.full_name", read_only=True)

    class Meta:
        model = SchoolFees  # Replace with your actual model name
        fields = [
            'id',
            'school_identification_id', 'school_identification_code', 'version', 'director', 'platform_charges', 'name', 'support_number_one', 'support_number_two', 'status', 'back_end', 'front_end',
            'campus', 'ca_limit', 'exam_limit', 'resit_limit', 'bg_logo_transcript', 'bg_logo_slip', 'colors', 'prefix', 'method', 'school_type', 'school_name', 'short_name', 'school_address', 'town', 'region', 'country', 'po_box', 'niu', 'latitude', 'longitude', 'radius',
            'school_id', 'school_email', 'school_telephone', 'website', 'campus', 'schoolfees_control', 'registration_seperate_tuition',
 
            'user_id', 'userprofile_id', 'full_name', 'matricle', 'username', 'role', 'dob', 'pob', 'telephone', 'email', 'address',
            'domain_id', 'domain_name', 'field_id', 'field_name', 'specialty_id', 'specialty_name', 'level_id', 'level', 'academic_year', 'tuition',
            'payment_one', 'payment_two', 'payment_three',
            'school_logo', 'code',
            'platform_paid', 'balance',
            'created_at',
            'updated_at',
            'created_by_id',
            'updated_by_id',
            'created_by_full_name',
            'updated_by_full_name',
        ]


class GetTransactionsSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)    
    schoolfees_id = serializers.IntegerField(source="schoolfees.id", read_only=True)
    user_id = serializers.IntegerField(source="schoolfees.userprofile.user.id", read_only=True)  # Fixed user_id source
    userprofile_id = serializers.IntegerField(source="schoolfees.userprofile.id", read_only=True)
    full_name = serializers.CharField(source="schoolfees.userprofile.user.full_name", read_only=True)
    matricle = serializers.CharField(source="schoolfees.userprofile.user.matricle", read_only=True)
    specialty_id = serializers.IntegerField(source="schoolfees.userprofile.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="schoolfees.userprofile.specialty.main_specialty.specialty_name", read_only=True)
    level = serializers.IntegerField(source="schoolfees.userprofile.specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="schoolfees.userprofile.specialty.academic_year", read_only=True)
    domain_id = serializers.IntegerField(source="schoolfees.userprofile.specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="schoolfees.userprofile.specialty.main_specialty.field.domain.domain_name", read_only=True)
    school_id = serializers.IntegerField(source="schoolfees.userprofile.specialty.school.id", read_only=True)
    campus = serializers.CharField(source="schoolfees.userprofile.specialty.school.campus", read_only=True)

    payer_name = serializers.CharField(read_only=True)
    telephone = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    payment_method = serializers.CharField(read_only=True)
    account = serializers.CharField(read_only=True)    
    reason = serializers.CharField(read_only=True)
    ref = serializers.CharField(read_only=True)
    operation_type = serializers.CharField(read_only=True)
    origin = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)

    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    
    created_by_id = serializers.IntegerField(source="created_by.id", read_only=True)
    created_by_full_name = serializers.CharField(source="created_by.full_name", read_only=True)
    
    updated_by_id = serializers.IntegerField(source="updated_by.id", read_only=True)  # Fixed updated_by_id source
    updated_by_full_name = serializers.CharField(source="updated_by.full_name", read_only=True)  # Fixed updated_by_full_name source

    class Meta:
        model = Transactions  # Replace with your actual model name
        fields = [
            'id',
            'schoolfees_id',
            'user_id',
            'userprofile_id',
            'full_name',
            'matricle',
            'specialty_id',
            'specialty_name',
            'level',
            'academic_year',
            'domain_id',
            'domain_name',
            'school_id',
            'campus',
            'payer_name', 
            'telephone', 
            'status', 
            'payment_method', 
            'account', 
            'reason', 
            'ref', 
            'operation_type', 
            'origin', 
            'amount',
            'created_at',
            'updated_at',
            'created_by_id',
            'updated_by_id',
            'created_by_full_name',
            'updated_by_full_name',
        ]


class GetAccountSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    number = serializers.CharField(read_only=True)
    year = serializers.CharField(read_only=True)
    balance = serializers.IntegerField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    created_at = serializers.CharField(read_only=True)


class GetTranscriptApplicationSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(source="userprofile.user.id", read_only=True)
    userprofile_id = serializers.IntegerField(source="userprofile.id", read_only=True)
    full_name = serializers.CharField(source="userprofile.user.full_name", read_only=True)
    matricle = serializers.CharField(source="userprofile.user.matricle", read_only=True)
    specialty_id = serializers.IntegerField(source="userprofile.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="userprofile.specialty.main_specialty.specialty_name", read_only=True)
    level = serializers.IntegerField(source="userprofile.specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="userprofile.specialty.academic_year", read_only=True)
    approved_by_id = serializers.CharField(source="approved_by.id", read_only=True)
    approved_by_full_name = serializers.CharField(source="approved_by.full_name", read_only=True)
   
    status = serializers.CharField(read_only=True)
    approved_at = serializers.CharField(read_only=True)
    print_count = serializers.IntegerField(read_only=True)
    printed_at = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    printed_by_id = serializers.IntegerField(source='printed_by.id', read_only=True)
    printed_by_full_name = serializers.CharField(source='printed_by.full_name', read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = SchoolFees  # Replace with your actual model name
        fields = [
            'id',
            'user_id',
            'userprofile_id',
            'full_name',
            'matricle',
            'specialty_id',
            'specialty_name',
            'level',
            'academic_year',
            'approved_by_id',
            'approved_by_full_name',
            'status',
            'approved_at',
            'print_count',
            'printed_by_id',
            'printed_by_full_name',
            'printed_at',
            'created_at',
            'updated_at',
            'created_by_id',
            'updated_by_id',
            'created_by_full_name',
            'updated_by_full_name',
        ]

