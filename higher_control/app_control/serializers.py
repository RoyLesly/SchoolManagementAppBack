from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *
from higher_control.user_control.serializers import CustomUserSerializer, GetCustomUserSerializer
from higher_control.user_control.models import UserProfile, Program


def validate_user_exists(attrs):
    created_by_id = attrs.get('created_by_id')
    updated_by_id = attrs.get('updated_by_id')
    if created_by_id:
        user_id = created_by_id
    if updated_by_id:
        user_id = updated_by_id
    try:
        return CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        raise serializers.ValidationError("User with ID {} does not exist.".format(user_id))



class SchoolIdentificationHigherSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolIdentificationHigher
        fields = ("__all__")
    
    def validate(self, attrs):
        validate_user_exists(attrs)


class SchoolInfoHigherSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = SchoolInfoHigher
        fields = "__all__"
    
    def validate(self, attrs):
        validate_user_exists(attrs)


class DomainSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Domain
        fields = "__all__"
        
    def validate(self, attrs):
        validate_user_exists(attrs)


class FieldSerializer(serializers.ModelSerializer):
    domain = DomainSerializer(read_only=True)
    domain_id = serializers.CharField(write_only=True, required=True)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Field
        fields = "__all__"

    def validate(self, attrs):
        validate_user_exists(attrs)

class MainSpecialtySerializer(serializers.ModelSerializer):
    field_id = serializers.CharField(write_only=True, required=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MainSpecialty
        fields = "__all__"
        
    def validate(self, attrs):
        validate_user_exists(attrs)        


class SpecialtySerializer(serializers.ModelSerializer):
    school_id = serializers.CharField(write_only=True, required=True)
    main_specialty_id = serializers.CharField(write_only=True, required=True)
    level_id = serializers.CharField(write_only=True, required=False)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Specialty
        fields = "__all__"
        dept = 1


class MainCourseSerializer(serializers.ModelSerializer):
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MainCourse
        fields = "__all__"
        dept = 1


class CourseSerializer(serializers.ModelSerializer):
    main_course_id = serializers.CharField(write_only=True, required=True)
    specialty_id = serializers.CharField(write_only=True, required=True)
    assigned_to_id = serializers.CharField(write_only=True, required=False)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Course
        fields = "__all__"
        dept = 1


class CourseUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(read_only=True)
    course_id = serializers.CharField(write_only=True, required=True)

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
        dept = 1


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = "__all__"
        dept = 1


class ProgramSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Program
        fields = "__all__"
        dept = 1


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(write_only=True, required=True)
    specialty_id = serializers.CharField(write_only=True, required=False)
    program_id = serializers.CharField(write_only=True, required=False)
    code = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = "__all__"
        dept = 2


class ResultSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(write_only=True, required=False)
    student_id = serializers.CharField(write_only=True, required=False)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Result
        fields = "__all__"
        dept = 1


class PublishSerializer(serializers.ModelSerializer):
    specialty_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Publish
        fields = "__all__"
        dept = 1


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
