from rest_framework import serializers
from . models import *
from user_control.serializers import CustomUserSerializer, GetCustomUserSerializer

import importlib


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"
        dept = 1


class MessageSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True, required=False)
    sender = CustomUserSerializer(read_only=True)
    sender_id = serializers.CharField(write_only=True, required=False)
    reciever = CustomUserSerializer(read_only=True)
    reciever_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Message
        fields = "__all__"
        dept = 1