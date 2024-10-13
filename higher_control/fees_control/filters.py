import django_filters
from .models import *


class SchoolFeesFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    userprofile__id = django_filters.CharFilter(lookup_expr="iexact")
    userprofile__specialty__id = django_filters.CharFilter(lookup_expr="exact")
    userprofile__specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__specialty__level__level = django_filters.CharFilter(lookup_expr="exact")
    userprofile__specialty__academic_year = django_filters.CharFilter(lookup_expr="exact")
    userprofile__specialty__school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    userprofile__specialty__main_specialty__field__domain__id = django_filters.CharFilter(lookup_expr="exact")
    userprofile__specialty__main_specialty__field__domain__domain_name = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__user__id = django_filters.CharFilter(lookup_expr="exact")
    userprofile__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__user__matricle = django_filters.CharFilter(lookup_expr="exact")
    userprofile__user__username = django_filters.CharFilter(lookup_expr="iexact")
    userprofile__specialty__payment_one = django_filters.CharFilter(lookup_expr="iexact")
    userprofile__specialty__payment_two = django_filters.CharFilter(lookup_expr="iexact")
    userprofile__specialty__payment_three = django_filters.CharFilter(lookup_expr="iexact")
    userprofile__no_specialty = django_filters.BooleanFilter(field_name='userprofile__specialty', lookup_expr='isnull')
    balance = django_filters.CharFilter(lookup_expr="icontains")
    platform_charges = django_filters.CharFilter(lookup_expr="icontains")
    platform_paid = django_filters.BooleanFilter(lookup_expr="exact")
    created_at = django_filters.CharFilter(lookup_expr="icontain")

    class meta:
        model = SchoolFees
        fields = {
        }


class TransactionsFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__user__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__specialty__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    schoolfees__userprofile__specialty__level__level = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__specialty__academic_year = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__specialty__tuition = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__userprofile__specialty__school__id = django_filters.CharFilter(lookup_expr="exact")
    origin = django_filters.CharFilter(lookup_expr="icontains")
    ref = django_filters.CharFilter(lookup_expr="exact")

    created_at = django_filters.DateTimeFilter(lookup_expr="icontain")
    created_by__full_name = django_filters.CharFilter(lookup_expr="icontain")
    updated_by__full_name = django_filters.CharFilter(lookup_expr="icontain")

    class meta:
        model = Transactions
        fields = {
        }

class ActivationKeyFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    key = django_filters.CharFilter(lookup_expr="icontains")
    is_used = django_filters.BooleanFilter(lookup_expr="exact")

    created_by__full_name = django_filters.CharFilter(lookup_expr="icontain")
    updated_by__full_name = django_filters.CharFilter(lookup_expr="icontain")

    class meta:
        model = ActivationKey
        fields = {
        }


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
    userprofile__id = django_filters.NumberFilter(lookup_expr="exact")
    userprofile__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__user__matricle = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__specialty__id = django_filters.NumberFilter(lookup_expr="exact")
    userprofile__specialty__main_specialty__specialty_name = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__specialty__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__specialty__level__level = django_filters.NumberFilter(lookup_expr="icontains")
    approved_by__id = django_filters.NumberFilter(lookup_expr="exact")
    status = django_filters.CharFilter(lookup_expr="icontains")
    approved_by__full_name = django_filters.CharFilter(lookup_expr="icontains")
    approved_at = django_filters.CharFilter(lookup_expr="icontains")
    printed_count = django_filters.NumberFilter(lookup_expr="exact")
    printed_by__id = django_filters.NumberFilter(lookup_expr="exact")
    printed_by__full_name = django_filters.CharFilter(lookup_expr="icontains")
    printed_at = django_filters.CharFilter(lookup_expr="icontains")
    created_at = django_filters.CharFilter(lookup_expr="icontains")
    updated_at = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = TranscriptApplication
        fields = {
        }
