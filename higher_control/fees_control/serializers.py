from rest_framework import serializers
from .models import *
from tenant.serializers import validate_user_exists


class ActivationKeySerializer(serializers.ModelSerializer):
    key = serializers.CharField(write_only=True, required=False)
    is_used = serializers.BooleanField(write_only=True, required=False)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = ActivationKey
        fields = "__all__"
        
    # def validate(self, attrs):
    #     validate_user_exists(attrs)


class SchoolFeesSerializer(serializers.ModelSerializer):
    specialty_id = serializers.IntegerField(write_only=True, required=False)
    userprofile_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = SchoolFees
        fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
    schoolfees = SchoolFeesSerializer(read_only=True)
    schoolfees_id = serializers.IntegerField(write_only=True, required=True)
    created_by_id = serializers.CharField(write_only=True, required=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Transactions
        fields = "__all__"


class TranscriptApplicationSerializer(serializers.ModelSerializer):
    userprofile_id = serializers.IntegerField(write_only=True, required=True)
    approved_by_id = serializers.CharField(write_only=True, required=False)
    printed_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = TranscriptApplication
        fields = "__all__"

    # def validate(self, attrs):
    #     validate_user_exists(attrs)


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = "__all__"
    
    # def validate(self, attrs):
    #     validate_user_exists(attrs)
