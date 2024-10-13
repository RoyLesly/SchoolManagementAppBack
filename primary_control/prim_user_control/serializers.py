from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from higher_control.user_control.models import *
from datetime import datetime
# import importlib


class GetPrimaryProfileSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user__id = serializers.IntegerField(read_only=True)
    user__first_name = serializers.CharField(read_only=True)
    user__last_name = serializers.CharField(read_only=True)
    user__full_name = serializers.CharField(read_only=True)
    user__matricle = serializers.CharField(read_only=True)
    user__username = serializers.CharField(read_only=True)
    user__sex = serializers.CharField(read_only=True)
    user__telephone = serializers.CharField(read_only=True)
    user__dob = serializers.CharField(read_only=True)
    user__pob = serializers.CharField(read_only=True)
    user__email = serializers.CharField(read_only=True)
    classroom__id = serializers.IntegerField(read_only=True)
    classroom__level__level = serializers.CharField(read_only=True)
    classroom__level__option = serializers.CharField(read_only=True)
    classroom__domain = serializers.CharField(read_only=True)
    classroom__academic_year = serializers.CharField(read_only=True)
    classroom__level__level = serializers.CharField(read_only=True)
    user__school__campus__name = serializers.CharField(read_only=True)
    active = serializers.CharField(read_only=True)
    session = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)

