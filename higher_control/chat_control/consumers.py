import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from . models import *  # Assuming you have a ChatMessage model
from . serializers import *  # Assuming you have a ChatMessage model

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.room_name, "Here 1")
        self.room_group_name = f"chat_{self.room_name}"
        print(self.room_group_name, "Here 2")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        past_messages = await self.get_past_messages(self.room_name)
        await self.send(text_data=json.dumps({
            "past_messages": past_messages
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        reciever_id = text_data_json['reciever_id']
        user_id = text_data_json['user_id']
        room_id = text_data_json['room_id']

        # Save chat message to the model
        await self.save_chat_message(user_id, reciever_id, room_id, message)

        # Send message to WebSocket
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @sync_to_async
    def save_chat_message(self, user_id, reciever_id, room_id, message):
        # Save chat message to your database model
        print(room_id)
        print(message)
        print(reciever_id,)
        print(user_id)
        t = MessageSerializer(data=
            {"user_id": user_id, "room": room_id, "content": message, "sender": user_id, "reciever_id": reciever_id}
        )
        if (t.is_valid()):
            print("VALID")
            t.save()

    @sync_to_async
    def get_past_messages(self, room_name):
        # Retrieve messages from the database and serialize them
        messages = Message.objects.filter(room__room_name=room_name).values('content')
        return list(messages)  # Convert queryset to list of dictionaries
