import django_filters
from .models import *


class SchoolFeesFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name="userprofile__user__id", lookup_expr="exact")
    userprofile_id = django_filters.NumberFilter(field_name="userprofile__id", lookup_expr="exact")
    full_name = django_filters.CharFilter(field_name="userprofile__user__full_name", lookup_expr="icontains")
    matricle = django_filters.CharFilter(field_name="userprofile__user__matricle", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="userprofile__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    specialty_name = django_filters.CharFilter(field_name="userprofile__specialty__main_specialty__Specialty_name", lookup_expr="icontains")
    academic_year = django_filters.CharFilter(field_name="userprofile__specialty__academic_year", lookup_expr="icontains")
    level = django_filters.NumberFilter(field_name="userprofile__specialty__level__level", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="userprofile__specialty__school__campus", lookup_expr="icontains")
    school_id = django_filters.NumberFilter(field_name="userprofile__specialty__school__id", lookup_expr="exact")
    platform_paid = django_filters.BooleanFilter(field_name="platform_paid")
    balance = django_filters.NumberFilter(field_name="balance")

    ordering = django_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('userprofile__user__id', 'user_id'),
            ('userprofile__id', 'userprofile_id'),
            ('userprofile__specialty__school__campus', 'campus'),
            ('userprofile__specialty__main_specialty__specialty_name', 'specialty_name'),
            ('userprofile__user__full_name', 'full_name'),
        )
    )

    class Meta:
        model = SchoolFees
        fields = ['id', 'user_id', 'userprofile_id', 'full_name', 'matricle', 'domain_name', 'specialty_name', 'academic_year', 
                  'level', 'school_id', 'platform_paid', 'balance',]



class TransactionsFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__user__id", lookup_expr="exact")
    userprofile_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__id", lookup_expr="exact")
    full_name = django_filters.CharFilter(field_name="schoolfees__userprofile__id", lookup_expr="icontains")
    matricle = django_filters.CharFilter(field_name="schoolfees__userprofile__id", lookup_expr="icontains")
    domain_name = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    specialty_name = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__main_specialty__Specialty_name", lookup_expr="icontains")
    academic_year = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__academic_year", lookup_expr="icontains")
    level = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__level__level", lookup_expr="exact")
    school_id = django_filters.NumberFilter(field_name="schoolfees__userprofile__specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="schoolfees__userprofile__specialty__school__campus", lookup_expr="icontains")
    
    amount = django_filters.CharFilter(field_name="amount", lookup_expr="exact")
    reason = django_filters.CharFilter(field_name="reason", lookup_expr="icontains")
    payment_method = django_filters.CharFilter(field_name="payment_method", lookup_expr="icontains")
    ref = django_filters.CharFilter(field_name="ref", lookup_expr="icontains")
    telephone = django_filters.CharFilter(field_name="telephone", lookup_expr="icontains")
    payer_name = django_filters.CharFilter(field_name="payer_name", lookup_expr="icontains")
    status = django_filters.BooleanFilter(field_name="status")
    operation_type = django_filters.CharFilter(field_name="operation_type", lookup_expr="icontains")
    
    created_at = django_filters.DateTimeFromToRangeFilter(field_name="created_at", lookup_expr="icontains")
    updated_at = django_filters.DateTimeFromToRangeFilter(field_name="updated_at", lookup_expr="icontains")
    created_by = django_filters.CharFilter(field_name="created_by__full_name", lookup_expr="icontains")
    updated_by = django_filters.CharFilter(field_name="updaated_by__full_name", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('schoolfees__userprofile__specialty__school__campus', 'campus'),
            ('schoolfees__userprofile__specialty__main_specialty__field__domain__domain_name', 'domain_name'),
            ('schoolfees__userprofile__specialty__main_specialty__specialty_name', 'specialty_name'),
            ('schoolfees__userprofile__user__first_name', 'full_name'),
        )
    )

    class Meta:
        model = Transactions
        fields = [ 
            'user_id', 'userprofile_id', 'full_name', 'matricle', 'domain_name', 'specialty_name',
            'academic_year', 'level', 'school_id', 'amount', 'reason', 'ref', 'telephone', 'status', 'operation_type',
            'created_at', 'created_by__full_name', 'updated_at', 'updated_by__full_name'
        ]

