from rest_framework import serializers
from .models import *


class TimeTableWeekSerializer(serializers.ModelSerializer):
    specialty_id = serializers.IntegerField(write_only=True, required=False)
    created_id = serializers.IntegerField(write_only=True, required=False)
    updated_by_id = serializers.IntegerField(write_only=True, required=False)
  

    class Meta:
        model = TimeTableWeek
        fields = "__all__"


class TimeTableDaySerializer(serializers.ModelSerializer):
    timetableweek_id = serializers.IntegerField(write_only=True, required=False)
    created_id = serializers.IntegerField(write_only=True, required=False)
    updated_by_id = serializers.IntegerField(write_only=True, required=False)
  
    class Meta:
        model = TimeTableDay
        fields = "__all__"


class TimeSlotSerializer(serializers.ModelSerializer):
    timetableday_id = serializers.IntegerField(write_only=True, required=False)
    course_id = serializers.IntegerField(write_only=True, required=False)
    created_id = serializers.IntegerField(write_only=True, required=False)
    updated_by_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = TimeSlot
        fields = '__all__'

