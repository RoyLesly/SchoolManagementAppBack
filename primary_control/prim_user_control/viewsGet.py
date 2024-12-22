from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission
from .models import *
from back.utils import *
from higher_control.user_control.serializers import *
from higher_control.app_control.serializers import UserProfileSerializer
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .filters import *


class GetPrimaryProfileView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = UserProfile.objects.all().order_by("-created_at")
    # serializer_class = GetUserProfileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryProfileFilter
    # permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        if fieldList:
            fieldList = fieldList.split(',')
            return self.queryset.values(*fieldList)
        return super().get_queryset()

    def paginate_queryset(self, queryset):
        param = querydict_to_dict(self.request.query_params)
        nopage = param.pop("nopage", None)
        if nopage:
            return None
        return super().paginate_queryset(queryset)
