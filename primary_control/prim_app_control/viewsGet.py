from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .filters import *
from django_filters import rest_framework as filters


class GetPrimaryClassRoomView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = PrimaryClassRoom.objects.all().order_by("-academic_year")
    serializer_class = GetPrimaryClassRoomSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryClassRoomFilter
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


class GetPrimaryMainSubjectView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = PrimaryMainSubject.objects.all().order_by("-created_at")
    serializer_class = GetPrimaryMainSubjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryMainSubjectFilter

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
        

   
class GetPrimarySubjectView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = PrimarySubject.objects.all().order_by("-created_at")
    serializer_class = GetPrimarySubjectSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimarySubjectFilter
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
        
   
class GetPrimaryLevelView(ModelViewSet):
    http_method_names = [ "get" ]
    queryset = PrimaryLevel.objects.all().order_by("-created_at")
    serializer_class = GetPrimaryLevelSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PrimaryLevelFilter
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


# class GetPrimaryResultView(ModelViewSet):
#     http_method_names = [ "get" ]
#     queryset = PrimaryResult.objects.all().order_by("-created_at")
#     serializer_class = GetPrimaryResultSerializer
#     parser_classes = (MultiPartParser, FormParser, JSONParser)
#     pagination_class = CustomPagination
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = PrimaryResultFilter
#     # permission_classes = [ IsAuthenticated ]

#     def get_queryset(self):
#         param = querydict_to_dict(self.request.query_params)
#         fieldList = param.pop("fieldList", None)
#         if fieldList:
#             fieldList = fieldList.split(',')
#             return self.queryset.values(*fieldList)
#         return super().get_queryset()

#     def paginate_queryset(self, queryset):
#         param = querydict_to_dict(self.request.query_params)
#         nopage = param.pop("nopage", None)
#         if nopage:
#             return None
#         return super().paginate_queryset(queryset)


# class GetPrimaryResultTranscriptView(ViewSet):
#     http_method_names = [ "get" ]
#     queryset = PrimaryResult.objects.all().order_by("-created_at")
#     serializer_class = GetPrimaryResultSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = PrimaryResultFilter

#     def list(self, request):
#         param = querydict_to_dict(self.request.query_params)
#         q = self.queryset
#         response = {}
#         def grade(av):
#             gd = "Fail"
#             if av:
#                 if av > 7.9:
#                     gd = "Poor"
#                 if av > 9.9:
#                     gd = "D"
#                 if av > 12.9:
#                     gd = "C"
#                 if av > 14.9:
#                     gd = "B"
#                 if av > 17.5:
#                     gd = "A"
#             return gd

