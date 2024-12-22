from django.db import models
from django.db.models.signals import post_save
from higher_control.user_control.models import CustomUser, UserProfile
from higher_control.user_control.choices import SEMESTER_CHOICES, COURSE_TYPE_CHOICES
from django.core.exceptions import ValidationError
from .functions import *
from .choices import *
from tenant.models import *



def upload_to(instance, filename):
    return f"uploads/{filename}"


class SchoolIdentificationHigher(SchoolIdentification):

    def __str__(self):
        return f"{self.code}-{self.status}"
    
    class Meta:
        ordering = ("created_at",)

         
class SchoolInfoHigher(Setting):
    campus = models.CharField(max_length=15, choices=CAMPUS_CHOICES, null=False, blank=False, default="Campus-A")
    school_identification = models.ForeignKey(SchoolIdentificationHigher, related_name='schoolinfo_schoolidentification', on_delete=models.PROTECT)
    ca_limit = models.IntegerField(blank=False, null=False, default=30)
    exam_limit = models.IntegerField(blank=False, null=False, default=70)
    resit_limit = models.IntegerField(blank=False, null=False, default=70)
    bg_logo_transcript = models.ImageField(upload_to='transcript_higher/', null=True, blank=True)
    bg_logo_slip = models.ImageField(upload_to='slip_higher/', null=True, blank=True)
    colors = models.CharField(max_length=255, blank=False, null=False, default="bg-teal-700, bg-teal-700")

    def __str__(self):
        return f"{self.campus} {self.short_name}"

    class Meta:
        ordering = ("created_at",)

    constraints = [
        models.UniqueConstraint(fields=["campus", "region"], name="unique_school_campus_region"),
    ]
    

class Domain(CreatedUpdatedModel):
    domain_name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} {self.domain_name}"


class Field(CreatedUpdatedModel):
    field_name = models.CharField(max_length=50, blank=False, unique=True)
    domain = models.ForeignKey(Domain, null=True, related_name='field_domain', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.field_name}"


class MainSpecialty(CreatedUpdatedModel):
    specialty_name = models.CharField(max_length=100, unique=True)
    specialty_name_short = models.CharField(max_length=5, default="Edit")
    field = models.ForeignKey(Field, null=True, on_delete=models.PROTECT, related_name='specialties')

    def __str__(self):
        return self.specialty_name


class Level(CreatedUpdatedModel):
    level = models.IntegerField(unique=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.level}"
    

class Specialty(CreatedUpdatedModel):
    school = models.ForeignKey(SchoolInfoHigher, on_delete=models.PROTECT, related_name='specialties')
    main_specialty = models.ForeignKey(MainSpecialty, on_delete=models.PROTECT, related_name='specialties')
    level = models.ForeignKey(Level, on_delete=models.PROTECT, related_name='specialties')
    academic_year = models.CharField(max_length=9)
    tuition = models.PositiveIntegerField(default=0)
    registration = models.PositiveIntegerField(default=0)
    payment_one = models.PositiveIntegerField(default=0)
    payment_two = models.PositiveIntegerField(default=0)
    payment_three = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "main_specialty", "academic_year", "level"], name="unique_specialty")
        ]

    def __str__(self):
        return f"{self.main_specialty.specialty_name}-L{self.level.level}-{self.academic_year} {self.school.campus}"

post_save.connect(create_publish_from_specialty, sender=Specialty)


class MainCourse(CreatedUpdatedModel):
    course_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Course: {self.course_name}"


class Course(CreatedUpdatedModel):
    main_course = models.ForeignKey(MainCourse, on_delete=models.PROTECT, related_name='courses')
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='courses')
    course_code = models.CharField(max_length=10)
    course_type = models.CharField(max_length=15, choices=COURSE_TYPE_CHOICES, default="Fundamental")
    semester = models.CharField(max_length=15, choices=SEMESTER_CHOICES, default="I")
    course_credit = models.IntegerField()
    completed = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    hours = models.IntegerField(default=0)
    hours_left = models.DecimalField(max_digits=5, decimal_places=2)
    date_assigned = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.PROTECT, related_name='courses')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["specialty", "main_course"], name="unique_course")
        ]

    def __str__(self):
        return f"{self.course_code} - {self.main_course.course_name} ({self.specialty})"

# Signal connections should be added after model class definitions.
post_save.connect(create_result_from_course, sender=Course)


class CourseUpload(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='uploads')
    file = models.FileField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        allowed_extensions = ['pdf', 'doc', 'docx']
        ext = self.file.name.split('.')[-1].lower()
        if ext not in allowed_extensions:
            raise ValidationError("Only PDF and Word documents are allowed.")

    def __str__(self):
        return self.title
    
    
class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='modules')
    module_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    files = models.ManyToManyField(CourseUpload, related_name='modules')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.module_title} - {self.course.main_course.course_name}"


class CourseModuleDetail(models.Model):
    course_module = models.ForeignKey(CourseModule, on_delete=models.PROTECT, related_name='details')
    detail_title = models.CharField(max_length=255)
    files = models.ManyToManyField(CourseUpload, related_name='details')
    description = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.detail_title} - {self.course_module.course.main_course.course_name}"

    
class Result(CreatedUpdatedModel):
    student = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='results')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='results')
    matricle = models.CharField(max_length=15, blank=True, null=True)
    ca = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    exam = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    resit = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    average = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["course", "student"], name="unique_result")
        ]

    def __str__(self):
        return f"{self.student.user.first_name} - {self.course.main_course.course_name}"

    def calculate_average(self):
        total = 0
        count = 0
        if self.ca:
            total += self.ca
            count += 1
        if self.exam and not self.resit:
            total += self.exam
            count += 1
        if self.resit:
            total += self.resit
            count += 1
        if count > 0:
            self.average = total
            self.validated = self.average >= 50


    def save(self, *args, **kwargs):
        self.matricle = self.student.user.matricle
        self.calculate_average()
        super().save(*args, **kwargs)

post_save.connect(create_publish_from_result, sender=Result)
    

class Publish(CreatedUpdatedModel):
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='publish')
    semester = models.CharField(max_length=15, choices=SEMESTER_CHOICES, default="I")
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
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["specialty", "semester"], name="unique_publish")
        ]

    def __str__(self):
        return f"Publish {self.specialty} - {self.semester}"

post_save.connect(update_results_from_publish, sender=Publish)


class SysCategory(CreatedUpdatedModel):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ("name",)


class SysConstant(CreatedUpdatedModel):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    sys_category = models.ForeignKey(SysCategory, null=True, related_name='sysconstant_sys_category', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}-{self.sys_category}"
    
    class Meta:
        ordering = ("name",)


