from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from .models import *
from .filters import *
from django_filters import rest_framework as filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class SchoolFeesView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SchoolFees.objects.all().order_by("-id")
    serializer_class = SchoolFeesSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SchoolFeesFilter
    # permission_classes = [ IsAuthenticated ]


class TransactionsView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Transactions.objects.all().order_by("-created_at")
    serializer_class = TransactionsSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionsFilter
    # permission_classes = [ IsAuthenticated ]



class ActivationKeyView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = ActivationKey.objects.all().order_by("-created_at")
    serializer_class = ActivationKeySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ActivationKeyFilter
    # permission_classes = [ IsAuthenticated ]


    
    