#         if "student__classroom__academic_year" in param.keys():
#             q = q.filter(student__classroom__academic_year=param["student__classroom__academic_year"])
#         if "student__id" in param.keys():
#             q = q.filter(student__id=param["student__id"])
#         i = []
#         def checkZero(a, b):
#             if b:
#                 return round(a/b, 2)
#             return 0
#         def total_term(a, b):
#             if a > 0:
#                 if b != None:
#                     return a * b
#         def anual_av(a, b, c):
#             l = [x for x in [a, b, c] if x]
#             if l:
#                 return round(checkZero(sum(l), len(l)))
#             return None
#         def calc_total(a, b):
#             if a:
#                 return a * b
#             return 0
#         for r in q:
#             total_term_1 = total_term(r.subject.subject_coefficient, r.average_term_1)
#             total_term_2 = total_term(r.subject.subject_coefficient, r.average_term_2)
#             total_term_3 = total_term(r.subject.subject_coefficient, r.average_term_3)
#             i.append({
#                     "id": r.id, 
#                     "grade_1": grade(r.average_term_1),
#                     "grade_2": grade(r.average_term_2),
#                     "grade_3": grade(r.average_term_3),
#                     "anual_average": anual_av(r.average_term_1, r.average_term_2, r.average_term_3),
#                     "average_term_1": r.average_term_1,
#                     "average_term_2": r.average_term_2,
#                     "average_term_3": r.average_term_3,
#                     "subject_coefficient": r.subject.subject_coefficient,
#                     "total": calc_total(anual_av(r.average_term_1, r.average_term_2, r.average_term_3), r.subject.subject_coefficient),
#                     "total_1": total_term_1,
#                     "total_2": total_term_2,
#                     "total_3": total_term_3,
#                     "subject_name": r.subject.main_subject.subject_name,
#                     "subject_code": r.subject.subject_code,
#                     "seq_1": r.seq_1,
#                     "seq_2": r.seq_2,
#                     "seq_3": r.seq_3,
#                     "seq_4": r.seq_4,
#                     "seq_5": r.seq_5,
#                     "seq_6": r.seq_6,
#                 })
#         total_coef_1 = 0
#         total_coef_2 = 0
#         total_coef_3 = 0
#         total_marks_1 = 0
#         total_marks_2 = 0
#         total_marks_3 = 0
#         total_subject_attempted = 0
#         total_subject_attempted_1 = 0
#         total_subject_attempted_2 = 0
#         total_subject_attempted_3 = 0
#         total_subject_earned = 0
#         total_subject_earned_1 = 0
#         total_subject_earned_2 = 0
#         total_subject_earned_3 = 0
#         total_subject_failed = 0
#         total_subject_failed_1 = 0
#         total_subject_failed_2 = 0
#         total_subject_failed_3 = 0
#         anual_total = 0
#         total_coef = 0
#         def calTotalCoef(x, a, b):
#             if x:
#                 return a + b
#             return a
#         def calTotalMarks(x, a, b):
#             if x:
#                 return a + b
#             return a
#         for r in i:
#             total_coef_1 = calTotalCoef(r["average_term_1"], total_coef_1, r["subject_coefficient"])
#             total_coef_2 = calTotalCoef(r["average_term_2"], total_coef_2, r["subject_coefficient"])
#             total_coef_3 = calTotalCoef(r["average_term_3"], total_coef_3, r["subject_coefficient"])
#             total_marks_1 = calTotalMarks(r["average_term_1"], total_marks_1, r["total_1"])
#             total_marks_2 = calTotalMarks(r["average_term_2"], total_marks_2, r["total_2"])
#             total_marks_3 = calTotalMarks(r["average_term_3"], total_marks_3, r["total_3"])
#         for r in i:
#             if (r["average_term_1"]):
#                 total_subject_attempted_1 = total_subject_attempted_1 + 1
#                 if (r["average_term_1"] > 9.99):
#                     total_subject_earned_1 = total_subject_earned_1 + 1
#                 else:
#                     total_subject_failed_1 = total_subject_failed_1 + 1
#             if (r["average_term_2"]):
#                 total_subject_attempted_2 = total_subject_attempted_2 + 1
#                 if (r["average_term_2"] > 9.99):
#                     total_subject_earned_2 = total_subject_earned_2 + 1
#                 else:
#                     total_subject_failed_2 = total_subject_failed_2 + 1
#             if (r["average_term_3"]):
#                 total_subject_attempted_3 = total_subject_attempted_3 + 1
#                 if (r["average_term_3"] > 9.99):
#                     total_subject_earned_3 = total_subject_earned_3 + 1
#                 else:
#                     total_subject_failed_3 = total_subject_failed_3 + 1
#             anual_total = anual_total + r["total"]
#         for r in i:
#             if r["anual_average"]:
#                 total_subject_attempted = total_subject_attempted + 1
#                 total_coef = total_coef + r["subject_coefficient"]
#                 if r["anual_average"] > 9.99:
#                     total_subject_earned = total_subject_earned + 1
#                 else:
#                     total_subject_failed = total_subject_failed + 1
#         response = {
#             "total_coef": total_coef,
#             "total_coef_1": total_coef_1,
#             "total_coef_2": total_coef_2,
#             "total_coef_3": total_coef_3,
#             "anual_total": anual_total,
#             "total_marks": total_marks_1 + total_marks_2 + total_marks_3,
#             "total_marks": total_marks_1 + total_marks_2 + total_marks_3,
#             "total_marks_1": total_marks_1,
#             "total_marks_2": total_marks_2,
#             "total_marks_3": total_marks_3,
#             "average": checkZero(anual_total, total_coef),
#             "average_1": checkZero(total_marks_1, total_coef_1),
#             "average_2": checkZero(total_marks_2, total_coef_2),
#             "average_3": checkZero(total_marks_3, total_coef_3),
#             "total_subject_attempted": total_subject_attempted,
#             "total_subject_earned": total_subject_earned,
#             "total_subject_failed": total_subject_failed,
#             "total_subject_attempted_1":total_subject_attempted_1,
#             "total_subject_attempted_2":total_subject_attempted_2,
#             "total_subject_attempted_3":total_subject_attempted_3,
#             "total_subject_earned_1": total_subject_earned_1,
#             "total_subject_earned_2": total_subject_earned_2,
#             "total_subject_earned_3": total_subject_earned_3,
#             "total_subject_failed_1": total_subject_failed_1,
#             "total_subject_failed_2": total_subject_failed_2,
#             "total_subject_failed_3": total_subject_failed_3,
#             "count": len(i),
#             "results": i,
#         }
#         return Response(response)
#         # return Response({ 
#         #     "count": q.values().count(),
#         #     "results": q.values(),
#         # })



