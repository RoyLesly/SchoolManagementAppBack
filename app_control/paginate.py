from rest_framework.viewsets import ViewSet, ModelViewSet
from back.utils import get_query, CustomPagination, querydict_to_dict
from django.db.models import Q
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class PageDomainView(ModelViewSet):
    http_method_names = ["get", ]
    queryset = Domain.objects.all().order_by("-created_at")
    serializer_class = DomainSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        results = self.queryset

        if searchField:
            if value:
                query = get_query(value, [searchField])
                results = results.filter(query)
        if searchFieldArray:
            if valueArray:
                query = get_query(valueArray, searchFieldArray)
                print(query, "MY QUERY")
                results = results.filter(query)

        return results
 

class PageMainSpecialtyView(ModelViewSet):
    http_method_names = ["get",]
    queryset = MainSpecialty.objects.all().order_by("-created_at")
    serializer_class = MainSpecialtySerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        results = self.queryset

        if searchField:
            if value:
                query = get_query(value, [searchField])
                results = results.filter(query)
        if searchFieldArray:
            if valueArray:
                query = get_query(valueArray, searchFieldArray)
                print(query, "MY QUERY")
                results = results.filter(query)
        return results
  
    
class PageSpecialtyView(ModelViewSet):
    http_method_names = ["get", ]
    queryset = Specialty.objects.all().order_by("-academic_year")
    serializer_class = SpecialtySerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        results = self.queryset

        if searchField:
            if value:
                query = get_query(value, [searchField])
                results = results.filter(query)
        if searchFieldArray:
            if valueArray:
                query = get_query(valueArray, searchFieldArray)
                print(query, "MY QUERY")
                results = results.filter(query)
        return results
    

class PageMainCourseView(ModelViewSet):
    http_method_names = ["get"]
    queryset = MainCourse.objects.all().order_by("-created_at")
    serializer_class = MainCourseSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        results = self.queryset

        if searchField:
            if value:
                query = get_query(value, [searchField])
                results = results.filter(query)
        if searchFieldArray:
            if valueArray:
                query = get_query(valueArray, searchFieldArray)
                print(query, "MY QUERY")
                results = results.filter(query)
        return results


class PageCourseView(ModelViewSet):
    http_method_names = ["get", ]
    queryset = Course.objects.all().order_by("specialty")
    serializer_class = CourseSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        results = self.queryset

        if searchField:
            if value:
                query = get_query(value, [searchField])
                results = results.filter(query)
        if searchFieldArray:
            if valueArray:
                query = get_query(valueArray, searchFieldArray)
                results = results.filter(query)
        return results
    

class PageResultView(ModelViewSet):
    http_method_names = ["get", ]
    queryset = Result.objects.all().order_by("-created_at")
    serializer_class = ResultSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        try:
            if (searchFieldArray[0] == "page"):
                page = valueArray[0]
        except:
            page = data.pop("page", None)

        results = self.queryset

        if searchField:
            try:
                if value:
                    query = get_query(value, [searchField])
                    results = results.filter(query)
            except:
                pass
        if searchFieldArray:
            try:
                if valueArray:
                    query = get_query(valueArray, searchFieldArray)
                    results = results.filter(query)
            except:
                pass
        return results
  

class PageLevelView(ModelViewSet):
    http_method_names = ["get",]
    queryset = Level.objects.all().order_by("-created_at")
    serializer_class = LevelSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)
        results = self.queryset#.filter(**data)

        if keyword:
            search_fields = ("")
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        return results



# KPI SECTION
class KpiAppControlView(ViewSet):
    http_method_names = ["get", ]

    def list(self, request):
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        kpi = data.pop("kpi", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        model = data.pop("model", Domain)
        results = 0

        if (model == "Domain"):
            model = Domain
        elif (model == "MainSpecialty"):
            model = MainSpecialty
        elif (model == "Specialty"):
            model = Specialty
        elif (model == "MainCourse"):
            model = MainCourse
        elif (model == "Course"):
            model = Course
        elif (model == "Level"):
            model = Level
        elif (model == "Result"):
            model = Result

        if not kpi:
            if searchField:
                try:
                    if value:
                        query = get_query(value, [searchField])
                        results = model.objects.filter(query).count()
                except:
                    pass
            if searchFieldArray:
                try:
                    if valueArray:
                        query = get_query(valueArray, searchFieldArray)
                        results = model.objects.filter(query).count()
                except:
                    pass
        if kpi:
            p = Q(**{"%s" % searchField: value})
            try:
                results = model.objects.filter(p).count()
            except:
                pass        
        return Response({ "count": results })
    


# DROPDOWNS SECTION
class DropdownsView(ViewSet):
    http_method_names = ["get", ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        model = param.pop("model", None)
        searchField = param.pop("searchField", None)

        if (model == "Domain"):
            data = Domain.objects.values_list("id", "domain_name")
        elif (model == "MainSpecialty"):
            data = MainSpecialty.objects.values_list("id", "specialty_name")
        elif (model == "Specialty"):
            data = Specialty.objects.values_list("id", "main_specialty__domain__id", "main_specialty__specialty_name", "academic_year", "level__level") # index[1] => domain_id
        elif (model == "MainCourse"):
            data = MainCourse.objects.values_list("id", "course_name")
        elif (model == "Course"):
            data = Course.objects.values_list("id", "main_course__course_name", "specialty__main_specialty__specialty_name", "specialty__level__level")
        elif (model == "Level"):
            data = Level.objects.values_list("id", "level")

        return Response({ "dropdown": data })
    
