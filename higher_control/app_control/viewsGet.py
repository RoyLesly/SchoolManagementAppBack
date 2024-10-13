from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q, Sum, F, Case, When, Value
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .filters import *
from django_filters import rest_framework as filters


class GetDomainView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Domain.objects.all().order_by("domain_name")
    serializer_class = GetDomainSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DomainFilter
    permission_classes = [ IsAuthenticated ]

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


class GetFieldView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Field.objects.all().order_by("-created_at")
    serializer_class = GetFieldSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FieldFilter

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


class GetMainSpecialtyView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = MainSpecialty.objects.all().order_by("-created_at")
    serializer_class = GetMainSpecialtySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MainSpecialtyFilter
    permission_classes = [ IsAuthenticated ]

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
    
    
class GetSpecialtyView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Specialty.objects.all().order_by("-academic_year")
    serializer_class = GetSpecialtySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecialtyFilter
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


class GetMainCourseView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = MainCourse.objects.all().order_by("-created_at")
    serializer_class = GetMainCourseSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MainCourseFilter

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
        

   
class GetCourseView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = GetCourseSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter
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


class GetLevelView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Level.objects.all().order_by("-created_at")
    serializer_class = GetLevelSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LevelFilter
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


class GetResultView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Result.objects.all().order_by("-created_at")
    serializer_class = GetResultSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ResultFilter
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


class GetResultTranscriptView(ViewSet):
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
    
        
class GetCampusView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = Campus.objects.all().order_by("-created_at")
    serializer_class = GetCampusSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'name', 'region',)

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
    
        
class GetSchoolInfoView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = SchoolInfo.objects.all().order_by("-created_at")
    serializer_class = GetSchoolInfoSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SchoolInfoFilter
    # permission_classes = [ IsAuthenticated ]
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
    
        
class GetSchoolIdentificationView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = SchoolIdentification.objects.all().order_by("-created_at")
    serializer_class = GetSchoolIdentificationSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SchoolIdentificationFilter
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