from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializersGet import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .filters import *
from django_filters import rest_framework as filters


class BaseGetViewSet(ModelViewSet):
    """
    A base viewset to handle common functionality for 'GET' requests.
    """
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        queryset = super().get_queryset()

        # Handle field selection dynamically
        if fieldList:
            fieldList = fieldList.split(',')
            queryset = queryset.values(*fieldList)

        return queryset

    def paginate_queryset(self, queryset):
        param = querydict_to_dict(self.request.query_params)
        nopage = param.pop("nopage", None)
        if nopage:
            return None
        return super().paginate_queryset(queryset)

    def perform_query_optimization(self, queryset, related_fields=None):
        """
        Perform query optimizations like select_related or prefetch_related.
        """
        if related_fields:
            queryset = queryset.select_related(*related_fields)
        return queryset


class GetSchoolIdentificationView(BaseGetViewSet):
    http_method_names = ["get"]
    queryset = SchoolIdentificationHigher.objects.all().order_by("-created_at")
    serializer_class = GetSchoolIdentificationSerializer
    filterset_class = SchoolIdentificationHigherFilter

         
class GetSchoolInfoView(BaseGetViewSet):
    http_method_names = ["get"]
    queryset = SchoolInfoHigher.objects.all().order_by("-created_at")
    serializer_class = GetSchoolInfoSerializer
    filterset_class = SchoolInfoHigherFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        # Optimize query by including related foreign keys
        queryset = self.perform_query_optimization(queryset, related_fields=["school_identification"])
        return queryset


class GetDomainView(BaseGetViewSet):
    http_method_names = ["get"]
    queryset = Domain.objects.all().order_by("domain_name")
    serializer_class = GetDomainSerializer
    filterset_class = DomainFilter
    # permission_classes = [IsAuthenticated]  # Uncomment if authentication is needed


class GetFieldView(BaseGetViewSet):
    http_method_names = ["get"]
    queryset = Field.objects.all().order_by("-created_at")
    serializer_class = GetFieldSerializer
    filterset_class = FieldFilter


class GetMainSpecialtyView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = MainSpecialty.objects.all().order_by("-created_at")
    serializer_class = GetMainSpecialtySerializer
    filterset_class = MainSpecialtyFilter
    # permission_classes = [ IsAuthenticated ]
    
    
class GetSpecialtyView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Specialty.objects.all().order_by("-academic_year")
    serializer_class = GetSpecialtySerializer
    filterset_class = SpecialtyFilter
    # permission_classes = [ IsAuthenticated ]


class GetMainCourseView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = MainCourse.objects.all().order_by("-created_at")
    serializer_class = GetMainCourseSerializer
    filterset_class = MainCourseFilter


class GetCourseView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = GetCourseSerializer
    filterset_class = CourseFilter
    # permission_classes = [ IsAuthenticated ]
    

class GetCourseUploadView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = CourseUpload.objects.all().order_by("-created_at")
    serializer_class = GetCourseUploadSerializer
    filterset_class = CourseUploadFilter
    # permission_classes = [ IsAuthenticated ]
    
    
class GetCourseModuleView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = CourseModule.objects.all().order_by("-created_at")
    serializer_class = GetCourseModuleSerializer
    filterset_class = CourseModuleFilter
    # permission_classes = [ IsAuthenticated ]
    
    
class GetCourseModuleDetailView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = CourseModuleDetail.objects.all().order_by("-created_at")
    serializer_class = GetCourseModuleDetailSerializer
    filterset_class = CourseModuleDetailFilter
    # permission_classes = [ IsAuthenticated ]


class GetLevelView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Level.objects.all().order_by("-created_at")
    serializer_class = GetLevelSerializer
    filterset_class = LevelFilter
    # permission_classes = [ IsAuthenticated ]


class GetResultView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Result.objects.all().order_by("-created_at")
    serializer_class = GetResultSerializer
    filterset_class = ResultFilter
    # permission_classes = [ IsAuthenticated ]


