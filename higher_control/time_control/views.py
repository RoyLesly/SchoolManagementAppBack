from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters


class TimeTableWeekView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = TimeTableWeek.objects.all().order_by("-year_week")
    serializer_class = TimeTableWeekSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TimeTableWeekFilter
    # permission_classes = [ IsAuthenticated ]
    

class TimeTableDayView(ModelViewSet):
    http_method_names = [ "get", "post", "put", "delete"]
    queryset = TimeTableDay.objects.all().order_by("-timetableweek__year_week")
    serializer_class = TimeTableDaySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TimeTableDayFilter
    # permission_classes = [ IsAuthenticated ]


class TimeSlotView(ModelViewSet):
    http_method_names = [ "get", "post", "put", "delete"]
    queryset = TimeSlot.objects.all().order_by("-timetableday__timetableweek__year_week")
    serializer_class = TimeSlotSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TimeSlotFilter
    # permission_classes = [ IsAuthenticated ]
