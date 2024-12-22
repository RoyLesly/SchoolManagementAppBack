from .models import *
from back.utils import *
from back.middleware import *
from higher_control.user_control.serializers import *
from .serializersGet import *
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .filters import *
from django.shortcuts import redirect
from tenant.views import BaseGetViewSet


class GetDepartmentView(BaseGetViewSet):
    http_method_names = ["get"]
    queryset = Department.objects.all().order_by("-created_at")
    serializer_class = GetDepartmentSerializer
    filterset_class = DepartmentFilter


class GetPageView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Page.objects.all().order_by("name")
    serializer_class = GetPageSerializer
    filterset_class = PageFilter
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.perform_query_optimization(queryset, related_fields=["field"])
        return queryset


class GetProgramView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Program.objects.all().order_by("name")
    serializer_class = GetProgramSerializer
    filterset_class = ProgramFilter
    permission_classes = [ IsAuthenticated ]


class GetUserProfileView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = UserProfile.objects.all().order_by("-created_at")
    serializer_class = GetUserProfileSerializer
    filterset_class = UserProfileFilter
    # permission_classes = [ IsAuthenticated ]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = self.perform_query_optimization(queryset, related_fields=["field"])
    #     return queryset


class GetAppearanceView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Appearance.objects.all().order_by("-created_at")
    serializer_class = GetAppearanceSerializer
    filterset_class = AppearanceFilter
    # permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.perform_query_optimization(queryset, related_fields=["field"])
        return queryset


class GetCustomUserView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = CustomUser.objects.all().order_by("-full_name")
    serializer_class = GetCustomUserSerializer
    filterset_class = CustomUserFilter
    # permission_classes = [ IsAuthenticated ]
    #permission_classes = [IsAuthenticatedWithAPIKey]  # Apply the custom permission


class GetPreInscriptionView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = PreInscription.objects.all().order_by("-full_name")
    serializer_class = GetPreInscriptionSerializer
    filterset_class = PreInscriptionFilter
    # permission_classes = [ IsAuthenticated ]


def user_verify_email(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if not user.email_confirmed:
        user.email_confirmed = True
        user.save()
        return redirect("https://resultbrains.econneq.com")
    else:
        return redirect("https://resultbrains.econneq.com")
        
        