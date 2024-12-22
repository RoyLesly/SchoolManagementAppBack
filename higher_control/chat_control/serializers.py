from rest_framework import serializers
from . models import *
from higher_control.user_control.serializersGet import CustomUserSerializer

import importlib

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUser
        fields = "__all__"
        dept = 1


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"
        dept = 1


class MessageSerializer(serializers.ModelSerializer):
    user = ChatUserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True, required=False)
    sender = ChatUserSerializer(read_only=True)
    sender_id = serializers.CharField(write_only=True, required=False)
    reciever = ChatUserSerializer(read_only=True)
    reciever_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Message
        fields = "__all__"
        dept = 1