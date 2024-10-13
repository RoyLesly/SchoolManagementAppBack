import django_filters
from .models import *

class NotificationFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    message_one = django_filters.CharFilter(lookup_expr="exact")
    message_two = django_filters.CharFilter(lookup_expr="icontains")
    target = django_filters.CharFilter(lookup_expr="icontains")
    schools = django_filters.CharFilter(lookup_expr="in")
    domains = django_filters.CharFilter(lookup_expr="in")
    specialty = django_filters.CharFilter(lookup_expr="in")
    role = django_filters.CharFilter(lookup_expr="icontains")
    custom = django_filters.CharFilter(lookup_expr="icontains")
    noti_type = django_filters.CharFilter(lookup_expr="icontains")
    created_by__full_name = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.BooleanFilter()
    ending_at = django_filters.BooleanFilter()

    class meta:
        model = Notification
        fields = {
            'ending_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }


class ComplainFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    message_one = django_filters.CharFilter(lookup_expr="exact")
    message_two = django_filters.CharFilter(lookup_expr="icontains")
    complain_type = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.BooleanFilter(field_name='specialty', lookup_expr='isnull')
    ending_at = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = Complain
        fields = {
            'ending_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
            'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
        }


class UserActivityFilter(django_filters.FilterSet):
    class meta:
        model = UserActivity
        fields = {
            'id': [ "exact" ],
            'name': [ "in", "exact" ]
        }