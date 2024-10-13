import django_filters
from .models import *


class DomainFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    domain_name = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = Domain
        fields = {
            'domain_name': [ "in", "exact" ]
        }


class SchoolIdentificationFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    code = django_filters.CharFilter(lookup_expr="icontains")
    name = django_filters.CharFilter(lookup_expr="icontains")
    back_end = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = SchoolIdentification
        fields = {}


class CampusFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    name = django_filters.CharFilter(lookup_expr="icontains")
    region = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = Campus
        fields = {
            'name': [ "icontain" ]
        }


class SchoolInfoFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    school_name = django_filters.CharFilter(lookup_expr="icontains")
    school_name_short = django_filters.CharFilter(lookup_expr="icontains")
    campus__region = django_filters.CharFilter(lookup_expr="icontains")
    director = django_filters.CharFilter(lookup_expr="icontains")
    campus__name = django_filters.CharFilter(lookup_expr="icontains")
    campus__id = django_filters.CharFilter(lookup_expr="exact")
    class meta:
        model = SchoolInfo


class FieldFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    domain__id = django_filters.CharFilter(lookup_expr="exact")
    domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = Field
        fields = {
            'field_name': [ "in", "exact" ]
        }


class MainSpecialtyFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    field__domain__id = django_filters.CharFilter(lookup_expr="exact")
    field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    field__id = django_filters.CharFilter(lookup_expr="exact")
    field__field_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty_name_short = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = MainSpecialty


class SpecialtyFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    main_specialty__field__domain__id = django_filters.CharFilter(lookup_expr="exact")
    main_specialty__field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    main_specialty__field__id = django_filters.CharFilter(lookup_expr="exact")
    main_specialty__field__field_name = django_filters.CharFilter(lookup_expr="icontains")
    main_specialty__id = django_filters.CharFilter(lookup_expr="exact")
    main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    academic_year = django_filters.CharFilter(lookup_expr="icontains")
    level__level = django_filters.CharFilter(lookup_expr="exact")
    tuition = django_filters.CharFilter(lookup_expr="icontains")
    level__id = django_filters.CharFilter(lookup_expr="exact")
    school__id = django_filters.CharFilter(lookup_expr="exact")
    school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    school__campus__region = django_filters.CharFilter(lookup_expr="icontain")
    school__campus__name = django_filters.CharFilter(lookup_expr="icontain")
    class meta:
        model = Specialty


class MainCourseFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    course_name = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = MainCourse


class CourseFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    main_course__id = django_filters.CharFilter(lookup_expr="exact")
    main_course__course_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__main_specialty__field__domain__id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__main_specialty__field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    specialty__school__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__level__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__level__level = django_filters.CharFilter(lookup_expr="exact")
    specialty__school__campus__region = django_filters.CharFilter(lookup_expr="exact")
    specialty__school__campus__name = django_filters.CharFilter(lookup_expr="exact")
    assigned_to__id = django_filters.CharFilter(lookup_expr="exact")
    course_code = django_filters.CharFilter(lookup_expr="exact")
    course_type = django_filters.CharFilter(lookup_expr="exact")
    semester = django_filters.CharFilter(lookup_expr="exact")
    course_credit = django_filters.CharFilter(lookup_expr="icontains")
    completed = django_filters.BooleanFilter()
    assigned = django_filters.BooleanFilter()
    paid = django_filters.BooleanFilter()
    hours = django_filters.CharFilter(lookup_expr="iexact")
    hours_left = django_filters.CharFilter(lookup_expr="iexact")
    assigned_to = django_filters.CharFilter(lookup_expr="exact")

    class meta:
        model = Course


class ResultFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    student__id = django_filters.CharFilter(lookup_expr="exact")
    student__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    student__user__matricle = django_filters.CharFilter(lookup_expr="iexact")
    student__user__telephone = django_filters.CharFilter(lookup_expr="icontains")
    student__specialty__id = django_filters.CharFilter(lookup_expr="exact")
    course__id = django_filters.CharFilter(lookup_expr="exact")
    course__specialty__id = django_filters.CharFilter(lookup_expr="exact")
    course__specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    course__specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    course__course_code = django_filters.CharFilter(lookup_expr="exact")
    course__course_type = django_filters.CharFilter(lookup_expr="exact")
    course__semester = django_filters.CharFilter(lookup_expr="exact")
    course__completed = django_filters.BooleanFilter()
    course__paid = django_filters.BooleanFilter()
    course__assigned_to = django_filters.CharFilter(lookup_expr="exact")
    course__assigned_to__full_name = django_filters.CharFilter(lookup_expr="icontains")
    publish_ca = django_filters.BooleanFilter()
    publish_exam = django_filters.BooleanFilter()
    publish_resit = django_filters.BooleanFilter()
    closed = django_filters.BooleanFilter()
    active = django_filters.BooleanFilter()
    class meta:
        model = Result
        fields = {
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }


class PublishFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    specialty__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__main_specialty__field__domain__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    specialty__school__id = django_filters.NumberFilter(lookup_expr="exact")
    semester = django_filters.CharFilter(lookup_expr="iexact")
    ca = django_filters.BooleanFilter()
    exam = django_filters.BooleanFilter()
    resit = django_filters.BooleanFilter()
    portal_ca = django_filters.BooleanFilter()
    portal_exam = django_filters.BooleanFilter()
    portal_resit = django_filters.BooleanFilter()
    class meta:
        model = Publish


class LevelFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    level = django_filters.CharFilter(lookup_expr="iexact")

    class meta:
        model = Level


class SysCategoryFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    name = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = SysCategory


class SysConstantFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    name = django_filters.CharFilter(lookup_expr="icontains")
    sys_category__id = django_filters.NumberFilter(lookup_expr="exact")
    sys_category__name = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = SysConstant

        
        