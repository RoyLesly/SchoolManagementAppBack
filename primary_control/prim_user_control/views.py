from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission
from .models import *
from back.utils import *
from higher_control.user_control.serializers import *
from higher_control.app_control.serializers import UserProfileSerializer
from .serializers import *
from rest_framework_simplejwt.views import (TokenObtainPairView,)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from back.utils import get_query
from django_filters import rest_framework as filters
from .filters import *


class PrimaryProfileView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = UserProfile.objects.all().order_by("-created_at")
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryProfileFilter
    # permission_classes = [ IsAuthenticatedCustom ]


# class UserActivityView(ModelViewSet):
#     http_method_names = [ "post", "get", "put", "delete"]
#     queryset = UserActivity.objects.all().order_by("-created_at")
#     serializer_class = UserActivitySerializer
#     parser_classes = (MultiPartParser, FormParser, JSONParser)
#     pagination_class = CustomPagination
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = UserActivityFilter
#     # permission_classes = [ IsAuthenticatedCustom ]

