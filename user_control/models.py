from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, PermissionsMixin, BaseUserManager )
from django.db.models.signals import post_save
from user_control.functions import create_profile, create_appearance, send_email_update, create_result_from_profile
from user_control.choices import DARK_MODE_CHOICES, DEPT_CHOICES, ROLE_CHOICES, TITLE_CHOICES, LANG_CHOICES
from datetime import datetime
from rest_framework.response import Response
import random


def getCustomUserPerms(id):
    try:
        return CustomUser.objects.get(id=id).get_all_permissions()
    except:
        return Exception("NOT LOGGED IN")


def check_permission(user_id, perm_check):
    if not CustomUser.objects.filter(id=user_id).first():
        print("NOT")
        raise Exception({ "errors": "NOT LOGGED IN" })
    perms = getCustomUserPerms(user_id)
    x = perm_check in perms
    if not x:
        a = perm_check.split('.')[1].split('_')
        raise Exception("Not Authorised To " + " ".join(a))

class CustomUserManager(BaseUserManager):
    def create_superuser(self, password, username, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', "admin")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser Must Have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser Must Have is_superuser=True")

        if not username:
            raise ValueError("Username Field Is Required")

        user = self.model(
            username=username, **extra_fields, 
        )
        user.set_password(password)
        user.save()

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=15, unique=True)
    matricle = models.CharField(max_length=15, unique=False, blank=True, default=random.randint(11111, 99999))
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    email = models.EmailField(null=False, unique=True, blank=False)
    hod = models.BooleanField(default=False, blank=True)
    email_confirmed = models.BooleanField(default=False, blank=True)
    first_name = models.CharField(max_length=50, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=6, blank=True, null=True)
    telephone = models.CharField(default=0, max_length=50, blank=True)
    title = models.CharField(max_length=15, choices=TITLE_CHOICES, blank=True, null=True)
    pob = models.CharField(max_length=25, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["role", "email"]
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("created_at",)
    

post_save.connect(create_profile, sender=CustomUser)
post_save.connect(create_appearance, sender=CustomUser)


class UserProfile(models.Model):
    user = models.ForeignKey( CustomUser, related_name="userprofile_user", null=True, on_delete=models.PROTECT )
    specialty = models.ForeignKey("app_control.Specialty", blank=True, null=True, related_name='userprofile_specialty', on_delete=models.SET_NULL)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [ 
            models.UniqueConstraint(fields=["specialty", "user"], name="unique_profile"),
        ]

    def __str__(self):
        return f"{self.user.username}"    

post_save.connect(create_result_from_profile, sender=UserProfile)
post_save.connect(send_email_update, sender=UserProfile)

class Appearance(models.Model):
    user = models.OneToOneField( CustomUser, related_name="appearance_user", null=True, on_delete=models.CASCADE )
    dark_mode = models.CharField(max_length=15, choices=DARK_MODE_CHOICES, default="light")
    lang = models.CharField(max_length=15, choices=LANG_CHOICES, default="En")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.username}"


class UserActivities(models.Model):
    username = models.CharField(max_length=50)
    action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "UserActivities"

    def __str__(self):
        return f"{self.username} {self.action} on {self.created_at}"


class PasswordToken(models.Model):
    user_profile = models.OneToOneField( UserProfile, related_name="passwordtoken_userprofile", null=False, on_delete=models.CASCADE )
    token = models.CharField(max_length=6, unique=True)
    expired = models.BooleanField(null=False)
    sent_mail = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user_profile.id} {self.token} on {self.updated_at}"

