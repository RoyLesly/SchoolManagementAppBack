from rest_framework import serializers
from higher_control.user_control.models import *
from higher_control.app_control.models import SchoolInfoHigher
from tenant.views import *



class GetDepartmentSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    created_by_id = serializers.IntegerField(read_only=True)
    created_by_full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Department  # Replace with your actual model name
        fields = [
            'id',
            'name',
            'created_by_id',
            'created_by_full_name',
        ]

class GetPageSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    created_by_id = serializers.IntegerField(read_only=True)
    created_by_full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Page  # Replace with your actual model name
        fields = [
            'id',
            'name',
            'created_by_id',
            'created_by_full_name',
        ]

class GetDepartmentSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = Program  # Replace with your actual model name
        fields = [
            'id',
            'name',
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",
        ]



class GetProgramSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
    
    class Meta:
        model = Program  # Replace with your actual model name
        fields = [
            'id',
            'name',
            'description',
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",
        ]


class GetUserProfileSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    photo = serializers.ImageField(source="user.photo", read_only=True)
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    full_name = serializers.CharField(source="user.full_name", read_only=True)
    matricle = serializers.CharField(source="user.matricle", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    sex = serializers.CharField(source="user.sex", read_only=True)
    dob = serializers.DateField(source="user.dob", read_only=True)  # Correctly using DateField for dob
    pob = serializers.CharField(source="user.pob", read_only=True)
    address = serializers.CharField(source="user.address", read_only=True)
    telephone = serializers.CharField(source="user.telephone", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)  # Correctly using EmailField for email
    parent = serializers.CharField(source="user.parent", read_only=True)
    parent_telephone = serializers.CharField(source="user.parent_telephone", read_only=True)
    specialty_id = serializers.IntegerField(source="specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="specialty.main_specialty.specialty_name", read_only=True)
    domain_id = serializers.IntegerField(source="specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="specialty.main_specialty.field.domain.domain_name", read_only=True)
    academic_year = serializers.CharField(source="specialty.academic_year", read_only=True)
    tuition = serializers.CharField(source="specialty.tuition", read_only=True)
    level = serializers.IntegerField(source="specialty.level.level", read_only=True)
    field_name = serializers.CharField(source="specialty.main_specialty.field.field_name", read_only=True)
    campus = serializers.CharField(source="specialty.school.campus", read_only=True)
    region = serializers.CharField(source="specialty.school.region", read_only=True)
    school_name = serializers.CharField(source="specialty.school.school_name", read_only=True)
    school_id = serializers.IntegerField(source="specialty.school.id", read_only=True)
    version = serializers.CharField(source="specialty.school.school_identification.version", read_only=True)
    program_id = serializers.IntegerField(source="program.id", read_only=True)
    program_name = serializers.CharField(source="program.name", read_only=True)
    active = serializers.CharField(read_only=True)
    session = serializers.CharField(read_only=True)
    code = serializers.ImageField(read_only=True)
    created_by_full_name = serializers.CharField(source="created_by.full_name", read_only=True)
    updated_by_full_name = serializers.CharField(source="updated_by.full_name", read_only=True)
    created_at = serializers.DateField(read_only=True)  # Ensure datetime format for created_at
    updated_at = serializers.DateField(read_only=True)  # Ensure datetime format for updated_at

    class Meta:
        model = UserProfile  # Replace with your actual model name
        fields = [
            'id',
            'photo',
            'user_id',
            'first_name',
            'last_name',
            'full_name',
            'matricle',
            'username',
            'sex',
            'dob',
            'pob',
            'address',
            'telephone',
            'email',
            'parent',
            'parent_telephone',
            'specialty_id',
            'specialty_name',
            'domain_id',
            'domain_name',
            'academic_year',
            'tuition',
            'level',
            'field_name',
            'campus',
            'region',
            'school_name',
            'school_id',
            'version',
            'program_id',
            'program_name',
            'active',
            'session',
            'code',
            'created_by_full_name',
            'updated_by_full_name',
            'created_at',
            'updated_at',
        ]


class GetAppearanceSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    matricle = serializers.CharField(read_only=True)    
    dark_mode = serializers.CharField(read_only=True)    
    lang = serializers.CharField(read_only=True)    
    created_by__full_name = serializers.CharField(read_only=True)


class GetUserActivitySerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    matricle = serializers.CharField(read_only=True)    
    action = serializers.CharField(read_only=True)    
    item = serializers.CharField(read_only=True)    
    details = serializers.CharField(read_only=True)    
    created_by__full_name = serializers.CharField(read_only=True)


class GetSchoolInfoSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    school_identification_id = serializers.IntegerField(source="school_identification.id", read_only=True)
    director = serializers.CharField(source="school_identification.director", read_only=True)
    school_name = serializers.CharField(read_only=True)
    short_name = serializers.CharField(read_only=True)
    main_school = serializers.BooleanField(read_only=True)
    address = serializers.CharField(read_only=True)
    campus = serializers.CharField(read_only=True)
    town = serializers.CharField(read_only=True)
    region = serializers.CharField(read_only=True)

    class Meta:
        model = SchoolInfoHigher  # Replace with your actual model name
        fields = [
            'id',
            'school_identification_id', 'director', 'school_name', 'short_name',
            'main_school', 'address', 'campus', 'town', 'region'
        ]


class GetCustomUserSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)
    matricle = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    sex = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    dob = serializers.DateField(read_only=True)  # Correctly using DateField for dob
    pob = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)  # Correctly using EmailField
    telephone = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)  # BooleanField for active status
    is_superuser = serializers.BooleanField(read_only=True)  # BooleanField for superuser status
    last_login = serializers.DateTimeField(read_only=True)  # DateTimeField for last login
    school_ids = serializers.PrimaryKeyRelatedField(source="school", many=True, read_only=True)  # Primary key relation for schools
    dept = GetDepartmentSerializer(many=True, read_only=True, required=False)
    page = GetPageSerializer(many=True, read_only=True)
    school = GetSchoolInfoSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser  # Your actual model
        fields = [
            'id',
            'username',
            'matricle',
            'role',
            'first_name',
            'last_name',
            'full_name',
            'sex',
            'address',
            'dob',
            'pob',
            'email',
            'telephone',
            'title',
            'is_active',
            'is_superuser',
            'last_login',
            'school_ids',
            'dept',
            'page',
            'school',
        ]



