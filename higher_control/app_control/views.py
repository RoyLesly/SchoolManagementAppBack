from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .filters import *
from django_filters import rest_framework as filters
from tenant.views import BaseModelViewSet


class SchoolIdentificationHigherView(BaseModelViewSet):
    http_method_names = ["post", "put", "delete"]
    queryset = SchoolIdentificationHigher.objects.all()
    serializer_class = SchoolIdentificationHigherSerializer


class SchoolInfoHigherView(BaseModelViewSet):
    http_method_names = ["post", "put", "delete"]
    queryset = SchoolInfoHigher.objects.all()
    serializer_class = SchoolInfoHigherSerializer


class DomainView(BaseModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class FieldView(BaseModelViewSet):
    http_method_names = ["post", "put", "delete"]
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class MainSpecialtyView(BaseModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = MainSpecialty.objects.all().order_by("-created_at")
    serializer_class = MainSpecialtySerializer
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
   
class CourseUploadView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = CourseUpload.objects.all().order_by("-course")
    serializer_class = CourseUploadSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = CourseUploadFilter
    # permission_classes = [ IsAuthenticated ]
   
class CourseModuleView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = CourseModule.objects.all().order_by("-course")
    serializer_class = CourseModuleSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseModuleFilter
    # permission_classes = [ IsAuthenticated ]
   
class CourseModuleDetailView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = CourseModuleDetail.objects.all().order_by("-created_at")
    serializer_class = CourseModuleDetailSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseModuleDetailFilter
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