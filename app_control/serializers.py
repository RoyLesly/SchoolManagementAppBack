from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import (Domain, MainSpecialty, Specialty, MainCourse, Course, Result, Level)
from user_control.serializers import CustomUserSerializer
from user_control.models import UserProfile


class AssignPermissionsToGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Permission.objects.all(), required=True)

    class Meta:
        model = Group
        fields = ("__all__")


class DomainSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Domain
        fields = "__all__"
        dept = 1


class MainSpecialtySerializer(serializers.ModelSerializer):
    domain = DomainSerializer(read_only=True)
    domain_id = serializers.CharField(write_only=True, required=True)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MainSpecialty
        fields = "__all__"
        dept = 1


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = "__all__"
        dept = 1


class SpecialtySerializer(serializers.ModelSerializer):
    main_specialty = MainSpecialtySerializer(read_only=True)
    main_specialty_id = serializers.CharField(write_only=True, required=True)
    level = LevelSerializer(read_only=True)
    level_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Specialty
        fields = "__all__"
        dept = 1


class MainCourseSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MainCourse
        fields = "__all__"
        dept = 1


class CourseSerializer(serializers.ModelSerializer):
    main_course = MainCourseSerializer(read_only=True)
    main_course_id = serializers.CharField(write_only=True, required=True)
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=True)
    assigned_to = CustomUserSerializer(read_only=True)
    assigned_to_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Course
        fields = "__all__"
        dept = 1


class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True, required=True)
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = "__all__"
        dept = 1


class ResultSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.CharField(write_only=True, required=True)
    student = UserProfileSerializer(read_only=True)
    student_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Result
        fields = "__all__"
        dept = 1


