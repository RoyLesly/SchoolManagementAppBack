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
    ref = django_filters.CharFilter(lookup_expr="exact")

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
