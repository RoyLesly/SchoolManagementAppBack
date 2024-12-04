from rest_framework import serializers
# from .models import *
from .models import Domain as Dom, Tenant
from higher_control.user_control.serializers import CustomUserSerializer, GetCustomUserSerializer


class TenantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    school_name = serializers.CharField(write_only=True, required=True)
    school_type = serializers.CharField(write_only=True, required=True)
    description = serializers.CharField(write_only=True, required=True)
    is_active = serializers.BooleanField(write_only=True, required=True)
    updated_at = serializers.CharField(write_only=True, required=False)
    created_on = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Tenant
        fields = "__all__"
        dept = 1


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dom
        fields = "__all__"
        dept = 1



# LIST SERIALIZERS =======================================================================================================


class GetTenantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user__id = serializers.IntegerField(read_only=True)
    user__full_name = serializers.CharField(read_only=True)
    school_name = serializers.CharField(read_only=True)
    school_type = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    created_on = serializers.CharField(read_only=True)


class GetDomainSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    domain = serializers.CharField(read_only=True)
    tenant__id = serializers.IntegerField(read_only=True)
    tenant__user__id = serializers.IntegerField(read_only=True)
    tenant__user__full_name = serializers.CharField(read_only=True)
    tenant__school_name = serializers.CharField(read_only=True)
    tenant__school_type = serializers.CharField(read_only=True)
    tenant__description = serializers.CharField(read_only=True)
    tenant__is_active = serializers.IntegerField(read_only=True)
    is_primary = serializers.BooleanField(read_only=True)


class SchoolIdentificationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    logo = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)
    version = serializers.CharField(read_only=True)
    director = serializers.CharField(read_only=True)
    platform_charges = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    support_number_one = serializers.CharField(read_only=True)
    support_number_two = serializers.CharField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    back_end = serializers.CharField(read_only=True)
    front_end = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


