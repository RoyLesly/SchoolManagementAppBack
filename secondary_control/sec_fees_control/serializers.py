from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *
from higher_control.user_control.serializers import CustomUserSerializer
from secondary_control.sec_app_control.serializers import SecondaryProfileSerializer
from .serializers import *
from .models import *


class SecSchoolFeesSerializer(serializers.ModelSerializer):
    secondaryprofile = SecondaryProfileSerializer(read_only=True)
    secondaryprofile_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = SecSchoolFees
        fields = "__all__"


class SecTransactionsSerializer(serializers.ModelSerializer):
    secschoolfees = SecSchoolFeesSerializer(read_only=True)
    secschoolfees_id = serializers.CharField(write_only=True, required=True)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = SecTransactions
        fields = "__all__"


class ActivationKeySerializer(serializers.ModelSerializer):
    key = serializers.CharField(write_only=True, required=False)
    is_used = serializers.BooleanField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = ActivationKey
        fields = "__all__"



# LIST SERIALIZERS =======================================================================================================


class GetSecSchoolFeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    secondaryprofile__id = serializers.CharField(read_only=True)
    secondaryprofile__user__id = serializers.CharField(read_only=True)
    secondaryprofile__user__full_name = serializers.CharField(read_only=True)
    secondaryprofile__user__matricle = serializers.CharField(read_only=True)
    secondaryprofile__user__role = serializers.CharField(read_only=True)
    secondaryprofile__user__username = serializers.CharField(read_only=True)
    secondaryprofile__secondary_classroom__id = serializers.CharField(read_only=True)
    secondaryprofile__secondary_classroom__level__level = serializers.CharField(read_only=True)
    secondaryprofile__secondary_classroom__academic_year = serializers.CharField(read_only=True)
    secondaryprofile__secondary_classroom__tuition = serializers.IntegerField(read_only=True)
    secondaryprofile__secondary_classroom__payment_one = serializers.IntegerField(read_only=True)
    secondaryprofile__secondary_classroom__payment_two = serializers.IntegerField(read_only=True)
    secondaryprofile__secondary_classroom__payment_three = serializers.IntegerField(read_only=True)
    platform_charges = serializers.IntegerField(read_only=True)
    platform_paid = serializers.BooleanField(read_only=True)
    balance = serializers.IntegerField(read_only=True)


class GetSecTransactionsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)    
    secschoolfees__id = serializers.IntegerField(read_only=True)
    secschoolfees__secondary_profile__id = serializers.IntegerField(read_only=True)
    secschoolfees__secondary_profile__user__id = serializers.IntegerField(read_only=True)
    secschoolfees__secondary_profile__user__full_name = serializers.CharField(read_only=True)
    secschoolfees__secondary_profile__secondary_classroom__id = serializers.IntegerField(read_only=True)
    secschoolfees__secondary_profile__secondary_classroom__main_secondary_classroom__secondary_classroom_name = serializers.CharField(read_only=True)
    secschoolfees__secondary_profile__secondary_classroom__academic_year = serializers.CharField(read_only=True)
    secschoolfees__secondary_profile__secondary_classroom__level__level = serializers.IntegerField(read_only=True)
    secschoolfees__secondary_profile__secondary_classroom__tuition = serializers.IntegerField(read_only=True)
    secschoolfees__platform_charges = serializers.CharField(read_only=True)
    secschoolfees__platform_paid = serializers.BooleanField(read_only=True)
    secschoolfees__balance = serializers.CharField(read_only=True)
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

