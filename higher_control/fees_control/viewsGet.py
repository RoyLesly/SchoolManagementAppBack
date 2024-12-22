from rest_framework.viewsets import ModelViewSet
from .models import *
from back.utils import *
from higher_control.user_control.serializers import *
from .serializers import *
from .serializersGet import *
from rest_framework.permissions import IsAuthenticated
from .filters import *
from tenant.views import BaseGetViewSet


class GetActivationKeyView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = ActivationKey.objects.all().order_by("-created_at")
    serializer_class = GetActivationKeySerializer
    filterset_class = ActivationKeyFilter
    # permission_classes = [ IsAuthenticated ]


class GetSchoolFeesView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = SchoolFees.objects.all().order_by("-id")
    serializer_class = GetSchoolFeesSerializer
    filterset_class = SchoolFeesFilter
    # permission_classes = [ IsAuthenticated ]

class GetTransactionsView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Transactions.objects.all().order_by("-created_at")
    serializer_class = GetTransactionsSerializer
    filterset_class = TransactionsFilter
    # permission_classes = [ IsAuthenticated ]


class GetAccountView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Account.objects.all().order_by("name")
    serializer_class = GetAccountSerializer
    filterset_class = AccountFilter
    # permission_classes = [ IsAuthenticated ]


class GetTranscriptApplicationView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = TranscriptApplication.objects.all().order_by("-created_at")
    serializer_class = GetTranscriptApplicationSerializer
    filterset_class = TranscriptApplicationFilter
    # permission_classes = [ IsAuthenticated ]


class GetProfileInfoView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = SchoolFees.objects.all().order_by("-created_at")
    serializer_class = GetSchoolFeesSerializer
    filterset_class = SchoolFeesFilter
    # permission_classes = [ IsAuthenticated ]

