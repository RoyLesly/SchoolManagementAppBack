from django.db import models
from django.db.models.signals import post_save, pre_save
from higher_control.user_control.models import CustomUser, UserProfile
from higher_control.user_control.choices import SEMESTER_CHOICES, COURSE_TYPE_CHOICES
from datetime import date, datetime
from django.utils import timezone
from .functions import *
from .choices import *


def getCustomUserPerms(id):
    return CustomUser.objects.get(id=id).get_all_permissions()


class SchoolIdentification(models.Model):
    code = models.CharField(max_length=8, null=False, blank=False)
    platform_charges = models.IntegerField(blank=False, null=False, default=1000)
    name = models.CharField(max_length=80, null=False, blank=False, default="")
    status = models.BooleanField(default=True, null=False, blank=False)
    back_end = models.CharField(max_length=75, default="http://127.0.0.1:8000", null=False, blank=False)
    front_end = models.CharField(max_length=75, default="http://apitest.econneq.com", null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='schoolidentification_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='schoolidentification_updated_by', on_delete=models.PROTECT)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.code}-{self.status}"
    
    class Meta:
        ordering = ("created_at",)

        
class Campus(models.Model):
    name = models.CharField(max_length=15, choices=CAMPUS_CHOICES, null=False, blank=False, default="I")
    region = models.CharField(max_length=15, choices=REGION_CHOICES, null=False, blank=False, default="I")
    created_by = models.ForeignKey(CustomUser, null=True, related_name='campus_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='campus_updated_by', on_delete=models.PROTECT)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.region}-{self.name}"
    
    class Meta:
        ordering = ("created_at",)
        constraints = [ 
            models.UniqueConstraint(fields=["name", "region"], name="unique_campus")
        ]

post_save.connect(create_school_identification, sender=Campus)

        
     
class SchoolInfo(models.Model):
    campus = models.OneToOneField(Campus, related_name='schoolinfo_campus', on_delete=models.PROTECT)
    school_identification = models.ForeignKey(SchoolIdentification, related_name='schoolinfo_schoolidentification', on_delete=models.PROTECT)
    school_type = models.CharField(max_length=15, choices=CAMPUS_TYPES, null=False, blank=False, default="Secondary")
    main_school = models.BooleanField(default=False)
    school_name = models.CharField(max_length=50, blank=False)
    short_name = models.CharField(max_length=20, blank=False)
    director = models.CharField(max_length=50, blank=False, null=False, default="edit")
    address = models.CharField(max_length=20, blank=False)
    town = models.CharField(max_length=10, blank=False)
    region = models.CharField(max_length=12, choices=REGION_CHOICES, blank=False)
    country = models.CharField(max_length=12, blank=False, default="CAMEROON")
    po_box = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=30, blank=False)
    niu = models.CharField(max_length=50, blank=False)
    telephone_one = models.CharField(max_length=15, blank=False)
    telephone_two = models.CharField(max_length=15, blank=False)
    website = models.CharField(max_length=45, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='school_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='school_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.campus} {self.short_name}"
    

class Domain(models.Model):
    domain_name = models.CharField(max_length=50, blank=False, unique=True)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='domain_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='domain_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.domain_name}"


class Field(models.Model):
    field_name = models.CharField(max_length=50, blank=False, unique=True)
    domain = models.ForeignKey(Domain, null=True, related_name='field_domain', on_delete=models.PROTECT)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='field_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='field_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.field_name}"


class MainSpecialty(models.Model):
    specialty_name = models.CharField(max_length=50, blank=False, unique=True)
    specialty_name_short = models.CharField(max_length=5, blank=False, default="Edit")
    field = models.ForeignKey(Field, null=True, related_name='specialty_field', on_delete=models.PROTECT)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='main_specialty_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='main_specialty_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.specialty_name}"


class Level(models.Model):
    level = models.IntegerField(unique=True, null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='level_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='level_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.level}"
    

class Specialty(models.Model):
    school = models.ForeignKey(SchoolInfo, default=1, null=False, related_name='specialty_school_info', on_delete=models.PROTECT)
    main_specialty = models.ForeignKey(MainSpecialty, null=False, related_name='specialty_main_specialty', on_delete=models.PROTECT)
    level = models.ForeignKey(Level, null=False, default=1, related_name='specialty_level', on_delete=models.PROTECT)
    academic_year = models.CharField(max_length=9, blank=False, unique=False)
    tuition = models.IntegerField(default=0)
    registration = models.IntegerField(default=0)
    payment_one = models.IntegerField(default=0)
    payment_two = models.IntegerField(default=0)
    payment_three = models.IntegerField(default=0)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='specialty_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='specialty_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        pass
        constraints = [ 
            models.UniqueConstraint(fields=["school", "main_specialty", "academic_year", "level"], name="unique_specialty")
        ]
    def __str__(self):
        return f"{self.main_specialty}-L{self.level.level}-{self.academic_year}"
    
