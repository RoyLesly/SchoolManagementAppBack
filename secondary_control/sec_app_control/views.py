from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters


class SecondaryClassRoomView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SecondaryClassRoom.objects.all().order_by("-academic_year")
    serializer_class = SecondaryClassRoomSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondaryClassRoomFilter
    # permission_classes = [ IsAuthenticated ]


class SecondaryMainSubjectView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SecondaryMainSubject.objects.all().order_by("-created_at")
    serializer_class = SecondaryMainSubjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondaryMainSubjectFilter

   
class SecondarySubjectView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SecondarySubject.objects.all().order_by("-created_at")
    serializer_class = SecondarySubjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondarySubjectFilter
    # permission_classes = [ IsAuthenticated ]
   

class SecondaryLevelView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SecondaryLevel.objects.all().order_by("-created_at")
    serializer_class = SecondaryLevelSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    # permission_classes = [ IsAuthenticated ]
        

class SecondaryResultView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = SecondaryResult.objects.all().order_by("-created_at")
    serializer_class = SecondaryResultSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondaryResultFilter
    # permission_classes = [ IsAuthenticated ]


class SecondaryPublishView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = SecondaryPublish.objects.all().order_by("-created_at")
    serializer_class = SecondaryPublishSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SecondaryPublishFilter
    # permission_classes = [ IsAuthenticated ]
    

class SecondaryMyClassRoomsView(ViewSet):
    # permission_classes = [ IsAuthenticated ]

    def update(self, request, pk=None):
        print(145, pk)
        # if self.request.method.lower() != "get":
        #     return self.queryset
        classrooms = SecondaryClassRoom.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(classrooms)

        return Response({ 
            "count": len(acad),
            "results": acad
        })
    

class SecondaryAcademicYearView(ViewSet):
    # permission_classes = [ IsAuthenticated ]

    def list(self, request):
        if self.request.method.lower() != "get":
            return self.queryset
        classrooms = SecondaryClassRoom.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(classrooms)

        return Response({ 
            "count": len(acad),
            "results": acad
        })