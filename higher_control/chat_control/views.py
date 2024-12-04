from . models import *
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . serializers import *
from django.db.models import F, Q, OuterRef, Subquery, Value




def index_view(request):
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(room_name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })


class MyInbox(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        messages = Message.objects.filter(
            id__in=Subquery(
                CustomUser.objects.filter(
                    Q(sender__reciever=user_id)|
                    Q(reciever__sender=user_id)
                ).distinct().annotate(
                    last_msg=Subquery(
                        Message.objects.filter(
                            Q(sender=OuterRef("id"), reciever=user_id)|
                            Q(reciever=OuterRef("id"), sender=user_id)
                        ).order_by("-id")[:1].values_list("id", flat=True)
                    )
                ).values_list("last_msg", flat=True).order_by("-id")
            )
        ).order_by("-id")

        return messages
    

class GetMessages(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        reciever_id = self.kwargs['reciever_id']

        messages = Message.objects.filter(
            sender__in=[sender_id, reciever_id],
            reciever__in=[sender_id, reciever_id]
        )

        return messages

class SendMessages(generics.CreateAPIView):
    serializer_class = MessageSerializer


class SearchUser(generics.ListAPIView):

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        username = self.kwargs["username"]
        logged_in_user = self.request.user
        users = CustomUser.objects.filter(
            Q(username__icontains=username)|
            Q(telephone__contains=username)|
            Q(email__contains=username)
            # Q(email__contains=username) &
            # ~Q(username=logged_in_user.username)
        )

        print(users)

        if not users:
            return Response(
                { "detail": "No Users Found!!" },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
    



class MessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        print(self.kwargs)
        return Message.objects.filter(room__room_name=room_name)


class RoomListView(ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        print(self.kwargs)
        return Room.objects.filter(room_name=room_name)
