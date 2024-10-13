import django_filters
from .models import *



class SecSchoolFeesFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__id = django_filters.CharFilter(lookup_expr="iexact")
    secondaryprofile__secondary_classroom__id = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__secondary_classroom__main_secondary_classroom__secondary_classroom_name = django_filters.CharFilter(lookup_expr="icontains")
    secondaryprofile__secondary_classroom__level__level = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__secondary_classroom__academic_year = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__secondary_classroom__school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__user__id = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    secondaryprofile__user__matricle = django_filters.CharFilter(lookup_expr="exact")
    secondaryprofile__user__username = django_filters.CharFilter(lookup_expr="iexact")
    secondaryprofile__secondary_classroom__payment_one = django_filters.CharFilter(lookup_expr="iexact")
    secondaryprofile__secondary_classroom__payment_two = django_filters.CharFilter(lookup_expr="iexact")
    secondaryprofile__secondary_classroom__payment_three = django_filters.CharFilter(lookup_expr="iexact")
    secondaryprofile__no_secondary_classroom = django_filters.BooleanFilter(field_name='secondaryprofile__secondary_classroom', lookup_expr='isnull')
    balance = django_filters.CharFilter(lookup_expr="icontains")
    platform_charges = django_filters.CharFilter(lookup_expr="icontains")
    platform_paid = django_filters.BooleanFilter(lookup_expr="exact")

    class meta:
        model = SecSchoolFees
        fields = {
        }


class SecTransactionsFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__secondaryprofile__user__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__secondaryprofile__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__secondaryprofile__secondary_classroom__id = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__secondaryprofile__secondary_classroom__main_secondary_classroom__secondary_classroom_name = django_filters.CharFilter(lookup_expr="icontains")
    schoolfees__secondaryprofile__secondary_classroom__level__level = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__secondaryprofile__secondary_classroom__academic_year = django_filters.CharFilter(lookup_expr="exact")
    schoolfees__secondaryprofile__secondary_classroom__tuition = django_filters.CharFilter(lookup_expr="exact")
    ref = django_filters.CharFilter(lookup_expr="exact")

    created_by__full_name = django_filters.CharFilter(lookup_expr="icontain")
    updated_by__full_name = django_filters.CharFilter(lookup_expr="icontain")

    class meta:
        model = SecTransactions
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
