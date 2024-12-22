from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *


class GetTimeTableWeekSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="specialty.main_specialty.field.domain.domain_name", read_only=True)
    specialty_id = serializers.IntegerField(source="specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="specialty.main_specialty.specialty_name", read_only=True)
    school_id = serializers.IntegerField(source="specialty.school.id", read_only=True)
    campus = serializers.CharField(source="specialty.school.campus", read_only=True)
    region = serializers.CharField(source="specialty.school.region", read_only=True)
    level = serializers.IntegerField(source="specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="specialty.academic_year", read_only=True)

    year_week = serializers.IntegerField(write_only=True, required=False)
    publish = serializers.BooleanField(write_only=True, required=False)

    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
       

    class Meta:
        model = TimeTableWeek
        fields = [
            'id', 
            'domain_id', 'domain_name', 'specialty_id','specialty_name', 'school_id', 'campus', 'region', 'level', 'academic_year',
            'year_week', 
            'publish', 
            
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",  
        ]


class GetTimeTableDaySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="timetableweek.specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="timetableweek.specialty.main_specialty.field.domain.domain_name", read_only=True)
    specialty_id = serializers.IntegerField(source="timetableweek.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="timetableweek.specialty.main_specialty.specialty_name", read_only=True)
    school_id = serializers.IntegerField(source="timetableweek.specialty.school.id", read_only=True)
    campus = serializers.CharField(source="timetableweek.specialty.school.campus", read_only=True)
    region = serializers.CharField(source="timetableweek.specialty.school.region", read_only=True)
    level = serializers.IntegerField(source="timetableweek.specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="timetableweek.specialty.academic_year", read_only=True)
    
    date = serializers.DateField(read_only=True)
    day = serializers.CharField(read_only=True)

    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
           
    
    class Meta:
        model = TimeTableDay
        fields = [
            'id', 
            'domain_id', 'domain_name', 'specialty_id','specialty_name', 'school_id', 'campus', 'region', 'level', 'academic_year',
            'date', 
            'day', 
            
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",  
        ]


class GetTimeSlotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    domain_id = serializers.IntegerField(source="timetableday.timetableweek.specialty.main_specialty.field.domain.id", read_only=True)
    domain_name = serializers.CharField(source="timetableday.timetableweek.specialty.main_specialty.field.domain.domain_name", read_only=True)
    specialty_id = serializers.IntegerField(source="timetableday.timetableweek.specialty.id", read_only=True)
    specialty_name = serializers.CharField(source="timetableday.timetableweek.specialty.main_specialty.specialty_name", read_only=True)
    school_id = serializers.IntegerField(source="timetableday.timetableweek.specialty.school.id", read_only=True)
    campus = serializers.CharField(source="timetableday.timetableweek.specialty.school.campus", read_only=True)
    level = serializers.IntegerField(source="timetableday.timetableweek.specialty.level.level", read_only=True)
    academic_year = serializers.CharField(source="timetableday.timetableweek.specialty.academic_year", read_only=True)
    date = serializers.DateField(source="timetableday.date", read_only=True)
    day = serializers.CharField(source="timetableday.day", read_only=True)
    
    course_id = serializers.CharField(source="course.id", read_only=True)
    course_name = serializers.CharField(source="course.main_course.course_name", read_only=True)
    assigned_to_id = serializers.IntegerField(source="course.assigned_to.id", read_only=True)
    assigned_to_full_name = serializers.CharField(source="course.assigned_to.full_name", read_only=True)
    course_hours = serializers.IntegerField(source="course.hours", read_only=True)
    course_hours_left = serializers.IntegerField(source="course.hours_left", read_only=True)
    
    title = serializers.CharField(read_only=True)
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)
    action = serializers.CharField(read_only=True)

    start_time = serializers.DateField(read_only=True)
    end_time = serializers.DateField(read_only=True)
    duration = serializers.DateField(read_only=True)
    hours = serializers.DateField(read_only=True)
    session = serializers.DateField(read_only=True)

    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)
    created_by_full_name = serializers.CharField(source='created_by.full_name', read_only=True)
    updated_by_full_name = serializers.CharField(source='updated_by.full_name', read_only=True)
           
    
    class Meta:
        model = TimeSlot
        fields = [
            'id', 
            'domain_id', 'domain_name', 'specialty_id','specialty_name', 'school_id', 'campus', 'level', 'academic_year',
            'date', 'day', 
            'course_id', 'course_name', 'assigned_to_id', 'assigned_to_full_name', 'course_hours', 'course_hours_left',
            'title', 'start', 'end', 'status', 'action', 
            'start_time', 'end_time', 'duration', 'hours', 'session', 
            
            'created_by_id',
            "updated_by_id",
            'created_by_full_name',
            "updated_by_full_name",  
        ]

