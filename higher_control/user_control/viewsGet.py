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
from django.shortcuts import redirect


class GetDepartmentView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Department.objects.all().order_by("name")
    serializer_class = GetDepartmentSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter
    # permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        if fieldList:
            fieldList = fieldList.split(',')
            return self.queryset.values(*fieldList)
        return super().get_queryset()


class GetPageView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Page.objects.all().order_by("name")
    serializer_class = GetPageSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PageFilter
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        if fieldList:
            fieldList = fieldList.split(',')
            return self.queryset.values(*fieldList)
        return super().get_queryset()


class GetProgramView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Program.objects.all().order_by("name")
    serializer_class = GetProgramSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProgramFilter
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        if fieldList:
            fieldList = fieldList.split(',')
            return self.queryset.values(*fieldList)
        return super().get_queryset()


class GetUserProfileView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = UserProfile.objects.all().order_by("-created_at")
    serializer_class = GetUserProfileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserProfileFilter
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


class GetAppearanceView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Appearance.objects.all().order_by("-created_at")
    serializer_class = GetAppearanceSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppearanceFilter
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


class GetCustomUserView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = CustomUser.objects.all().order_by("-full_name")
    serializer_class = GetCustomUserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter
    # permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        notstudent = param.pop("notstudent", None)
        q = self.queryset
        if fieldList:
            fieldList = fieldList.split(',')
            if notstudent == "true":
                q = self.queryset.exclude(role="student")
            return q.values(*fieldList)
        return super().get_queryset()

    def paginate_queryset(self, queryset):
        param = querydict_to_dict(self.request.query_params)
        nopage = param.pop("nopage", None)
        if nopage:
            return None
        return super().paginate_queryset(queryset)


class GetPreInscriptionView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = PreInscription.objects.all().order_by("-full_name")
    serializer_class = GetPreInscriptionSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PreInscriptionFilter
    # permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        notstudent = param.pop("notstudent", None)
        q = self.queryset
        if fieldList:
            fieldList = fieldList.split(',')
            if notstudent == "true":
                q = self.queryset.exclude(role="student")
            return q.values(*fieldList)
        return super().get_queryset()

    def paginate_queryset(self, queryset):
        param = querydict_to_dict(self.request.query_params)
        nopage = param.pop("nopage", None)
        if nopage:
            return None
        return super().paginate_queryset(queryset)
    

def user_verify_email(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if not user.email_confirmed:
        user.email_confirmed = True
        user.save()
        return redirect("https://resultbrains.econneq.com")
    else:
        return redirect("https://resultbrains.econneq.com")
        
        