# post_save.connect(create_specialty_fees_from_course, sender=Specialty)
post_save.connect(create_publish_from_specialty, sender=Specialty)


class MainCourse(models.Model):
    course_name = models.CharField(max_length=50, blank=False, unique=True)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='main_course_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='main_course_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.course_name}"


class Course(models.Model):
    main_course = models.ForeignKey(MainCourse, null=True, related_name='course_main_course', on_delete=models.PROTECT)
    specialty = models.ForeignKey(Specialty, null=True, related_name='course_specialty', on_delete=models.PROTECT)
    course_code = models.CharField(max_length=10, blank=False)
    course_type = models.CharField(max_length=15, choices=COURSE_TYPE_CHOICES, null=False, blank=False, default="Fundamental")
    semester = models.CharField(max_length=15, choices=SEMESTER_CHOICES, null=False, blank=False, default="I")
    course_credit = models.IntegerField(blank=False)
    completed = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    hours = models.IntegerField(default=0)
    hours_left = models.DecimalField(max_digits=5, decimal_places=2)
    date_assigned = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey(CustomUser, null=True, blank=True, related_name='course_lecturer', on_delete=models.PROTECT)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='course_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='course_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.main_course}-{self.specialty}"
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=["specialty", "main_course"], name="unique_course") ]
    
post_save.connect(create_result_from_course, sender=Course)


class Result(models.Model):
    student = models.ForeignKey(UserProfile, null=True, related_name='result_userprofile', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, null=True, related_name='result_course', on_delete=models.PROTECT)
    matricle = models.CharField(max_length=15, null=True, blank=True)
    ca = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    exam = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    resit = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    average = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    validated = models.BooleanField(default=False)
    publish_ca = models.BooleanField(default=False)
    publish_exam = models.BooleanField(default=False)
    publish_resit = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='result_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='result_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.student.user.first_name}-{self.course.main_course.course_name}"
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=["course", "student"], name="unique_result") ]
        
    def calculate_average(self):
        try:
            if int(self.exam) > 0 and int(self.ca) > 0:
                self.average = self.ca + self.exam
        except: 
            pass
        try:
            if int(self.resit) > 0 and int(self.ca) > 0:
                self.average = self.ca + self.resit 
        except: 
            pass
        try:
            if self.ca is None and int(self.exam) > 0:
                self.average = self.exam 
        except: 
            pass
        try:
            if self.ca is None and int(self.resit) > 0:
                self.average = self.resit
        except: 
            pass
        try:
            if int(self.ca) > 0 and self.exam is None and self.resit is None:
                self.average = self.ca
        except: 
            pass
        try:
            if self.average > 49.99:
                self.validated = True
            else:
                self.validated = False
        except:
            pass

    def save(self, *args, **kwargs):
        self.matricle = self.student.user.matricle
        self.calculate_average()        
        super(Result, self).save(*args, **kwargs)


post_save.connect(create_publish_from_result, sender=Result)
    

class Publish(models.Model):
    specialty = models.ForeignKey(Specialty, null=True, related_name='publish_specialty', on_delete=models.PROTECT)
    semester = models.CharField(max_length=15, choices=SEMESTER_CHOICES, null=False, blank=False, default="I")
    ca = models.BooleanField(default=False)
    exam = models.BooleanField(default=False)
    resit = models.BooleanField(default=False)
    portal_ca = models.BooleanField(default=False)
    portal_exam = models.BooleanField(default=False)
    portal_resit = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='publish_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='publish_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.specialty}-{self.semester}"
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=["specialty", "semester"], name="unique_publish") ]

post_save.connect(update_results_from_publish, sender=Publish)


class SysCategory(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ("name",)


class SysConstant(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    sys_category = models.ForeignKey(SysCategory, null=True, related_name='sysconstant_sys_category', on_delete=models.PROTECT)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='sysconstant_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='sysconstant_updated_by', on_delete=models.PROTECT)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.sys_category}"
    
    class Meta:
        ordering = ("name",)


