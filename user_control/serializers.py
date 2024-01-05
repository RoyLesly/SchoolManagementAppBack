from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import importlib
from user_control.models import (CustomUser, ROLE_CHOICES, UserActivities, Appearance)


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
    username = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(ROLE_CHOICES)


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    role = serializers.ChoiceField(ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        exclude = ("password",)
        # fields = "__all__"
        dept = 1

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password",)


class GetUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    user_permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = CustomUser
        fields = ("__all__")

class LoginSerialiser(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class CheckUserSerialiser(serializers.Serializer):
    username = serializers.CharField(required=True)


class LogoutSerialiser(serializers.Serializer):
    user_id = serializers.CharField(required=True)


class AssignGroupsToUserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Group.objects.all(), required=True)
    password = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ("__all__")


class AssignPermissionsToGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Permission.objects.all(), required=True)

    class Meta:
        model = Group
        fields = ("__all__")


class UpdatePasswordUserSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()
    newPassword = serializers.CharField(required=False)


class CreatePasswordUserSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=False)
    password = serializers.CharField(required=False)


class ResetPasswordUserSerializer(serializers.Serializer):
    updated_by_id = serializers.CharField(required=True)
    account_to_reset_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ForgotPasswordSerializer(serializers.Serializer):
    data = serializers.CharField(required=True)
    auth_method = serializers.CharField(required=True)


class PasswordTokenSerializer(serializers.Serializer):
    data = serializers.CharField(required=True)
    auth_method = serializers.CharField(required=True)


class UserActivitiesSerializer(serializers.Serializer):
    class Meta:
        model = UserActivities
        fields = ("__all__")


class AppearanceSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = Appearance
        fields = "__all__"
        dept = 1

