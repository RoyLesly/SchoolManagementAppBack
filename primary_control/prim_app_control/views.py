from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters


class PrimaryClassRoomView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = PrimaryClassRoom.objects.all().order_by("-academic_year")
    serializer_class = PrimaryClassRoomSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryClassRoomFilter
    # permission_classes = [ IsAuthenticated ]


class PrimaryMainSubjectView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = PrimaryMainSubject.objects.all().order_by("-created_at")
    serializer_class = PrimaryMainSubjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryMainSubjectFilter

   
class PrimarySubjectView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = PrimarySubject.objects.all().order_by("-created_at")
    serializer_class = PrimarySubjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimarySubjectFilter
    # permission_classes = [ IsAuthenticated ]
   

class PrimaryLevelView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = PrimaryLevel.objects.all().order_by("-created_at")
    serializer_class = PrimaryLevelSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    # permission_classes = [ IsAuthenticated ]
       