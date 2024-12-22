from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from higher_control.user_control.models import *
from datetime import datetime
import importlib
# from tenant.serializers import validate_user_exists



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        user.last_login = datetime.now()
        user.password_set = True
        user.save()
        token = super().get_token(user)
        token["username"] = user.username
        token["full_name"] = user.full_name
        token["matricle"] = user.matricle
        token["role"] = user.role
        token["is_superuser"] = user.is_superuser
        token["permissions"] = list(user.user_permissions.values_list("codename", flat=True))
        token["dept"] = list(user.dept.all().values_list("name", flat=True))
        token["page"] = list(user.page.all().values_list("name", flat=True))
        token["school"] = list(user.school.all().values_list("id", flat=True))  

        toBeDeleted = UserProfile.objects.all()
        for p in toBeDeleted:
            p.save()

        return token


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = "__all__"
        dept = 1


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer(read_only=True)

    class Meta:
        model = Permission
        fields = "__all__"
        dept = 1


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = "__all__"
        dept = 1


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(ROLE_CHOICES)




class ProgramSerializer(serializers.ModelSerializer):
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Program
        fields = "__all__"



class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    role = serializers.ChoiceField(ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        exclude = ("password",)
        # fields = "__all__"
        dept = 1


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PageSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class SchoolInfoTwoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    module_schoolinfo = importlib.import_module("higher_control.app_control").models.SchoolInfoHigher

    class Meta:
        model = importlib.import_module("higher_control.app_control").models.SchoolInfoHigher
        fields = "__all__"


# class UserProfileSerializer(serializers.ModelSerializer):
#     user = CustomUserSerializer(read_only=True)
#     user_id = serializers.CharField(write_only=True, required=True)
#     specialty_id = serializers.CharField(write_only=True, required=True)
#     specialty = importlib.import_module("higher_control.app_control").serializers.SpecialtySerializer(read_only=True)
#     program_id = serializers.CharField(write_only=True, required=True)
#     program = ProgramSerializer(read_only=True)


#     class Meta:
#         model = UserProfile
#         fields = "__all__"
    

class PreInscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreInscription
        fields = ("__all__")


class UpdatePasswordUserSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=False)


class CreatePasswordUserSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    confirm_password = serializers.CharField(required=False)


class ResetPasswordUserSerializer(serializers.Serializer):
    updated_by_id = serializers.CharField(required=True)
    account_to_reset_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class AppearanceSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True, write_only=True)
    dark_mode = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = Appearance
        fields = "__all__"


