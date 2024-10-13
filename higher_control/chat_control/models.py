from django.db import models


from django.contrib.auth.models import User
from django.db import models
from higher_control.user_control.models import CustomUser


class Room(models.Model):
    room_name = models.CharField(max_length=128)
    online = models.ManyToManyField(CustomUser, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.room_name} ({self.get_online_count()})'


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="message_user")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reciever")
    
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    content = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.created_at}]'

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Message"

    @property
    def sender_profile(self):
        sender = CustomUser.objects.get(user=self.sender)
        return sender
    
    @property
    def reciever_profile(self):
        reciever = CustomUser.objects.get(user=self.reciever)
        return reciever
