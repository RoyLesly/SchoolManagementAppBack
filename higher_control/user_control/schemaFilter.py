import django_filters
from .models import *


class CustomUserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id", lookup_expr="exact")
    matricle = django_filters.CharFilter(field_name="matricle", lookup_expr="icontains")
    full_name = django_filters.CharFilter(field_name="full_name", lookup_expr="icontains")
    school_id = django_filters.NumberFilter(field_name="school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="school__campus", lookup_expr="icontains")
    role = django_filters.CharFilter(field_name="role", lookup_expr="iexact")
    is_active = django_filters.BooleanFilter(field_name="is_active")
    
    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'),  # Sorting by full_name
        ('full_name', 'full_name'),  # Sorting by full_name
        ('matricle', 'matricle'),    # Sorting by username
    ))
    

    class Meta:
        model = CustomUser
        fields = ['id', 'matricle', 'email', 'sex', 'role', 'username', 'dob', 'school_id', 'campus', 'is_active', 'is_superuser', 'is_staff']


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    ordering = django_filters.OrderingFilter(fields=(
        ('name', 'name'), 
    ))

    class Meta:
        model = Department
        fields = ['id', 'name']


class ProgramFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    
    ordering = django_filters.OrderingFilter(fields=(
        ('name', 'name'), 
    ))

    class Meta:
        model = Program
        fields = ['id', 'name', 'description']


class UserProfileFilter(django_filters.FilterSet):
    session = django_filters.CharFilter(field_name="session", lookup_expr="icontains")
    user_id = django_filters.NumberFilter(field_name="user__id", lookup_expr="exact")
    matricle = django_filters.CharFilter(field_name="user__matricle", lookup_expr="icontains")
    full_name = django_filters.CharFilter(field_name="user__full_name", lookup_expr="icontains")
    sex = django_filters.CharFilter(field_name="user__sex", lookup_expr="iexact")
    telephone = django_filters.CharFilter(field_name="user__telephone", lookup_expr="icontains")
    role = django_filters.CharFilter(field_name="user__role", lookup_expr="icontains")
    specialty_id = django_filters.NumberFilter(field_name="specialty__id", lookup_expr="exact")
    specialty_name = django_filters.CharFilter(field_name="specialty__main_specialty__specialty_name", lookup_expr="icontains")
    domain_id = django_filters.NumberFilter(field_name="specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    field_id = django_filters.NumberFilter(field_name="specialty__main_specialty__field__id", lookup_expr="exact")
    field_name = django_filters.CharFilter(field_name="specialty__main_specialty__field__field_name", lookup_expr="icontains")
    school_id = django_filters.NumberFilter(field_name="specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="specialty__school__campus", lookup_expr="icontains")
    academic_year = django_filters.CharFilter(field_name="specialty__academic_year", lookup_expr="iexact")
    level_id = django_filters.NumberFilter(field_name="specialty__level__id", lookup_expr="exact")
    level = django_filters.NumberFilter(field_name="specialty__level__level", lookup_expr="exact")
    is_staff = django_filters.BooleanFilter(field_name="user__is_staff")
    is_active = django_filters.BooleanFilter(field_name="user__is_active")
    is_superuser = django_filters.BooleanFilter(field_name="user__is_superuser")
    last_login = django_filters.DateTimeFilter(field_name="last_login", lookup_expr="icontains")

    nospecialty = django_filters.BooleanFilter(field_name="specialty", lookup_expr="isnull")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('user__id', 'user_id'), 
        ('user__full_name', 'full_name'), 
        ('user__matricle', 'matricle'), 
        ('specialty__main_specialty__field__domain__domain_name', 'domain_name'), 
        ('specialty__academic_year', 'academic_year'), 
        ('specialty__level', 'level'), 
        ('specialty__main_specialty__specialty_name', 'specialty_name'), 
        ('program__name', 'program_name'), 
    ))

    class Meta:
        model = UserProfile
        fields = [
            'id', 'session', 'user_id', 'matricle', 'full_name', 'sex', 'telephone', 'role', 
            'specialty_id', 'specialty_name', 'domain_id', 'domain_name', 'field_id', 'field_name', 'school_id',
            'campus', 'academic_year', 'level_id', 'level', 'is_staff', 'is_superuser', 'last_login'
        ]


class PreInscriptionFilter(django_filters.FilterSet):
    registration_number = django_filters.CharFilter(field_name="registration_number", lookup_expr="icontains")
    first_name = django_filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    full_name = django_filters.CharFilter(field_name="full_name", lookup_expr="icontains")
    telephone = django_filters.CharFilter(field_name="telephone", lookup_expr="icontains")
    specialty_one = django_filters.CharFilter(field_name="specialty_one", lookup_expr="icontains")
    specialty_two = django_filters.CharFilter(field_name="specialty_two", lookup_expr="icontains")
    campus = django_filters.CharFilter(field_name="campus", lookup_expr="icontains")
    admission_status = django_filters.BooleanFilter(field_name="admission_status")
    action = django_filters.CharFilter(field_name="action", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('registration_number', 'registration_number'), 
        ('specialty_one', 'specialty_one'), 
        ('full_name', 'full_name'), 
        ('campus', 'campus'), 
        ('admission_status', 'admission_status'), 
        ('action', 'action'), 
    ))

    class Meta:
        model = PreInscription
        fields = [
            'id', 'registration_number', 'first_name', 'last_name', 'full_name', 'telephone', 'specialty_one', 
            'specialty_two', 'campus', 'admission_status', 'action',
        ]
