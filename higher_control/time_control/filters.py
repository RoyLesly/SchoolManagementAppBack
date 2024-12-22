from django_filters import rest_framework as filters
from .models import *


class TimeTableWeekFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr="icontains")
    domain_id = filters.NumberFilter(field_name="timetableweek.specialty.main_specialty.field.domain.id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="timetableweek.specialty.main_specialty.field.domain.domain_name", lookup_expr="icontains")
    specialty_id = filters.NumberFilter(field_name="timetableweek.specialty.id", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="timetableweek.specialty.main_specialty.specialty_name", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="timetableweek.specialty.school.id", lookup_expr="exact")
    campus = filters.CharFilter(field_name="timetableweek.specialty.school.campus", lookup_expr="icontains")
    region = filters.CharFilter(field_name="timetableweek.specialty.school.region", lookup_expr="icontains")
    level = filters.NumberFilter(field_name="timetableweek.specialty.level.level", lookup_expr="icontains")
    academic_year = filters.CharFilter(field_name="timetableweek.specialty.academic_year", lookup_expr="icontains")
    
    date = filters.DateFilter(lookup_expr="icontains")
    day = filters.CharFilter(lookup_expr="icontains")

    created_by_id = filters.NumberFilter(field_name='created_by.id', lookup_expr="icontains")
    updated_by_id = filters.NumberFilter(field_name='updated_by.id', lookup_expr="icontains")
    created_by_full_name = filters.CharFilter(field_name='created_by.full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by.full_name', lookup_expr="icontains")

    class meta:
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


class TimeTableDayFilter(filters.FilterSet):
    domain_id = filters.NumberFilter(field_name="timetableweek.specialty.main_specialty.field.domain.id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="timetableweek.specialty.main_specialty.field.domain.domain_name", lookup_expr="icontains")
    specialty_id = filters.NumberFilter(field_name="timetableweek.specialty.id", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="timetableweek.specialty.main_specialty.specialty_name", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="timetableweek.specialty.school.id", lookup_expr="exact")
    campus = filters.CharFilter(field_name="timetableweek.specialty.school.campus", lookup_expr="icontains")
    region = filters.CharFilter(field_name="timetableweek.specialty.school.region", lookup_expr="icontains")
    level = filters.NumberFilter(field_name="timetableweek.specialty.level.level", lookup_expr="icontains")
    academic_year = filters.CharFilter(field_name="timetableweek.specialty.academic_year", lookup_expr="icontains")
    
    date = filters.DateFilter(lookup_expr="icontains")
    day = filters.CharFilter(lookup_expr="icontains")

    created_by_id = filters.NumberFilter(field_name='created_by.id', lookup_expr="icontains")
    updated_by_id = filters.NumberFilter(field_name='updated_by.id', lookup_expr="icontains")
    created_by_full_name = filters.CharFilter(field_name='created_by.full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by.full_name', lookup_expr="icontains")
           
    
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


class TimeSlotFilter(filters.FilterSet):
    domain_id = filters.NumberFilter(field_name="timetableday.timetableweek.specialty.main_specialty.field.domain.id", lookup_expr="exact")
    domain_name = filters.CharFilter(field_name="timetableday.timetableweek.specialty.main_specialty.field.domain.domain_name", lookup_expr="icontains")
    specialty_id = filters.NumberFilter(field_name="timetableday.timetableweek.specialty.id", lookup_expr="exact")
    specialty_name = filters.CharFilter(field_name="timetableday.timetableweek.specialty.main_specialty.specialty_name", lookup_expr="icontains")
    school_id = filters.NumberFilter(field_name="timetableday.timetableweek.specialty.school.id", lookup_expr="exact")
    campus = filters.CharFilter(field_name="timetableday.timetableweek.specialty.school.campus", lookup_expr="icontains")
    level = filters.NumberFilter(field_name="timetableday.timetableweek.specialty.level.level", lookup_expr="icontains")
    academic_year = filters.CharFilter(field_name="timetableday.timetableweek.specialty.academic_year", lookup_expr="icontains")
    date = filters.DateFilter(field_name="timetableday.date", lookup_expr="icontains")
    day = filters.CharFilter(field_name="timetableday.day", lookup_expr="icontains")
    
    course_id = filters.CharFilter(field_name="course.id", lookup_expr="exact")
    course_name = filters.CharFilter(field_name="course.main_course.course_name", lookup_expr="icontains")
    assigned_to_id = filters.NumberFilter(field_name="course.assigned_to.id", lookup_expr="exact")
    assigned_to_full_name = filters.CharFilter(field_name="course.assigned_to.full_name", lookup_expr="icontains")
    course_hours = filters.NumberFilter(field_name="course.hours", lookup_expr="icontains")
    course_hours_left = filters.NumberFilter(field_name="course.hours_left", lookup_expr="icontains")
    
    title = filters.CharFilter(lookup_expr="icontains")
    start = filters.DateTimeFilter(lookup_expr="icontains")
    end = filters.DateTimeFilter(lookup_expr="icontains")
    status = filters.CharFilter(lookup_expr="icontains")
    action = filters.CharFilter(lookup_expr="icontains")

    start_time = filters.TimeFilter(lookup_expr="icontains")
    end_time = filters.TimeFilter(lookup_expr="icontains")
    duration = filters.DurationFilter(lookup_expr="icontains")
    hours = filters.NumberFilter(lookup_expr="icontains")
    session = filters.CharFilter(lookup_expr="icontains")

    created_by_id = filters.NumberFilter(field_name='created_by.id', lookup_expr="icontains")
    updated_by_id = filters.NumberFilter(field_name='updated_by.id', lookup_expr="icontains")
    created_by_full_name = filters.CharFilter(field_name='created_by.full_name', lookup_expr="icontains")
    updated_by_full_name = filters.CharFilter(field_name='updated_by.full_name', lookup_expr="icontains")
           
    
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
    
