import django_filters
from .models import *


class SchoolFeesFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    user_id = django_filters.NumberFilter(field_name="userprofile__user__id", lookup_expr="exact")
    userprofile_id = django_filters.NumberFilter(field_name="userprofile__id", lookup_expr="exact")
    full_name = django_filters.CharFilter(field_name="userprofile__user__full_name", lookup_expr="exact")
    matricle = django_filters.CharFilter(field_name="userprofile__user__matricle", lookup_expr="exact")
    username = django_filters.CharFilter(field_name="userprofile__user__username", lookup_expr="exact")
    specialty_id = django_filters.NumberFilter(field_name="userprofile__specialty__id", lookup_expr="exact")
    specialty_name = django_filters.CharFilter(field_name="userprofile__specialty__main_specialty__specialty_name", lookup_expr="icontains")
    level = django_filters.NumberFilter(field_name="userprofile__specialty__level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="userprofile__specialty__academic_year", lookup_expr="exact")
    school_id = django_filters.NumberFilter(field_name="userprofile__specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="userprofile__specialty__school__campus", lookup_expr="exact")
    domain_id = django_filters.CharFilter(field_name="userprofile__specialty__main_specialty__field__domain__id", lookup_expr="icontains")
    domain_name = django_filters.CharFilter(field_name="userprofile__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    tuition = django_filters.NumberFilter(field_name="userprofile__specialty__tuition", lookup_expr="exact")
    registration = django_filters.NumberFilter(field_name="userprofile__specialty__registration", lookup_expr="exact")
    payment_one = django_filters.NumberFilter(field_name="userprofile__specialty__payment_one", lookup_expr="exact")
    payment_two = django_filters.NumberFilter(field_name="userprofile__specialty__payment_two", lookup_expr="exact")
    payment_three = django_filters.NumberFilter(field_name="userprofile__specialty__payment_three", lookup_expr="exact")
    no_specialty = django_filters.BooleanFilter(field_name='userprofile__specialty', lookup_expr='isnull')
    balance = django_filters.RangeFilter()  #?balance_min=100&balance_max=500 Added RangeFilter for balance
    platform_charges = django_filters.NumberFilter(field_name="userprofile__specialty__school__platform_charges", lookup_expr="exact")
    platform_paid = django_filters.BooleanFilter(lookup_expr="exact")
    created_at = django_filters.DateFromToRangeFilter()  #?created_at_after=2024-01-01&created_at_before=2024-12-31, ?created_at_after=2024-01-01  Range filter for DateField
    updated_at = django_filters.DateFromToRangeFilter()  #?created_at_after=2024-01-01&created_at_before=2024-12-31, ?created_at_after=2024-01-01  Range filter for DateField

    class Meta:
        model = SchoolFees
        fields = [
            'id', 'user_id', 'userprofile_id', 'full_name', 'matricle', 'username', 'specialty_id', 'specialty_name', 'level', 'academic_year',
            'school_id', 'campus', 'domain_id', 'domain_name', 'tuition', 'registration', 'payment_one', 'payment_two', 'payment_three', 'no_specialty',
            'balance', 'platform_charges', 'platform_paid', 'created_at'
        ]


class TransactionsFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees_id = django_filters.CharFilter(field_name="schoolfees__id", lookup_expr="iexact")
    user_id = django_filters.CharFilter(field_name="schoolfees__userprofile__user__id", lookup_expr="iexact")
    userprofile_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__id", lookup_expr="exact")
    full_name = django_filters.CharFilter(field_name="schoolfees__userprofile__user__full_name", lookup_expr="exact")
    matricle = django_filters.CharFilter(field_name="schoolfees__userprofile__user__matricle", lookup_expr="exact")
    username = django_filters.CharFilter(field_name="schoolfees__userprofile__user__username", lookup_expr="exact")
    specialty_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__id", lookup_expr="exact")
    specialty_name = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__main_specialty__specialty_name", lookup_expr="icontains")
    level = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__academic_year", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__school__campus", lookup_expr="exact")
    school_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__school__id", lookup_expr="exact")
    domain_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    tuition = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__tuition", lookup_expr="exact")
    registration = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__registration", lookup_expr="exact")
    origin = django_filters.CharFilter(lookup_expr="icontains")
    ref = django_filters.CharFilter(lookup_expr="exact")
    created_at = django_filters.DateTimeFilter(lookup_expr="gte")  # Replace with valid lookup as needed
    created_by_full_name = django_filters.CharFilter(field_name="created_by__full_name", lookup_expr="icontains")
    updated_by_full_name = django_filters.CharFilter(field_name="updated_by__full_name", lookup_expr="icontains")

    class Meta:
        model = Transactions
        fields = [
            'id', 'schoolfees_id', 'user_id', 'userprofile_id', 'full_name', 'matricle', 'username', 'specialty_id', 'specialty_name',
            'level', 'academic_year', 'school_id', 'campus', 'domain_id', 'domain_name', 'tuition', 'registration', 'origin', 'ref',
            'created_at', 'created_by_full_name', 'updated_by_full_name',
        ]


class ActivationKeyFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    key = django_filters.CharFilter(lookup_expr="icontains")
    is_used = django_filters.BooleanFilter(lookup_expr="exact")

    created_by__full_name = django_filters.CharFilter(lookup_expr="icontain")
    updated_by__full_name = django_filters.CharFilter(lookup_expr="icontain")

    class meta:
        model = ActivationKey
        fields = [
            'id'
        ]


class AccountFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    name = django_filters.CharFilter(lookup_expr="icontains")
    number = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(lookup_expr="icontains")
    balance = django_filters.NumberFilter(lookup_expr="icontains")

    class meta:
        model = Account
        fields = {
        }


class TranscriptApplicationFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    user_id = django_filters.CharFilter(field_name="userprofile__user__id" ,lookup_expr="iexact")
    userprofile_id = django_filters.NumberFilter(field_name="userprofile__id" ,lookup_expr="iexact")
    full_name = django_filters.CharFilter(field_name="userprofile__user__full_name" ,lookup_expr="exact")
    matricle = django_filters.CharFilter(field_name="userprofile__user__imatricle" ,lookup_expr="exact")
    username = django_filters.CharFilter(field_name="userprofile__user__username" ,lookup_expr="exact")
    specialty_id = django_filters.NumberFilter(field_name="userprofile__specialty__id" ,lookup_expr="exact")
    specialty_name = django_filters.CharFilter(field_name="userprofile__specialty__main_specialty__specialty_name" ,lookup_expr="icontains")
    level = django_filters.NumberFilter(field_name="userprofile__specialty__level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="userprofile__specialty__academic_year", lookup_expr="exact")
    school_id = django_filters.NumberFilter(field_name="_userprofile__specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="userprofile__specialty__school__campus", lookup_expr="exact")
    school_id = django_filters.NumberFilter(field_name="userprofile__specialty__school__id", lookup_expr="exact")
    
    domain_id = django_filters.NumberFilter(field_name="userprofile__specialty__main_specialty__field__domain__id", lookup_expr="icontains")
    domain_name = django_filters.CharFilter(field_name="_userprofile__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    tuition = django_filters.NumberFilter(field_name="userprofile__specialty__tuition", lookup_expr="iexact")
    registration = django_filters.NumberFilter(field_name="userprofile__specialty__registration", lookup_expr="iexact")
    approved_by_id = django_filters.NumberFilter(field_name="approved_by__id", lookup_expr="iexact")
    
    status = django_filters.CharFilter(lookup_expr="icontains")
    approved_by__full_name = django_filters.CharFilter(lookup_expr="icontains")
    approved_at = django_filters.CharFilter(lookup_expr="icontains")
    printed_count = django_filters.NumberFilter(lookup_expr="exact")
    printed_by_id = django_filters.NumberFilter(field_name="printed_by__id", lookup_expr="iexact")
    printed_by_full_name = django_filters.NumberFilter(field_name="printed_by__full_name", lookup_expr="iexact")
    printed_at = django_filters.CharFilter(lookup_expr="icontains")
    created_at = django_filters.CharFilter(lookup_expr="icontains")
    updated_at = django_filters.CharFilter(lookup_expr="icontains")
    created_by_full_name = django_filters.CharFilter(field_name="created_by__full_name", lookup_expr="icontains")
    updated_by_full_name = django_filters.CharFilter(field_name="updated_by__full_name", lookup_expr="icontains")


    class meta:
        model = TranscriptApplication
        fields = {
        }