# class GetPrimaryResultClassroomView(ViewSet):
#     http_method_names = [ "get" ]
#     queryset = PrimaryResult.objects.all().order_by("-created_at")
#     serializer_class = GetPrimaryResultSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = PrimaryResultFilter

#     def list(self, request):
#         param = querydict_to_dict(self.request.query_params)
#         q = self.queryset
#         profs = []
#         subjects = []
#         subjects_names = []
#         if "student__classroom__id" in param.keys():
#             q = q.filter(student__classroom__id=param["student__classroom__id"])
#             subjects = PrimarySubject.objects.filter(classroom__id=param["student__classroom__id"])
#             subjects_names = subjects.values_list("main_subject__subject_name", flat=True)
#             profs = UserProfile.objects.filter(classroom__id=param["student__classroom__id"])
#         results = []
#         for p in profs:
#             my_res = []
#             prof_results = q.filter(student=p)
#             my_res.append(p.user.full_name)
#             for s in subjects:
#                 s_results = prof_results.filter(subject=s)
#                 name = s.main_subject.subject_name
#                 r = []
#                 if s_results:
#                     f = s_results.first()
#                     r = [name, f.seq_1, f.seq_2, f.seq_3, f.seq_4, f.seq_5, f.seq_6 ]
#                 my_res.append(r)
#             results.append(my_res)
#         return Response([subjects_names, results])



# class GetPrimaryPublishView(ModelViewSet):
#     http_method_names = [ "get" ]
#     queryset = PrimaryPublish.objects.all().order_by("-created_at")
#     serializer_class = GetPrimaryPublishSerializer
#     parser_classes = (MultiPartParser, FormParser, JSONParser)
#     pagination_class = CustomPagination
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = PrimaryPublishFilter
#     permission_classes = [ IsAuthenticated ]

#     def get_queryset(self):
#         param = querydict_to_dict(self.request.query_params)
#         fieldList = param.pop("fieldList", None)
#         if fieldList:
#             fieldList = fieldList.split(',')
#             return self.queryset.values(*fieldList)
#         return super().get_queryset()

#     def paginate_queryset(self, queryset):
#         param = querydict_to_dict(self.request.query_params)
#         nopage = param.pop("nopage", None)
#         if nopage:
#             return None
#         return super().paginate_queryset(queryset)
    

# class GetPrimaryMyClassRoomsView(ViewSet):
#     # permission_classes = [ IsAuthenticated ]

#     def update(self, request, pk=None):
#         print(145, pk)
#         # if self.request.method.lower() != "get":
#         #     return self.queryset
#         classrooms = PrimaryClassRoom.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
#         acad = list(classrooms)

#         return Response({ 
#             "count": len(acad),
#             "results": acad
#         })
    

# class GetPrimaryAcademicYearView(ViewSet):
    # permission_classes = [ IsAuthenticated ]

    def list(self, request):
        if self.request.method.lower() != "get":
            return self.queryset
        classrooms = PrimaryClassRoom.objects.all().values("academic_year").values_list("academic_year", flat=True).distinct()
        acad = list(classrooms)

        return Response({ 
            "count": len(acad),
            "results": acad
        })