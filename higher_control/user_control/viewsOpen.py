from rest_framework.viewsets import ModelViewSet
from .models import *
from back.utils import *
from back.middleware import *
from higher_control.user_control.serializers import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters import rest_framework as filters
from .filters import *
from django.shortcuts import redirect


# OPEN END POINTS
class CheckCustomUserView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = CustomUser.objects.all().order_by("-full_name")
    serializer_class = GetCustomUserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter
    permission_classes = [ IsAuthenticatedWithAPIKey ]

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


class CheckPreInscriptionView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = PreInscription.objects.all().order_by("-full_name")
    serializer_class = GetPreInscriptionSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PreInscriptionFilter
    # permission_classes = [ IsAuthenticated ]
    permission_classes = [ IsAuthenticatedWithAPIKey ]

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
    
