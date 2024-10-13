import django_filters
from .models import *



class TimeTableWeekFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__level__level = django_filters.CharFilter(lookup_expr="icontains")
    specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    specialty__session = django_filters.CharFilter(lookup_expr="icontains")
    specialty__main_specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__main_specialty__field__id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__main_specialty__field__field_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__main_specialty__field__domain__id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__main_specialty__field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    year_week = django_filters.CharFilter(lookup_expr="icontains")
    publish = django_filters.BooleanFilter(lookup_expr="icontains")

    created_by__id = django_filters.NumberFilter(lookup_expr="exact")
    created_by__full_name = django_filters.CharFilter(lookup_expr="icontains")
    updated_by__id = django_filters.NumberFilter(lookup_expr="exact")
    updated_by__full_name = django_filters.CharFilter(lookup_expr="icontains")


    class meta:
        model = TimeTableWeek
        fields = {
        }


class TimeTableDayFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    date = django_filters.CharFilter(lookup_expr="icontains")
    day = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__id = django_filters.NumberFilter(lookup_expr="icontains")
    timetableweek__specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableweek__specialty__level__level = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__specialty__session = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__specialty__main_specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableweek__specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__specialty__main_specialty__field__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableweek__specialty__main_specialty__field__field_name = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__specialty__main_specialty__field__domain__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableweek__specialty__main_specialty__field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__year_week = django_filters.CharFilter(lookup_expr="icontains")
    timetableweek__publish = django_filters.BooleanFilter(lookup_expr="icontains")

    created_by__id = django_filters.NumberFilter(lookup_expr="exact")
    created_by__full_name = django_filters.CharFilter(lookup_expr="icontains")
    updated_by__id = django_filters.NumberFilter(lookup_expr="exact")
    updated_by__full_name = django_filters.CharFilter(lookup_expr="icontains")


    class meta:
        model = TimeTableDay
        fields = {
        }


class TimeSlotFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    course__id = django_filters.NumberFilter(lookup_expr="exact")
    course__specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    course__main_course__id = django_filters.NumberFilter(lookup_expr="exact")
    course__main_course__course_name = django_filters.CharFilter(lookup_expr="icontains")
    course__assigned_to__id = django_filters.NumberFilter(lookup_expr="exact")
    course__assigned_to__full_name = django_filters.CharFilter(lookup_expr="icontains")
    session = django_filters.CharFilter(lookup_expr="icontains")

    course__specialty__school__id = django_filters.NumberFilter(lookup_expr="exact")

    timetableday__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableday__day = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__date = django_filters.CharFilter(lookup_expr="icontains")

    title = django_filters.CharFilter(lookup_expr="icontains")
    start = django_filters.CharFilter(lookup_expr="icontains")
    end = django_filters.CharFilter(lookup_expr="icontains")
    start_time = django_filters.CharFilter(lookup_expr="icontains")
    end_time = django_filters.CharFilter(lookup_expr="icontains")
    hours = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(lookup_expr="icontains")
    session = django_filters.CharFilter(lookup_expr="icontains")

    timetableday__timetableweek__id = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableday__timetableweek__specialty__level__level = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__specialty__main_specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableday__timetableweek__specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__specialty__main_specialty__field__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableday__timetableweek__specialty__main_specialty__field__field_name = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__specialty__main_specialty__field__domain__id = django_filters.NumberFilter(lookup_expr="exact")
    timetableday__timetableweek__specialty__main_specialty__field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__year_week = django_filters.CharFilter(lookup_expr="icontains")
    timetableday__timetableweek__publish = django_filters.BooleanFilter(lookup_expr="icontains")
    

    created_by__id = django_filters.NumberFilter(lookup_expr="exact")
    created_by__full_name = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = TimeSlot
        fields = {
        }
    
