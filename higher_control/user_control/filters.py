import django_filters
from .models import *


class DepartmentFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Department
        fields = [
            "id",
            "name"
        ]


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
    id = django_filters.CharFilter(field_name="id", lookup_expr="exact")
    code = django_filters.CharFilter(field_name="code", lookup_expr="exact")
    user_id = django_filters.CharFilter(field_name="user__id", lookup_expr="exact")
    first_name = django_filters.CharFilter(field_name="user__first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(field_name="user__last_name", lookup_expr="icontains")
    full_name = django_filters.CharFilter(field_name="user__full_name", lookup_expr="icontains")
    matricle = django_filters.CharFilter(field_name="user__matricle", lookup_expr="iexact")
    username = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    sex = django_filters.CharFilter(field_name="user__sex", lookup_expr="iexact")
    dob = django_filters.DateFilter(field_name="user__dob", lookup_expr="exact")
    pob = django_filters.CharFilter(field_name="user__pob", lookup_expr="icontains")
    address = django_filters.CharFilter(field_name="user__address", lookup_expr="icontains")
    telephone = django_filters.CharFilter(field_name="user__telephone", lookup_expr="iexact")
    email = django_filters.CharFilter(field_name="user__email", lookup_expr="icontains")
    is_active = django_filters.BooleanFilter(field_name="user__is_active", lookup_expr="exact")
    is_staff = django_filters.BooleanFilter(field_name="user__is_staff", lookup_expr="exact")
    parent = django_filters.CharFilter(field_name="user__parent", lookup_expr="icontains")
    parent_telephone = django_filters.CharFilter(field_name="user__parent_telephone", lookup_expr="icontains")
    specialty_id = django_filters.CharFilter(field_name="specialty__id", lookup_expr="exact")
    specialty_name = django_filters.CharFilter(field_name="specialty__main_specialty__specialty_name", lookup_expr="icontains")
    domain_id = django_filters.CharFilter(field_name="specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    academic_year = django_filters.CharFilter(field_name="specialty__academic_year", lookup_expr="icontains")
    tuition = django_filters.CharFilter(field_name="specialty__tuition", lookup_expr="icontains")
    level = django_filters.CharFilter(field_name="specialty__level__level", lookup_expr="iexact")
    field_name = django_filters.CharFilter(field_name="specialty__main_specialty__field__field_name", lookup_expr="icontains")
    campus = django_filters.CharFilter(field_name="specialty__school__campus", lookup_expr="icontains")
    region = django_filters.CharFilter(field_name="specialty__school__region", lookup_expr="icontains")
    school_name = django_filters.CharFilter(field_name="specialty__school__school_name", lookup_expr="icontains")
    school_id = django_filters.CharFilter(field_name="specialty__school__id", lookup_expr="exact")
    version = django_filters.CharFilter(field_name="specialty__school__school_identification__version", lookup_expr="icontains")
    program_id = django_filters.CharFilter(field_name="specialty__program__id", lookup_expr="exact")
    program_name = django_filters.CharFilter(field_name="specialty__program__name", lookup_expr="icontains")
    active = django_filters.BooleanFilter(field_name="active", lookup_expr="exact")
    session = django_filters.CharFilter(field_name="session", lookup_expr="iexact")
    created_by_full_name = django_filters.CharFilter(field_name="created_by_full_name", lookup_expr="icontains")
    created_at = django_filters.DateFilter(field_name="created_at", lookup_expr="exact")
    updated_at = django_filters.DateFilter(field_name="updated_at", lookup_expr="exact")

    nospecialty = django_filters.BooleanFilter(field_name="specialty", lookup_expr="isnull")

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "code",
            "user_id",
            "first_name",
            "last_name",
            "full_name",
            "matricle",
            "username",
            "sex",
            "dob",
            "pob",
            "address",
            "telephone",
            "email",
            "is_active",
            "is_staff",
            "parent",
            "parent_telephone",
            "specialty_id",
            "specialty_name",
            "domain_id",
            "domain_name",
            "academic_year",
            "tuition",
            "level",
            "field_name",
            "campus",
            "region",
            "school_name",
            "school_id",
            "version",
            "program_id",
            "program_name",
            "active",
            "session",
            "created_by_full_name",
            "created_at",
            "updated_at",
        ]


class CustomUserFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    username = django_filters.CharFilter(lookup_expr="icontains")
    matricle = django_filters.CharFilter(lookup_expr="iexact")
    user_name = django_filters.CharFilter(field_name="username", lookup_expr="icontains")  # Maps to serializer name
    role = django_filters.CharFilter(lookup_expr="iexact")
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    full_name = django_filters.CharFilter(lookup_expr="icontains")
    sex = django_filters.CharFilter(lookup_expr="iexact")
    address = django_filters.CharFilter(lookup_expr="icontains")
    dob = django_filters.DateFilter(lookup_expr="exact")  # Assuming dob is a DateField
    pob = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="iexact")
    telephone = django_filters.CharFilter(lookup_expr="icontains")
    title = django_filters.CharFilter(lookup_expr="iexact")
    is_staff = django_filters.BooleanFilter(field_name="is_staff")
    is_active = django_filters.BooleanFilter(field_name="is_active")
    is_superuser = django_filters.BooleanFilter(field_name="is_superuser")
    last_login = django_filters.DateTimeFilter(lookup_expr="exact")  # Assuming last_login is DateTimeField
    school_id = django_filters.NumberFilter(field_name="school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="school__campus", lookup_expr="exact")

    # Nested relationships
    dept = django_filters.CharFilter(field_name="dept__name", lookup_expr="icontains")
    page = django_filters.CharFilter(field_name="page__name", lookup_expr="icontains")
    school = django_filters.CharFilter(field_name="school__school_name", lookup_expr="icontains")

    noadmin = django_filters.BooleanFilter(method='filter_exclude_admin')
    noteacher = django_filters.BooleanFilter(method='filter_exclude_teacher')
    nostudent = django_filters.BooleanFilter(method='filter_exclude_student')

    created_at = django_filters.DateFilter(field_name="created_at", lookup_expr="date")
    updated_at = django_filters.DateFilter(field_name="updated_at", lookup_expr="date")
    updated_by = django_filters.CharFilter(field_name="updated_by__username", lookup_expr="icontains")  # Assumes `updated_by` is a ForeignKey to a user model

    class Meta:
        model = CustomUser
        fields = [
            "id", "username", "matricle", "user_name", "role", "first_name", "last_name",
            "full_name", "sex", "address", "dob", "pob", "email", "telephone", "title",
            "is_active", "is_superuser", "last_login", "school__id", "school__campus__id",
            "dept", "page", "school", "created_at", "updated_at", "updated_by"
        ]

    def filter_exclude_student(self, queryset, name, value):
        if value:  # If the filter is set to True
            return queryset.exclude(role="student")  # Exclude users with the "student" role
        return queryset  # Return all users (no exclusion)
    def filter_exclude_admin(self, queryset, name, value):
        if value:  # If the filter is set to True
            return queryset.exclude(role="admin")  # Exclude users with the "student" role
        return queryset  # Return all users (no exclusion)
    def filter_exclude_teacher(self, queryset, name, value):
        if value:  # If the filter is set to True
            return queryset.exclude(role="teacher")  # Exclude users with the "student" role
        return queryset  # Return all users (no exclusion)


class PreInscriptionFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    registration_number = django_filters.CharFilter(lookup_expr="iexact")
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    full_name = django_filters.CharFilter(lookup_expr="icontains")
    sex = django_filters.CharFilter(lookup_expr="iexact")
    email = django_filters.CharFilter(lookup_expr="icontains")
    telephone = django_filters.CharFilter(lookup_expr="icontains")
    address = django_filters.CharFilter(lookup_expr="icontains")
    pob = django_filters.CharFilter(lookup_expr="icontains")
    dob = django_filters.DateFilter(lookup_expr="exact")
    status = django_filters.CharFilter(lookup_expr="iexact")
    emergency_name = django_filters.CharFilter(lookup_expr="icontains")
    emergency_town = django_filters.CharFilter(lookup_expr="icontains")
    emergency_telephone = django_filters.CharFilter(lookup_expr="iexact")
    program = django_filters.CharFilter(lookup_expr="icontains")
    level = django_filters.CharFilter(lookup_expr="iexact")
    session = django_filters.CharFilter(lookup_expr="iexact")
    academic_year = django_filters.CharFilter(lookup_expr="iexact")
    specialty_one = django_filters.CharFilter(lookup_expr="icontains")
    specialty_two = django_filters.CharFilter(lookup_expr="icontains")
    specialty_three = django_filters.CharFilter(lookup_expr="icontains")
    campus = django_filters.CharFilter(lookup_expr="iexact")
    admission_status = django_filters.BooleanFilter(lookup_expr="exact")
    action = django_filters.CharFilter(lookup_expr="iexact")
    created_at = django_filters.DateTimeFilter(lookup_expr="exact")
    updated_at = django_filters.DateTimeFilter(lookup_expr="exact")

    class Meta:
        model = PreInscription
        fields = [
            "id",
            "registration_number",
            "first_name",
            "last_name",
            "full_name",
            "sex",
            "email",
            "telephone",
            "address",
            "pob",
            "dob",
            "status",
            "emergency_name",
            "emergency_town",
            "emergency_telephone",
            "program",
            "level",
            "session",
            "academic_year",
            "specialty_one",
            "specialty_two",
            "specialty_three",
            "campus",
            "admission_status",
            "action",
            "created_at",
            "updated_at",
        ]


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
