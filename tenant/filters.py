import django_filters
from .models import *


class TenantFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    user__id = django_filters.NumberFilter(lookup_expr="icontains")
    user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    school_name = django_filters.CharFilter(lookup_expr="icontains")
    school_type = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    is_active = django_filters.BooleanFilter(lookup_expr="icontains")
    updated_at = django_filters.CharFilter(lookup_expr="icontains")
    created_at = django_filters.CharFilter(lookup_expr="icontains")
    
    class meta:
        model = Tenant


class DomainFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr="exact")
    tenant__id = django_filters.NumberFilter(lookup_expr="icontains")
    tenant__user__id = django_filters.NumberFilter(lookup_expr="icontains")
    tenant__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
    tenant__school_name = django_filters.CharFilter(lookup_expr="icontains")
    tenant__school_type = django_filters.CharFilter(lookup_expr="icontains")
    tenant__description = django_filters.CharFilter(lookup_expr="icontains")
    tenant__is_active = django_filters.BooleanFilter(lookup_expr="icontains")
    domain = django_filters.CharFilter(lookup_expr="icontains")
    is_primary = django_filters.BooleanFilter(lookup_expr="icontains")
    
    class meta:
        model = Domain

