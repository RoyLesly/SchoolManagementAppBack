from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *
from higher_control.user_control.serializers import CustomUserSerializer, GetCustomUserSerializer
from higher_control.app_control.serializers import SpecialtySerializer, CourseSerializer
from higher_control.user_control.models import UserProfile, Program


class TimeTableWeekSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=False)
    year_week = serializers.CharField(write_only=True, required=False)
    publish = serializers.BooleanField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = TimeTableWeek
        fields = "__all__"


class TimeTableDaySerializer(serializers.ModelSerializer):
    timetableweek = TimeTableWeekSerializer(read_only=True)
    timetableweek_id = serializers.CharField(write_only=True, required=False)
    date = serializers.CharField(write_only=True, required=False)
    day = serializers.CharField(write_only=True, required=False)

    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = TimeTableDay
        fields = "__all__"


class TimeSlotSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True, required=False)
    timetableday = TimeTableDaySerializer(read_only=True)
    timetableday_id = serializers.IntegerField(write_only=True, required=False)
    title = serializers.CharField(write_only=True, required=False)
    start = serializers.DateTimeField(write_only=True, required=False)
    end = serializers.DateTimeField(write_only=True, required=False)
    start_time = serializers.TimeField(write_only=True, required=False)
    end_time = serializers.TimeField(write_only=True, required=False)
    hours = serializers.CharField(write_only=True, required=False)
    session = serializers.CharField(write_only=True, required=False)

    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.IntegerField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = TimeSlot
        fields = "__all__"



# LIST SERIALIZERS =======================================================================================================


class GetTimeTableWeekSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    specialty__id = serializers.IntegerField(read_only=True)
    specialty__level__level = serializers.CharField(read_only=True)
    specialty__academic_year = serializers.CharField(read_only=True)
    specialty__session = serializers.CharField(read_only=True)
    specialty__main_specialty__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    specialty__main_specialty__field__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__field__field_name = serializers.CharField(read_only=True)
    specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    year_week = serializers.CharField(read_only=True)
    publish = serializers.BooleanField(read_only=True)

    created_by__id = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__id = serializers.IntegerField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetTimeTableDaySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    day = serializers.CharField(read_only=True)
    timetableweek__id = serializers.CharField(read_only=True)
    timetableweek__specialty__id = serializers.IntegerField(read_only=True)
    timetableweek__specialty__level__level = serializers.CharField(read_only=True)
    timetableweek__specialty__academic_year = serializers.CharField(read_only=True)
    timetableweek__specialty__session = serializers.CharField(read_only=True)
    timetableweek__specialty__main_specialty__id = serializers.IntegerField(read_only=True)
    timetableweek__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    timetableweek__specialty__main_specialty__field__id = serializers.IntegerField(read_only=True)
    timetableweek__specialty__main_specialty__field__field_name = serializers.CharField(read_only=True)
    timetableweek__specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    timetableweek__specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    timetableweek__year_week = serializers.CharField(read_only=True)
    timetableweek__publish = serializers.BooleanField(read_only=True)

    created_by__id = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__id = serializers.IntegerField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetTimeSlotSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course__id = serializers.IntegerField(read_only=True)
    course__main_course__id = serializers.IntegerField(read_only=True)
    course__main_course__course_name = serializers.CharField(read_only=True)
    course__assigned_to__id = serializers.CharField(read_only=True)
    course__assigned_to__full_name = serializers.CharField(read_only=True)
    course__hours = serializers.IntegerField(read_only=True)
    course__hours_left = serializers.IntegerField(read_only=True)

    timetableday__id = serializers.IntegerField(read_only=True)
    timetableday__day = serializers.CharField(read_only=True)
    timetableday__date = serializers.CharField(read_only=True)

    title = serializers.CharField(read_only=True)
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField(read_only=True)
    start_time = serializers.CharField(read_only=True)
    end_time = serializers.CharField(read_only=True)
    hours = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    session = serializers.CharField(read_only=True)

    timetableday__timetableweek__id = serializers.CharField(read_only=True)
    timetableday__timetableweek__specialty__id = serializers.IntegerField(read_only=True)
    timetableday__timetableweek__specialty__level__level = serializers.CharField(read_only=True)
    timetableday__timetableweek__specialty__academic_year = serializers.CharField(read_only=True)
    timetableday__timetableweek__specialty__session = serializers.CharField(read_only=True)
    timetableday__timetableweek__specialty__main_specialty__id = serializers.IntegerField(read_only=True)
    timetableday__timetableweek__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    timetableday__timetableweek__specialty__main_specialty__field__id = serializers.IntegerField(read_only=True)
    timetableday__timetableweek__specialty__main_specialty__field__field_name = serializers.CharField(read_only=True)
    timetableday__timetableweek__specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    timetableday__timetableweek__specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    timetableday__timetableweek__year_week = serializers.CharField(read_only=True)
    timetableday__timetableweek__publish = serializers.BooleanField(read_only=True)
    

    created_by__id = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__id = serializers.IntegerField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)

