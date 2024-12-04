from rest_framework import serializers
from higher_control.noti_control.models import *
from higher_control.app_control.serializers import SchoolInfoHigher, Domain, Specialty, DomainSerializer, SpecialtySerializer
from higher_control.user_control.serializers import CustomUserSerializer
from datetime import datetime
import importlib

class IDListField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id
    
    
class NotificationSerializer(serializers.ModelSerializer):
    schools = serializers.PrimaryKeyRelatedField(many=True, queryset=SchoolInfoHigher.objects.all(), required=False)
    domains = serializers.PrimaryKeyRelatedField(many=True, queryset=Domain.objects.all(), required=False)
    specialty = serializers.PrimaryKeyRelatedField(many=True, queryset=Specialty.objects.all(), required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Notification
        fields = ("__all__")


class ComplainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complain
        fields = ("__all__")


class UserActivitySerializer(serializers.Serializer):
    class Meta:
        model = UserActivity
        fields = ("__all__")



# LIST SERIALIZERS =======================================================================================================

class GetNotificationSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    message_one = serializers.CharField(read_only=True)
    message_two = serializers.CharField(read_only=True)
    noti_type = serializers.CharField(read_only=True)
    target = serializers.CharField(read_only=True)
    ending_at = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    # schools = SchoolInfoSerializer(many=True, read_only=True)
    # domains = DomainSerializer(many=True, required=True)
    # specialty = SpecialtySerializer(many=True, required=True)

    class Meta:
        model = Notification
        fields = ("__all__")


class GetComplainSerializer(serializers.ModelSerializer):
    # domains = DomainSerializer(many=True, read_only=True, required=False)
    # classes = SpecialtySerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Complain
        fields = ("__all__")


class GetUserActivitySerializer(serializers.ModelSerializer):
    domains = DomainSerializer(many=True, read_only=True, required=False)
    classes = SpecialtySerializer(many=True, read_only=True, required=False)

    class Meta:
        model = UserActivity
        fields = ("__all__")