class GetPreInscriptionSerializer(DynamicFieldsModelSerializer):
    id = serializers.CharField(read_only=True)
    registration_number = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    sex = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    telephone = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    pob = serializers.CharField(read_only=True)
    dob = serializers.DateField(read_only=True, format="%Y-%m-%d")  # Format for better readability
    status = serializers.CharField(read_only=True)
    emergency_name = serializers.CharField(read_only=True)
    emergency_town = serializers.CharField(read_only=True)
    emergency_telephone = serializers.CharField(read_only=True)
    program = serializers.CharField(read_only=True)
    level = serializers.CharField(read_only=True)
    session = serializers.CharField(read_only=True)
    academic_year = serializers.CharField(read_only=True)
    specialty_one = serializers.CharField(read_only=True)
    specialty_two = serializers.CharField(read_only=True)
    specialty_three = serializers.CharField(read_only=True)
    campus = serializers.CharField(read_only=True)
    admission_status = serializers.BooleanField(read_only=True)
    action = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")  # Adds timestamp formatting
    updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = PreInscription
        fields = [
            "id",
            "registration_number",
            "first_name",
            "last_name",
            "full_name",
            "sex",
            "email",
            "telephone",
            "address",
            "pob",
            "dob",
            "status",
            "emergency_name",
            "emergency_town",
            "emergency_telephone",
            "program",
            "level",
            "session",
            "academic_year",
            "specialty_one",
            "specialty_two",
            "specialty_three",
            "campus",
            "admission_status",
            "action",
            "created_at",
            "updated_at",
        ]


