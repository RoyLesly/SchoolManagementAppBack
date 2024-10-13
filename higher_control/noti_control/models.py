from django.db import models
from higher_control.user_control.models import CustomUser
from django.db.models.signals import post_save
from .functions import *
from .choices import *


class Notification(models.Model):
    message_one = models.CharField(max_length=255, null=False, blank=False)
    message_two = models.CharField(max_length=255, null=True, blank=True)
    target = models.CharField(max_length=15, choices=TARGET_CHOICES, blank=True, null=True)
    schools = models.ManyToManyField("app_control.SchoolInfo", blank=True)
    domains = models.ManyToManyField("app_control.Domain", blank=True)
    specialty = models.ManyToManyField("app_control.Specialty", blank=True)
    custom = models.CharField(max_length=50, choices=CUSTOM_NOTI_QUERY_CHOICES, blank=True, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, blank=True, null=True)
    noti_type = models.CharField(max_length=15, choices=NOTI_TYPE_CHOICES, blank=True, null=True)

    status = models.BooleanField(default=True, null=False, blank=False)
    ending_at = models.DateField(null=False)
    
    created_by = models.ForeignKey(CustomUser, null=True, related_name='notification_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='notification_updated_by', on_delete=models.PROTECT)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.role}-{self.status}-{self.noti_type}"
    

post_save.connect(deactivate_notifications, sender=Notification)




class Complain(models.Model):
    message_one = models.CharField(max_length=255, null=False, blank=False)
    message_two = models.CharField(max_length=255, null=True, blank=True)
    complain_type = models.CharField(max_length=15, choices=COMPLAIN_TYPE_CHOICES, blank=True, null=True)

    status = models.BooleanField(default=True, null=False, blank=False)
    ending_at = models.DateField(null=False)
    
    created_by = models.ForeignKey(CustomUser, null=True, related_name='complain_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='complain_updated_by', on_delete=models.PROTECT)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.complain_type}-{self.status}-{self.ending_at}"


class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser, related_name="user_activity_user", null=True, on_delete=models.CASCADE )
    action = models.TextField()
    item = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-updated_at",)
        verbose_name_plural = "UserActivities"

    def __str__(self):
        return f"{self.user.username} {self.action} on {self.updated_at}"