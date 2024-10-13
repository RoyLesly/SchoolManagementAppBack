from django.db import models
from higher_control.user_control.models import CustomUser
from higher_control.app_control.models import Specialty, Course
from django.db.models.signals import post_save
from higher_control.user_control.choices import SESSION_CHOICES
from .functions import *
from .choices import *
import math, pytz
from django.db.models.signals import post_save, pre_save
from datetime import datetime, date

# datetime object containing current date and time
now = datetime.now(pytz.timezone('Africa/Douala'))
today = date.today()


DAY_CHOICES = (
    ("MONDAY", "MONDAY"), ("TUESDAY", "TUESDAY"), ("WEDNESDAY", "WEDNESDAY"), 
    ("THURSDAY", "THURSDAY"), ("FRIDAY", "FRIDAY"), ("SATURDAY", "SATURDAY"), ("SUNDAY", "SUNDAY"),
)

class TimeTableWeek(models.Model):
    year_week = models.CharField(max_length=7, null=False, blank=False, unique=False)
    specialty = models.ForeignKey(Specialty, null=False, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)

    created_by = models.ForeignKey(CustomUser, null=True, related_name='timetableweek_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='timetableweek_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.year_week}-{self.specialty.main_specialty.specialty_name[0: 10]}-{self.specialty.academic_year}-{self.specialty.level.level}"

    class Meta:
        constraints = [ 
            models.UniqueConstraint(fields=["specialty", "year_week"], name="unique_timetableweek")
        ]


class TimeTableDay(models.Model):
    timetableweek = models.ForeignKey(TimeTableWeek, null=True, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    day = models.CharField(max_length=15, choices=DAY_CHOICES, blank=False)

    created_by = models.ForeignKey(CustomUser, null=True, related_name='timetableday_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}-{self.timetableweek.year_week}"
    
    class Meta:
        constraints = [ 
            models.UniqueConstraint(fields=["day", "timetableweek"], name="unique_timetableday")
        ]


class TimeSlot(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True, related_name='timeslot_course', on_delete=models.CASCADE)
    timetableday = models.ForeignKey(TimeTableDay, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False, blank=False)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=TIMESLOT_CHOICES, null=False, blank=False, default="I")
    action = models.CharField(max_length=15, choices=TIMESLOT_ACTIONS, null=False, blank=False, default="PENDING")

    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    session = models.CharField(max_length=15, choices=SESSION_CHOICES, default="Morning")

    created_by = models.ForeignKey(CustomUser, null=True, related_name='timeslot_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='timeslot_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)
   
    def __str__(self):
        return f"{self.timetableday.day}-{self.title}"
    
    class Meta:
        constraints = [ 
            models.UniqueConstraint(fields=["start", "timetableday"], name="unique_timeslot")
        ]
    def update_time(self):
        if self.action == "IN":
            self.start_time = now.time()
        if self.action == "OUT":
            self.end_time = now.time
            diff = datetime.combine(today, self.end_time) - datetime.combine(today, self.start_time)
            # diff = datetime.combine(today, self.end_time) - datetime.combine(today, self.start_time)
            self.duration = diff
            time_slot_hours = math.ceil(((self.end - self.start).total_seconds()/3600) * 4) / 4
            hours_taught = math.ceil((diff.total_seconds()/3600) * 4) / 4
            if time_slot_hours < hours_taught:
                self.hours = time_slot_hours
            else:
                self.hours = hours_taught
        if self.action == "OUT-BY-SYSTEM":
            self.end_time = now

def create_title(sender, created, instance, *args, **kwargs):
    if created:
        if instance.title:
            pass
        else: 
            instance.title = instance.course.main_course.course_name
            instance.save()

def other_actions(sender, instance, *args, **kwargs):
    instance.update_time()

pre_save.connect(other_actions, sender=TimeSlot)
post_save.connect(create_title, sender=TimeSlot)
post_save.connect(update_course_hours_left, sender=TimeSlot)



