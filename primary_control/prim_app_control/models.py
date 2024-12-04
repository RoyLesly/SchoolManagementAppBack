from django.db import models
from django.db.models.signals import post_save, pre_save
from higher_control.user_control.models import CustomUser
from higher_control.user_control.choices import *
from datetime import date, datetime
from django.utils import timezone
from higher_control.app_control.models import SchoolInfoHigher
from .choices import *



class PrimaryLevel(models.Model):
    level = models.CharField(max_length=15, choices=PRIMARY_LEVEL_CHOICES, null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_level_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_level_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("created_at",)
        constraints = [ 
            models.UniqueConstraint(fields=["level"], name="unique_Primary_level")
        ]

    def __str__(self):
        return f"{self.level} - {self.option}"
    

class PrimaryClassRoom(models.Model):
    school = models.ForeignKey(SchoolInfoHigher, null=False, related_name='Primary_classroom_school_info', on_delete=models.PROTECT)
    level = models.ForeignKey(PrimaryLevel, null=False, related_name='classroom_level', on_delete=models.PROTECT)
    academic_year = models.CharField(max_length=9, blank=False, unique=False)
    assigned_to = models.ForeignKey(CustomUser, null=True, blank=True, related_name='Primary_subject_lecturer', on_delete=models.SET_NULL)
    registration = models.IntegerField(default=0)
    tuition = models.IntegerField(default=0)
    payment_one = models.IntegerField(default=0)
    payment_two = models.IntegerField(default=0)
    payment_three = models.IntegerField(default=0)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_classroom_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_classroom_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        constraints = [ 
            models.UniqueConstraint(fields=["school", "level", "academic_year"], name="unique_Primary_classroom")
        ]
    def __str__(self):
        return f"{self.level.level} {self.level.option}-{self.academic_year}"


class PrimaryMainSubject(models.Model):
    subject_name = models.CharField(max_length=50, blank=False, unique=True)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_main_subject_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_main_subject_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.subject_name}"


class PrimarySubject(models.Model):
    main_subject = models.ForeignKey(PrimaryMainSubject, null=True, related_name='Primary_subject_main_subject', on_delete=models.PROTECT)
    classroom = models.ForeignKey(PrimaryClassRoom, null=True, related_name='Primary_subject_class', on_delete=models.PROTECT)
    subject_code = models.CharField(max_length=10, blank=False)
    subject_coefficient = models.IntegerField(blank=False)
    assigned = models.BooleanField(default=False)
    date_assigned = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_subject_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_subject_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.main_subject}-{self.classroom}"
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=["classroom", "main_subject"], name="unique_Primary_subject") ]
    
# post_save.connect(create_result_from_subject, sender=PrimarySubject)


# class PrimaryResult(models.Model):
#     student = models.ForeignKey(PrimaryProfile, null=True, related_name='result_Primaryprofile', on_delete=models.PROTECT)
#     subject = models.ForeignKey(PrimarySubject, null=True, related_name='result_Primary_subject', on_delete=models.PROTECT)
#     seq_1 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     seq_2 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     seq_3 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     seq_4 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     seq_5 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     seq_6 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#     average_term_1 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
#     average_term_2 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
#     average_term_3 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
#     passed_1 = models.BooleanField(default=False)
#     passed_2 = models.BooleanField(default=False)
#     passed_3 = models.BooleanField(default=False)
#     publish_seq_1 = models.BooleanField(default=False)
#     publish_seq_2 = models.BooleanField(default=False)
#     publish_seq_3 = models.BooleanField(default=False)
#     publish_seq_4 = models.BooleanField(default=False)
#     publish_seq_5 = models.BooleanField(default=False)
#     publish_seq_6 = models.BooleanField(default=False)
#     publish_term_1 = models.BooleanField(default=False)
#     publish_term_2 = models.BooleanField(default=False)
#     publish_term_3 = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
#     created_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_result_created_by', on_delete=models.SET_NULL)
#     created_at = models.DateField(auto_now_add=True)
#     updated_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_result_updated_by', on_delete=models.SET_NULL)
#     updated_at = models.DateField(auto_now=True)

#     def __str__(self):
#         return f"{self.id} {self.student.user.first_name}-{self.subject.main_subject.subject_name}"
    
#     class Meta:
#         constraints = [ models.UniqueConstraint(fields=["subject", "student"], name="unique_Primary_result") ]
        
#     def calculate_average(self):
#         print(111111111111111111111111111111111)
#         def av(a, b):
#             print(a, b)
#             if a != None:
#                 if b != None:
#                     return (a + b)/2
#                 return a
#             if b != None:
#                 return b
#         try:
#             self.average_term_1 = av(self.seq_1, self.seq_2)
#             if (self.average_term_1 > 9.99):
#                 self.passed_1 = True 
#             else:
#                 self.passed_1 = False 
#         except: 
#             pass
#         try:
#             self.average_term_2 = av(self.seq_3, self.seq_4)
#             if (self.average_term_2 > 9.99):
#                 self.passed_2 = True 
#             else:
#                 self.passed_2 = False 
#         except: 
#             pass
#         try:
#             self.average_term_3 = av(self.seq_5, self.seq_6)
#             if (self.average_term_3 > 9.99):
#                 self.passed_3 = True 
#             else:
#                 self.passed_3 = False 
#         except: 
#             pass

#     def save(self, *args, **kwargs):       
#         self.calculate_average()        
#         super(PrimaryResult, self).save(*args, **kwargs)


# post_save.connect(create_publish_from_result, sender=PrimaryResult)
    

# class PrimaryPublish(models.Model):
#     classroom = models.ForeignKey(PrimaryClassRoom, null=True, related_name='publish_Primary_classroom', on_delete=models.PROTECT)
#     publish_type = models.CharField(max_length=15, choices=PUBLISH_TYPE_CHOICES, null=False, blank=False, default="I")
#     publish_item = models.CharField(max_length=15, choices=PUBLISH_ITEM_CHOICES, null=False, blank=False, default="I")
#     publish = models.BooleanField(default=False)
#     portal = models.BooleanField(default=True)

#     created_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_publish_created_by', on_delete=models.SET_NULL)
#     created_at = models.DateField(auto_now_add=True)
#     updated_by = models.ForeignKey(CustomUser, null=True, related_name='Primary_publish_updated_by', on_delete=models.SET_NULL)
#     updated_at = models.DateField(auto_now=True)

#     def __str__(self):
#         return f"{self.id} {self.classroom}-{self.publish_type}-{self.publish_item}"
    
#     class Meta:
#         constraints = [ models.UniqueConstraint(fields=["classroom", "publish_type", "publish_item"], name="unique_Primarypublish") ]

# post_save.connect(update_results_from_publish, sender=PrimaryPublish)