class GetResultTranscriptView(BaseGetViewSet):
    http_method_names = [ "get" ]
    queryset = Result.objects.all().order_by("-created_at")
    serializer_class = GetResultSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ResultFilter

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        fieldList = param.pop("fieldList", None)
        q = self.queryset
        if fieldList:
            response = {}
            # fieldList = fieldList.split(',')
            def gradePoint(av):
                gd = 0
                if av:
                    if av > 39.9:
                        gd = 1.0
                    if av > 44.9:
                        gd = 1.5
                    if av > 49.9:
                        gd = 2.0
                    if av > 54.9:
                        gd = 2.5
                    if av > 59.9:
                        gd = 3.0
                    if av > 69.9:
                        gd = 3.5
                    if av > 79.9:
                        gd = 4.0
                return gd
            def grade(av):
                gd = "F"
                if av:
                    if av > 39.9:
                        gd = "D"
                    if av > 44.9:
                        gd = "D+"
                    if av > 49.9:
                        gd = "C"
                    if av > 54.9:
                        gd = "C+"
                    if av > 59.9:
                        gd = "B"
                    if av > 69.9:
                        gd = "B+"
                    if av > 79.9:
                        gd = "A"
                return gd

            if "student__specialty__academic_year" in param.keys():
                q = q.filter(student__specialty__academic_year=param["student__specialty__academic_year"])
            if "student__id" in param.keys():
                q = q.filter(student__id=param["student__id"])
            if "course__semester" in param.keys():
                q = q.filter(course__semester=param["course__semester"])
            i = []
            for r in q:
                rav = 0
                if r.average:
                    rav = r.average
                tot = 0
                gp = gradePoint(r.average)
                wp = r.course.course_credit * gp
                tot = rav * r.course.course_credit
                i.append({
                        "id": r.id, 
                        "wp": wp, 
                        "gp": gp,
                        "tot": tot,
                        "gd": grade(rav),
                        "course__main_course__course_name": r.course.main_course.course_name,
                        "course__semester": r.course.semester,
                        "course__course_code": r.course.course_code,
                        "course__course_credit": r.course.course_credit,
                        "ca": r.ca,
                        "exam": r.exam,
                        "resit": r.resit,
                        "average": rav,
                        "validated": r.validated,
                    })
            average_x_wp = 0
            total_credit = 0
            total_credit_attempted = 0
            total_credit_earned = 0
            for r in i:
                total_credit = total_credit + r["course__course_credit"]
                average_x_wp = average_x_wp + r["tot"]
            for a in q.filter(average__gt = 49.9):
                total_credit_earned = total_credit_earned + a.course.course_credit
            for a in q.filter(average__gt = 0):
                total_credit_attempted = total_credit_attempted + a.course.course_credit
            gp = 0
            if total_credit_attempted:
                gp = average_x_wp/(total_credit_attempted * 25)
            response = {
                "gp": gp,
                "total_credit": total_credit,
                "total_credit_attempted": total_credit_attempted,
                "total_credit_earned": total_credit_earned,
                "count": len(i),
                "results": i,
            }
            return Response(response)
        return Response({ 
            "count": q.values().count(),
            "results": q.values(),
        })


class GetPublishView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Publish.objects.all().order_by("-created_at")
    serializer_class = GetPublishSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PublishFilter
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
    

class GetSysCategoryView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = SysCategory.objects.all().order_by("name")
    serializer_class = GetSysCategorySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SysCategoryFilter
    # permission_required = ('app_control.view_schoolinfo')

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
        
        
class GetSysConstantView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = SysConstant.objects.all().order_by("name")
    serializer_class = GetSysConstantSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SysConstantFilter
    # permission_required = ('app_control.view_schoolinfo')

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
        

class GetSemesterView(ViewSet):
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
    

class GetMySpecialtiesView(ViewSet):

    def update(self, request, pk=None):
        specialties = Specialty.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(specialties)

        return Response({ 
            "count": len(acad),
            "results": acad
        })
    

class GetAcademicYearView(ViewSet):
    '''my code '''
    #my code '''
    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        school = param.pop("school", None)
        specialties = Specialty.objects.filter(school__id=school).values("academic_year").values_list("academic_year", flat=True).distinct()
        # if school:
        #     specialties = Specialty.objects.filter(school__id=school).values("academic_year").values_list("academic_year", flat=True).distinct()
        # else:
        #     specialties = Specialty.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(specialties)

        return Response({ 
            "count": len(acad),
            "results": acad
        })