from rest_framework.viewsets import ModelViewSet
from .models import *
from back.utils import *
from back.middleware import *
from higher_control.user_control.serializers import *
from .serializersGet import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters import rest_framework as filters
from .filters import *
from tenant.views import BaseGetViewSet


# OPEN END POINTS
class CheckCustomUserView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = CustomUser.objects.all().order_by("-full_name")
    serializer_class = GetCustomUserSerializer
    filterset_class = CustomUserFilter
    permission_classes = [ IsAuthenticatedWithAPIKey ]


class CheckPreInscriptionView(BaseGetViewSet):
    http_method_names = ["get"]
    queryset = PreInscription.objects.all().order_by("-full_name")
    serializer_class = GetPreInscriptionSerializer
    filterset_class = PreInscriptionFilter
    permission_classes = [ IsAuthenticatedWithAPIKey ]

    
