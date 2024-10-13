from django.urls import path
from .views import *

app_name = "higher_control.chat_control"


urlpatterns = [
    path('', index_view, name='chat-index'),
    path('my-messages/<user_id>/', MyInbox.as_view(), name='my-messages'),
    path('get-messages/<sender_id>/<reciever_id>', GetMessages.as_view(), name='get-messages'),
    path('send-message', SendMessages.as_view(), name='send-messages'),
    path('search-users/<username>', SearchUser.as_view(), name='send-messages'),
    path('<str:room_name>', room_view, name='chat-room'),
]