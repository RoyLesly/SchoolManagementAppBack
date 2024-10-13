from django.contrib import admin
from .models import *


class MessageAdmin(admin.ModelAdmin):
    list_editable = [ 'is_read' ]
    list_display = [ "id", "is_read", "user", "sender", "reciever", "content", "room", "created_at"]

admin.site.register(Message, MessageAdmin)
admin.site.register(Room)
