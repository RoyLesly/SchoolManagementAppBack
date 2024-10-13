from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters


class TenantView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Tenant.objects.all().order_by("id")
    serializer_class = TenantSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TenantFilter
    # permission_classes = [ IsAuthenticated ]


class DomainView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Domain.objects.all().order_by("id")
    serializer_class = DomainSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DomainFilter
    # permission_classes = [ IsAuthenticated ]
