from django.db import models
from rest_framework.response import Response
from django.contrib.auth.models import ( AbstractBaseUser, PermissionsMixin, BaseUserManager )
from django.db.models.signals import post_save
from higher_control.user_control.functions import *
from higher_control.user_control.functionsSpecific import *
from higher_control.user_control.choices import *


def getCustomUserPerms(id):
    try:
        return CustomUser.objects.get(id=id).get_all_permissions()
    except:
        return Exception("NOT LOGGED IN")


def check_permission(user_id, perm_check):
    if not CustomUser.objects.filter(id=user_id).first():
        # return Response({ "errors": "NOT LOGGED IN" })
        raise Exception({ "errors": "NOT LOGGED IN" })
    perms = getCustomUserPerms(user_id)
    x = perm_check in perms
    if not x:
        a = perm_check.split('.')[1].split('_')
        # return Response({ "errors": "Not Authorized To " + " ".join(a)})
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

    username = models.CharField(max_length=19, unique=True)
    matricle = models.CharField(max_length=15, unique=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, blank=False)
    password_set = models.BooleanField(default=False)
    
    dept = models.ManyToManyField("user_control.Department", blank=True)
    page = models.ManyToManyField("user_control.Page", blank=True)
    school = models.ManyToManyField("app_control.SchoolInfo", blank=False, related_name='user_shool')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, unique=True, blank=True)
    hod = models.BooleanField(default=False, blank=True)
    email_confirmed = models.BooleanField(default=False, blank=True)
    first_name = models.CharField(max_length=15, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    
    about = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    telephone = models.CharField(unique=True, max_length=13, blank=True, null=True)
    title = models.CharField(max_length=15, choices=TITLE_CHOICES, blank=True, null=True)
    pob = models.CharField(max_length=25, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    parent = models.CharField(max_length=30, null=True, blank=True)
    parent_telephone = models.CharField(unique=False, max_length=28, blank=True, null=True)
    # created_campus = models.ManyToManyField("app_control.SchoolInfo", blank=False, related_name='user_created_campus')

    prefix = models.CharField(unique=False, max_length=28, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = "matricle"
    REQUIRED_FIELDS = ["role", "email", "username"]
    objects = CustomUserManager()
    

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("-created_at",)
    
    def generate_registration_number(self):
        if self.role == "student" and not self.matricle:
            pref = self.prefix.upper()
            if self.prefix[0] == "1":
                self.matricle = f"{str(pref)[1:3]}{pref[3:]}{str(self.id)[0:].zfill(4)}"
            elif self.prefix[0] == "2":
                self.matricle = f"{pref[3]}{str(pref)[1:3]}{pref[3:]}{str(self.id)[0:].zfill(4)}"
            elif self.prefix[0] == "3":
                self.matricle = f"{pref[3:]}{str(pref)[1:3]}{pref[2:]}{str(self.id)[0:].zfill(4)}"
            else:
                self.matricle = f"{pref[3:]}{str(pref)[1:3]}{str(self.id)[0:4].zfill(4)}"
            self.username = self.matricle
        else:
            self.matricle = f"{str(self.first_name.strip().split()[0])}{str(self.id)[0:4].zfill(4)}"
            self.username = f"{str(self.first_name.strip().split()[0])}{str(self.id)[0:4].zfill(4)}"
        self.full_name = f"{self.first_name.strip()} {self.last_name}"
        

def registration_post_save(sender, instance, created, *args, **kwargs):
        if created:
            instance.generate_registration_number()
            instance.save()
    
        
post_save.connect(registration_post_save, sender=CustomUser)
post_save.connect(create_profile, sender=CustomUser)
post_save.connect(create_appearance, sender=CustomUser)


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True, choices=DEPT_CHOICES, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='department_created_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='department_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"
        
        
class Program(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='program_created_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='program_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Programs"

    def __str__(self):
        return f"{self.name}"


class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, related_name="userprofile_user", null=True, on_delete=models.PROTECT )
    specialty = models.ForeignKey("app_control.Specialty", blank=True, null=True, related_name='userprofile_specialty', on_delete=models.SET_NULL)
    matricle = models.CharField(max_length=15, null=True, blank=True)
    active = models.BooleanField(default=True, blank=False)
    program = models.ForeignKey( Program, related_name="userprofile_program", default=1, null=False, on_delete=models.PROTECT )
    session = models.CharField(max_length=15, choices=SESSION_CHOICES, default="Morning")
    code = models.ImageField(blank=True, null=True, upload_to="code")

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [ 
            models.UniqueConstraint(fields=["specialty", "user"], name="unique_profile"),
        ]

    def __str__(self):
        return f"PI-{self.id}-{self.user.first_name}-UI-{self.user.id}"          

post_save.connect(create_code_profile, sender=UserProfile)
post_save.connect(create_result_from_profile, sender=UserProfile)
post_save.connect(profile_activate_deactivate_results, sender=UserProfile)
post_save.connect(create_schoolfees, sender=UserProfile)


class Appearance(models.Model):
    user = models.OneToOneField(CustomUser, related_name="appearance_user", null=True, on_delete=models.CASCADE )
    dark_mode = models.CharField(max_length=15, choices=DARK_MODE_CHOICES, default="light")
    lang = models.CharField(max_length=15, choices=LANG_CHOICES, default="En")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user.username}"
    

class Page(models.Model):
    name = models.CharField(max_length=50, choices=PAGE_CHOICES, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='page_created_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='page_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.name}"
        
        
class PreInscription(models.Model):
    registration_number = models.CharField(max_length=20, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)    
    full_name = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=6, choices=GENDER, blank=False, null=False)
    email = models.EmailField(null=False, unique=True, blank=False)
    telephone = models.CharField(unique=True, max_length=13, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    pob = models.CharField(max_length=25, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=8, choices=PREINSCRIPTION_STATUS, blank=False, null=False)
    emergency_name = models.CharField(max_length=30, null=False, blank=False)
    emergency_town = models.CharField(max_length=30, null=True, blank=True)
    emergency_telephone = models.CharField(unique=False, max_length=28, blank=False, null=False)
    program = models.CharField(max_length=12, choices=PROGRAM_CHOICES, blank=False, null=False)
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES, blank=False, null=False)
    session = models.CharField(max_length=12, choices=SESSION_CHOICES, blank=False, null=False)
    academic_year = models.CharField(unique=False, max_length=10, blank=False, null=False)
    specialty_one = models.CharField(unique=False, max_length=50, blank=False, null=False)
    specialty_two = models.CharField(unique=False, max_length=50, blank=False, null=False)
    specialty_three = models.CharField(unique=False, max_length=50, blank=False, null=False)
    campus = models.CharField(unique=False, max_length=20, default="Campus-A", blank=False, null=False)
    admission_status = models.BooleanField(default=False)
    action = models.CharField(max_length=12, choices=PREINSCRIPTION_ACTION, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        ordering = ("-created_at",)
    
    def generate_reg_number(self):
        self.registration_number = f"{str(self.academic_year)[2:4]}{self.first_name}{str(self.id)[0:2].zfill(2)}"
        self.full_name = f"{self.first_name} {self.last_name}"  

post_save.connect(preinscription_post_save, sender=PreInscription)
