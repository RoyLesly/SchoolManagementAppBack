import django_filters
from .models import *


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = Department
        fields = {
            'id': [ "exact" ],
        }


class PageFilter(django_filters.FilterSet):
    class meta:
        model = Page
        fields = {
            'id': [ "exact" ],
            'name': [ "in", "exact" ]
        }


class ProgramFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = Program
        

class UserProfileFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    user__id = django_filters.CharFilter(lookup_expr="exact")
    user__matricle = django_filters.CharFilter(lookup_expr="icontains")
    user__username = django_filters.CharFilter(lookup_expr="icontains")
    user__first_name = django_filters.CharFilter(lookup_expr="icontains")
    user__last_name = django_filters.CharFilter(lookup_expr="icontains")
    user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    user__role = django_filters.CharFilter(lookup_expr="iexact")
    user__sex = django_filters.CharFilter(lookup_expr="iexact")
    user__is_active = django_filters.BooleanFilter()
    user__is_superuser = django_filters.BooleanFilter()
    user__email = django_filters.CharFilter(lookup_expr="icontains")
    user__dob = django_filters.CharFilter(lookup_expr="iexact")
    user__last_login = django_filters.CharFilter(lookup_expr="iexact")
    user__telephone = django_filters.CharFilter(lookup_expr="icontains")
    user__school__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__main_specialty__field__domain__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    specialty__level__level = django_filters.CharFilter(lookup_expr="iexact")
    specialty__level__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__school__id = django_filters.CharFilter(lookup_expr="exact")
    specialty__school__campus__region = django_filters.CharFilter(lookup_expr="icontains")
    specialty__school__campus__name = django_filters.CharFilter(lookup_expr="icontains")
    specialty__school__campus__id = django_filters.CharFilter(lookup_expr="exact")

    nospecialty = django_filters.BooleanFilter(field_name='specialty', lookup_expr='isnull')

    class meta:
        model = UserProfile
        fields = {
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }



class CustomUserFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    matricle = django_filters.CharFilter(lookup_expr="icontains")
    username = django_filters.CharFilter(lookup_expr="icontains")
    full_name = django_filters.CharFilter(lookup_expr="icontains")
    role = django_filters.CharFilter(lookup_expr="icontains")
    is_active = django_filters.BooleanFilter()
    is_staff = django_filters.BooleanFilter()
    is_superuser = django_filters.BooleanFilter()
    email = django_filters.CharFilter(lookup_expr="icontains")
    dob = django_filters.CharFilter(lookup_expr="iexact")
    last_login = django_filters.CharFilter(lookup_expr="iexact")
    telephone = django_filters.CharFilter(lookup_expr="icontains")
    school__id = django_filters.CharFilter(lookup_expr="exact")
    school__campus__region = django_filters.CharFilter(lookup_expr="icontains")
    admin = django_filters.CharFilter(field_name='role', lookup_expr='icontains')
    teacher = django_filters.CharFilter(field_name='role', lookup_expr='icontains')
    student = django_filters.CharFilter(field_name='role', lookup_expr='icontains')

    nostudent = django_filters.BooleanFilter(field_name='role', lookup_expr='icontains')

    class meta:
        model = CustomUser
        fields = {
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }


class PreInscriptionFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    registration_number = django_filters.CharFilter(lookup_expr="icontains")
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    full_name = django_filters.CharFilter(lookup_expr="icontains")
    sex = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    telephone = django_filters.CharFilter(lookup_expr="icontains")
    address = django_filters.CharFilter(lookup_expr="icontains")
    pob = django_filters.CharFilter(lookup_expr="icontains")
    dob = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(lookup_expr="icontains")
    emergency_name = django_filters.CharFilter(lookup_expr="icontains")
    emergency_town = django_filters.CharFilter(lookup_expr="icontains")
    emergency_telephone = django_filters.CharFilter(lookup_expr="icontains")
    academic_year = django_filters.CharFilter(lookup_expr="icontains")
    program = django_filters.CharFilter(lookup_expr="icontains")
    campus = django_filters.CharFilter(lookup_expr="icontains")
    level = django_filters.CharFilter(lookup_expr="icontains")
    session = django_filters.CharFilter(lookup_expr="icontains")
    specialty_one = django_filters.CharFilter(lookup_expr="icontains")
    specialty_two = django_filters.CharFilter(lookup_expr="icontains")
    addmission_status = django_filters.BooleanFilter(lookup_expr="exact")
    action = django_filters.BooleanFilter(lookup_expr="icontains")
    created_at = django_filters.CharFilter(lookup_expr="icontains")
    updated_at = django_filters.CharFilter(lookup_expr="icontains")
  
    class meta:
        model = PreInscription
        fields = {
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }


class AppearanceFilter(django_filters.FilterSet):
    user__id = django_filters.CharFilter(lookup_expr="exact")
    dark_mode = django_filters.CharFilter(lookup_expr="icontains")
    lang = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = Appearance
        fields = {
            'id': [ "exact" ],
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }
