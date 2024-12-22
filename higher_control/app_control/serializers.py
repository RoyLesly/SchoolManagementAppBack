from rest_framework import serializers
from .models import *
from higher_control.user_control.serializers import CustomUserSerializer
from higher_control.user_control.models import UserProfile, Program
from tenant.serializers import validate_user_exists


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class SchoolIdentificationHigherSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolIdentificationHigher
        fields = ("__all__")
    
    # def validate(self, attrs):
    #     pass    #validate_user_exists(attrs) 


class SchoolInfoHigherSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.IntegerField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = SchoolInfoHigher
        fields = "__all__"


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    domain = DomainSerializer(read_only=True)
    domain_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Field
        fields = "__all__"

class MainSpecialtySerializer(serializers.ModelSerializer):
    field_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MainSpecialty
        fields = "__all__"
    

class SpecialtySerializer(serializers.ModelSerializer):
    school = SchoolInfoHigherSerializer(read_only=True)
    school_id = serializers.CharField(write_only=True, required=True)
    main_specialty = MainSpecialtySerializer(read_only=True)
    main_specialty_id = serializers.CharField(write_only=True, required=True)
    level = LevelSerializer(read_only=True)
    level_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Specialty
        fields = "__all__"


class MainCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainCourse
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    main_course_id = serializers.CharField(write_only=True, required=True)
    main_course = MainCourseSerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=True)
    specialty = SpecialtySerializer(read_only=True)
    assigned_to_id = serializers.CharField(write_only=True, required=False)
    assigned_to = CustomUserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        dept = 1


class CourseUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(read_only=True)
    course_id = serializers.CharField(write_only=True, required=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = CourseUpload
        fields = "__all__"
        dept = 1


class CourseModuleSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CourseModule
        fields = "__all__"
        dept = 1


class CourseModuleDetailSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CourseModuleDetail
        fields = "__all__"

class ProgramSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Program
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True, required=False)
    user_id = serializers.CharField(write_only=True, required=True)
    user = CustomUserSerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=True)
    program_id = serializers.CharField(write_only=True, required=True)
    code = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = [ 'id', 'user_id', 'user', 'specialty_id', 'program_id', 'session', 'code' ]


class ResultSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(write_only=True, required=False)
    course = CourseSerializer(read_only=True)
    student_id = serializers.CharField(write_only=True, required=False)
    student = UserProfileSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Result
        fields = "__all__"


class PublishSerializer(serializers.ModelSerializer):
    specialty_id = serializers.CharField(write_only=True, required=True)
    specialty = SpecialtySerializer(read_only=True,)
    created_by_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Publish
        fields = "__all__"


class SysCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SysCategory
        fields = "__all__"


class SysConstantSerializer(serializers.ModelSerializer):
    sys_category_id = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SysConstant
        fields = "__all__"
