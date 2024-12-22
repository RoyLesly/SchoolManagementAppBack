import graphene
from graphene_django.types import DjangoObjectType
from .models import ChatUser, Room, Message
from higher_control.user_control.models import CustomUser

# ChatUser Type
class ChatUserType(DjangoObjectType):
    class Meta:
        model = ChatUser
        fields = ("id", "name", "telephone", "created_at")

# Room Type
class RoomType(DjangoObjectType):
    online_count = graphene.Int()

    class Meta:
        model = Room
        fields = ("id", "room_name", "online", "online_count")

    def resolve_online_count(self, info):
        return self.get_online_count()

# Message Type
class MessageType(DjangoObjectType):
    sender_profile = graphene.Field(lambda: CustomUserType)
    reciever_profile = graphene.Field(lambda: CustomUserType)

    class Meta:
        model = Message
        fields = ("id", "user", "sender", "reciever", "room", "content", "is_read", "created_at", "sender_profile", "reciever_profile")

    def resolve_sender_profile(self, info):
        return CustomUser.objects.get(id=self.sender.id)

    def resolve_reciever_profile(self, info):
        return CustomUser.objects.get(id=self.reciever.id)

# CustomUser Type
class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")

# Query Class
class Query(graphene.ObjectType):
    all_chat_users = graphene.List(ChatUserType)
    all_rooms = graphene.List(RoomType)
    all_messages = graphene.List(MessageType)
    message_by_room = graphene.List(MessageType, room_id=graphene.ID())

    def resolve_all_chat_users(self, info):
        return ChatUser.objects.all()

    def resolve_all_rooms(self, info):
        return Room.objects.all()

    def resolve_all_messages(self, info):
        return Message.objects.all()

    def resolve_message_by_room(self, info, room_id):
        return Message.objects.filter(room_id=room_id)

# Mutations
class CreateChatUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        telephone = graphene.Int(required=True)

    chat_user = graphene.Field(ChatUserType)

    def mutate(self, info, name, telephone):
        chat_user = ChatUser(name=name, telephone=telephone)
        chat_user.save()
        return CreateChatUser(chat_user=chat_user)

class CreateRoom(graphene.Mutation):
    class Arguments:
        room_name = graphene.String(required=True)

    room = graphene.Field(RoomType)

    def mutate(self, info, room_name):
        room = Room(room_name=room_name)
        room.save()
        return CreateRoom(room=room)

class CreateMessage(graphene.Mutation):
    class Arguments:
        sender_id = graphene.ID(required=True)
        reciever_id = graphene.ID(required=True)
        room_id = graphene.ID(required=True)
        content = graphene.String(required=True)

    message = graphene.Field(MessageType)

    def mutate(self, info, sender_id, reciever_id, room_id, content):
        sender = ChatUser.objects.get(id=sender_id)
        reciever = ChatUser.objects.get(id=reciever_id)
        room = Room.objects.get(id=room_id)
        message = Message(sender=sender, reciever=reciever, room=room, content=content)
        message.save()
        return CreateMessage(message=message)

class Mutation(graphene.ObjectType):
    create_chat_user = CreateChatUser.Field()
    create_room = CreateRoom.Field()
    create_message = CreateMessage.Field()

# Schema Definition
schema = graphene.Schema(query=Query, mutation=Mutation)
