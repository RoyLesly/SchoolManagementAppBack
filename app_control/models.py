from django.db import models
from django.db.models.signals import post_save
from user_control.models import CustomUser, UserProfile
from user_control.choices import SEMESTER_CHOICES, COURSE_TYPE_CHOICES
from datetime import date, datetime
from django.utils import timezone


def getCustomUserPerms(id):
    return CustomUser.objects.get(id=id).get_all_permissions()


class Domain(models.Model):
    domain_name = models.CharField(max_length=50, blank=False, unique=True)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='domain_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='domain_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.domain_name}"


class MainSpecialty(models.Model):
    specialty_name = models.CharField(max_length=50, blank=False, unique=True)
    domain = models.ForeignKey(Domain, null=True, related_name='specialty_domain', on_delete=models.SET_NULL)
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
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.level}"
    

class Specialty(models.Model):
    main_specialty = models.ForeignKey(MainSpecialty, null=True, related_name='specialty_main_specialty', on_delete=models.PROTECT)
    level = models.ForeignKey(Level, null=False, default=1, related_name='specialty_level', on_delete=models.PROTECT)
    academic_year = models.CharField(max_length=9, blank=False, unique=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='specialty_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='specialty_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        pass
        constraints = [ 
            models.UniqueConstraint(fields=["main_specialty", "academic_year", "level"], name="unique_specialty")
        ]
    def __str__(self):
        return f"{self.main_specialty}-L{self.level.level}-{self.academic_year}"


class MainCourse(models.Model):
    course_name = models.CharField(max_length=50, blank=False, unique=True)
    # main_specialty = models.ForeignKey(MainSpecialty, null=True, related_name='course_specialty', on_delete=models.SET_NULL)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='main_course_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='main_course_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.course_name}"
    

def create_result_from_course(sender, **kwargs):
    created_course = kwargs['instance']
    created_course_specialty_id = created_course.specialty.id
    user_profiles = UserProfile.objects.filter(specialty__id=created_course_specialty_id)
    if user_profiles:
        for prof in user_profiles:
            try:
                Result.objects.create(
                    student = prof,
                    course = created_course,
                )
            except:
                # raise Exception("COUSE EXIST ALREADY")
                pass


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
    date_assigned = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey(CustomUser, null=True, blank=True, related_name='course_lecturer', on_delete=models.SET_NULL)
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
    ca = models.CharField(max_length=4, null=True, blank=True)
    test = models.CharField(max_length=4, null=True, blank=True)
    exam = models.CharField(max_length=4, null=True, blank=True)
    resit = models.CharField(max_length=4, null=True, blank=True)
    average = models.CharField(max_length=4, null=True, blank=True)
    validated = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='result_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='result_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.student.user.first_name}-{self.course.main_course.course_name}"
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=["course", "student"], name="unique_result") ]
    