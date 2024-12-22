import graphene
from graphene_django.types import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from higher_control.user_control.models import CustomUser, UserProfile
from .schemaFilter import *



# Types for Models
class ActivationKeyType(DjangoObjectType):
    class Meta:
        model = ActivationKey


class SchoolFeesType(DjangoObjectType):
    class Meta:
        model = SchoolFees
        filter_fields = [
            'id', 
            'userprofile__user__id', 
            'userprofile__id', 
            'userprofile__user__full_name', 
            'userprofile__user__matricle', 
            'userprofile__specialty__main_specialty__field__domain__domain_name', 
            'userprofile__specialty__main_specialty__Specialty_name', 
            'userprofile__specialty__academic_year', 
            'userprofile__specialty__level__level', 
            'userprofile__specialty__school__campus', 
            'userprofile__specialty__school__id', 
            'platform_paid', 
            'balance',
        ]
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "userprofile",
            "platform_paid",
            "balance",
        )


class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
        )


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transactions
        filter_fields = [
            'id', 
            'schoolfees__userprofile__user__id', 
            'schoolfees__userprofile__id', 
            'schoolfees__userprofile__user__full_name', 
            'schoolfees__userprofile__user__matricle', 
            'schoolfees__userprofile__specialty__main_specialty__field__domain__domain_name', 
            'schoolfees__userprofile__specialty__main_specialty__Specialty_name', 
            'schoolfees__userprofile__specialty__academic_year', 
            'schoolfees__userprofile__specialty__level__level', 
            'schoolfees__userprofile__specialty__school__campus', 
            'schoolfees__userprofile__specialty__school__id', 
            'schoolfees__platform_paid', 
            'created_at',
            'updated_at',
            'created_by__full_name',
            'updated_by__full_name',
        ]
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "schoolfees",
            "payer_name",
            "telephone",
            "status",
            "payment_method",
            "account",
            "reason",
            "ref",
            "operation_type",
            "origin",
            "amount",
            "operator",
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
        )


class TranscriptApplicationType(DjangoObjectType):
    class Meta:
        model = TranscriptApplication


# Queries
class Query(graphene.ObjectType):
    all_activation_keys = graphene.List(ActivationKeyType)
    all_school_fees = DjangoFilterConnectionField(SchoolFeesType, filterset_class=SchoolFeesFilter)
    all_transactions = DjangoFilterConnectionField(TransactionType, filterset_class=TransactionsFilter)
    all_accounts = graphene.List(AccountType)
    all_transcript_applications = graphene.List(TranscriptApplicationType)


schema = graphene.Schema(query=Query)
