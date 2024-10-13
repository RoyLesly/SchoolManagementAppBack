from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters


class DomainView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Domain.objects.all().order_by("domain_name")
    serializer_class = DomainSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DomainFilter
    # permission_classes = [ IsAuthenticated ]


class FieldView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Field.objects.all().order_by("-created_at")
    serializer_class = FieldSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FieldFilter


class MainSpecialtyView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = MainSpecialty.objects.all().order_by("-created_at")
    serializer_class = MainSpecialtySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MainSpecialtyFilter
    # permission_classes = [ IsAuthenticated ]
    
    
class SpecialtyView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Specialty.objects.all().order_by("-academic_year")
    serializer_class = SpecialtySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecialtyFilter
    # permission_classes = [ IsAuthenticated ]


class MainCourseView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = MainCourse.objects.all().order_by("-created_at")
    serializer_class = MainCourseSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MainCourseFilter

   
class CourseView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = CourseSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter
    # permission_classes = [ IsAuthenticated ]
        


class LevelView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Level.objects.all().order_by("-created_at")
    serializer_class = LevelSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LevelFilter
    # permission_classes = [ IsAuthenticated ]


class ResultView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Result.objects.all().order_by("-created_at")
    serializer_class = ResultSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ResultFilter
    # permission_classes = [ IsAuthenticated ]


class PublishView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Publish.objects.all().order_by("-created_at")
    serializer_class = PublishSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PublishFilter
    # permission_classes = [ IsAuthenticated ]
    
        
class CampusView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Campus.objects.all().order_by("-created_at")
    serializer_class = CampusSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'name', 'region',)
    
        
class SchoolInfoView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SchoolInfo.objects.all().order_by("-created_at")
    serializer_class = SchoolInfoSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'school_name',)
    
        
class SchoolIdentificationView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SchoolIdentification.objects.all().order_by("-created_at")
    serializer_class = SchoolIdentificationSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'school_name',)
    
        
class SysCategoryView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SysCategory.objects.all().order_by("name")
    serializer_class = SysCategorySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'name',)
    
        
class SysConstantView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = SysConstant.objects.all().order_by("name")
    serializer_class = SysConstantSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'name',)
        

class SemesterView(ViewSet):
    # permission_classes = [ IsAuthenticated ]

    def list(self, request):
        if self.request.method.lower() != "get":
            return self.queryset
        results = Result.objects.all().values("course__semester").values_list("course__semester", flat=True).distinct()
        semester = list(results)

        return Response({ 
            "count": len(semester),
            "results": semester
        })
    

class MySpecialtiesView(ViewSet):
    # permission_classes = [ IsAuthenticated ]

    def update(self, request, pk=None):
        print(145, pk)
        # if self.request.method.lower() != "get":
        #     return self.queryset
        specialties = Specialty.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(specialties)

        return Response({ 
            "count": len(acad),
            "results": acad
        })
    

class AcademicYearView(ViewSet):
    # permission_classes = [ IsAuthenticated ]

    def list(self, request):
        if self.request.method.lower() != "get":
            return self.queryset
        specialties = Specialty.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(specialties)

        return Response({ 
            "count": len(acad),
            "results": acad
        })