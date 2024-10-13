from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *
from user_control.serializers import CustomUserSerializer, GetCustomUserSerializer
from app_control.serializers import SpecialtySerializer, UserProfileSerializer


class SchoolFeesSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=False)
    userprofile = UserProfileSerializer(read_only=True)
    userprofile_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = PrimSchoolFees
        fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
    schoolfees = SchoolFeesSerializer(read_only=True)
    schoolfees_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = PrimTransactions
        fields = "__all__"


class PrimActivationKeySerializer(serializers.ModelSerializer):
    key = serializers.CharField(write_only=True, required=False)
    is_used = serializers.BooleanField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = PrimActivationKey
        fields = "__all__"



# LIST SERIALIZERS =======================================================================================================


class GetSchoolFeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    userprofile__id = serializers.CharField(read_only=True)
    userprofile__user__id = serializers.CharField(read_only=True)
    userprofile__user__full_name = serializers.CharField(read_only=True)
    userprofile__user__matricle = serializers.CharField(read_only=True)
    userprofile__user__role = serializers.CharField(read_only=True)
    userprofile__user__username = serializers.CharField(read_only=True)
    userprofile__specialty__id = serializers.CharField(read_only=True)
    userprofile__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    userprofile__specialty__level__level = serializers.CharField(read_only=True)
    userprofile__specialty__academic_year = serializers.CharField(read_only=True)
    userprofile__specialty__tuition = serializers.IntegerField(read_only=True)
    userprofile__specialty__payment_one = serializers.IntegerField(read_only=True)
    userprofile__specialty__payment_two = serializers.IntegerField(read_only=True)
    userprofile__specialty__payment_three = serializers.IntegerField(read_only=True)
    platform_charges = serializers.IntegerField(read_only=True)
    platform_paid = serializers.BooleanField(read_only=True)
    balance = serializers.IntegerField(read_only=True)


class GetTransactionsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)    
    schoolfees__id = serializers.IntegerField(read_only=True)
    schoolfees__userprofile__id = serializers.IntegerField(read_only=True)
    schoolfees__userprofile__user__id = serializers.IntegerField(read_only=True)
    schoolfees__userprofile__user__full_name = serializers.CharField(read_only=True)
    schoolfees__userprofile__specialty__id = serializers.IntegerField(read_only=True)
    schoolfees__userprofile__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    schoolfees__userprofile__specialty__academic_year = serializers.CharField(read_only=True)
    schoolfees__userprofile__specialty__level__level = serializers.IntegerField(read_only=True)
    schoolfees__userprofile__specialty__tuition = serializers.IntegerField(read_only=True)
    schoolfees__platform_charges = serializers.CharField(read_only=True)
    schoolfees__platform_paid = serializers.BooleanField(read_only=True)
    schoolfees__balance = serializers.CharField(read_only=True)
    payer_name = serializers.CharField(read_only=True)
    telephone = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    operator = serializers.CharField(read_only=True)
    payment_method = serializers.CharField(read_only=True)    
    reason = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    ref = serializers.CharField(read_only=True)

    created_at = serializers.CharField(read_only=True)
    created_by__first_name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetActivationKeySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)    
    name = serializers.CharField(read_only=True)
    account_name = serializers.CharField(read_only=True)
  
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)

