from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from back.utils import get_query, querydict_to_dict, CustomPagination
from .serializers import (
    Domain, MainSpecialty, Specialty, MainCourse, Course, Level, Result, 
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from user_control.models import check_permission


class KpiDomainView(ModelViewSet):
    http_method_names = ["get",]
    queryset = Domain.objects.all().order_by("-id")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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
    

class KpiMainSpecialtyView(ModelViewSet):
    http_method_names = ["get",]
    queryset = MainSpecialty.objects.all().order_by("-id")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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


class KpiSpecialtyView(ModelViewSet):
    http_method_names = ["get",]
    queryset = Specialty.objects.all().order_by("-academic_year")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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


class KpiMainCourseView(ModelViewSet):
    http_method_names = ["get",]
    queryset = MainCourse.objects.all().order_by("-id")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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


class KpiCourseView(ModelViewSet):
    http_method_names = ["get",]
    queryset = Course.objects.all().order_by("-id")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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
    

class KpiLevelView(ModelViewSet):
    http_method_names = ["get",]
    queryset = Level.objects.all().order_by("-id")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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


class KpiResultView(ModelViewSet):
    http_method_names = ["get",]
    queryset = Result.objects.all().order_by("-id")
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
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
    
