import django_filters
from .models import *


class SecondaryProfileFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    user__id = django_filters.CharFilter(lookup_expr="exact")
    user__matricle = django_filters.CharFilter(lookup_expr="icontains")
    user__username = django_filters.CharFilter(lookup_expr="icontains")
    user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    user__role = django_filters.CharFilter(lookup_expr="iexact")
    user__is_active = django_filters.BooleanFilter()
    user__is_superuser = django_filters.BooleanFilter()
    user__email = django_filters.CharFilter(lookup_expr="icontains")
    user__dob = django_filters.CharFilter(lookup_expr="iexact")
    user__last_login = django_filters.CharFilter(lookup_expr="iexact")
    user__telephone = django_filters.CharFilter(lookup_expr="icontains")
    user__school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    user__is_staff = django_filters.BooleanFilter(lookup_expr="exact")
    secondary_classroom__id = django_filters.CharFilter(lookup_expr="exact")
    secondary_classroom__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    secondary_classroom__level__level = django_filters.CharFilter(lookup_expr="icontains")
    secondary_classroom__level__id = django_filters.CharFilter(lookup_expr="exact")
    secondary_classroom__school__id = django_filters.CharFilter(lookup_expr="exact")
    secondary_classroom__school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    secondary_classroom__school__campus__region = django_filters.CharFilter(lookup_expr="icontains")
    secondary_classroom__school__campus__name = django_filters.CharFilter(lookup_expr="icontains")
    session = django_filters.CharFilter(lookup_expr="icontains")

    noclassroom = django_filters.BooleanFilter(field_name='secondary_classroom', lookup_expr='isnull')

    class meta:
        model = SecondaryProfile
        fields = {
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }


class PlatformFilter(django_filters.FilterSet):
    userprofile__user__id = django_filters.CharFilter(lookup_expr="exact")
    userprofile__user__matricle = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__user__username = django_filters.CharFilter(lookup_expr="icontains")
    userprofile__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    telephone = django_filters.CharFilter(lookup_expr="icontains")
    paid = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        # model = UserProfile
        fields = {
            'id': [ "exact" ],
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }
