from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from back.utils import *
from secondary_control.sec_app_control.serializers import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from back.utils import get_query
from django_filters import rest_framework as filters
from .filters import *
from django.shortcuts import redirect


class SecondaryProfileView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SecondaryProfile.objects.all().order_by("-created_at")
    serializer_class = SecondaryProfileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondaryProfileFilter
    # permission_classes = [ IsAuthenticatedCustom ]


class CheckPasswordView(APIView):
    http_method_names = [ "post", ]
    serializer_class = CustomUserSerializer

    def post(self, request):
        user = CustomUser.objects.filter(matricle=request.data["matricle"])
        if not user:
            return Response({"errors": "No Account Found" })
        if len(user) < 1:
            return Response({"errors": "No Account Found" })
        else:
            if user[0].password == "":
                return Response({"fail": {
                    "id": user[0].id,
                    "username": user[0].username,
                    "matricle": user[0].matricle,
                } })
            else:
                return Response({
                    "id": user[0].id,
                    "username": user[0].username,
                    "matricle": user[0].matricle,
                })
