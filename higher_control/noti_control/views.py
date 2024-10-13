from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters



def add_user_activity(user, action, item, details):
    UserActivity.objects.create(
        user=user,
        action=action,
        item=item,
        details=details
    )


class NotificationView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Notification.objects.all().order_by("status")
    serializer_class = NotificationSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NotificationFilter
    # permission_classes = [ IsAuthenticated ]


class ComplainView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Complain.objects.all().order_by("-created_at")
    serializer_class = ComplainSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ComplainFilter


class UserActivityView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = UserActivity.objects.all().order_by("-created_at")
    serializer_class = UserActivitySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserActivityFilter
    # permission_classes = [ IsAuthenticatedCustom ]
