from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from back.utils import get_query, CustomPagination
from .serializers import (
    Domain, DomainSerializer, MainSpecialty, Specialty, MainCourse, Course, Level,
    MainSpecialtySerializer, SpecialtySerializer, MainCourseSerializer, CourseSerializer,
    Result, ResultSerializer, LevelSerializer
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from user_control.models import check_permission


class DomainView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Domain.objects.all().order_by("-created_at")
    serializer_class = DomainSerializer
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_domain"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_specialty"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })            
        return Response({"errors": serializer.errors })  

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_domain"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": object.delete() }) 
    

class MainSpecialtyView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = MainSpecialty.objects.all().order_by("-created_at")
    serializer_class = MainSpecialtySerializer
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_mainspecialty"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_mainspecialty"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })      

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_mainspecialty"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "May Contain Some Classes" })  
        
    
class SpecialtyView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Specialty.objects.all().order_by("-academic_year")
    serializer_class = SpecialtySerializer
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_specialty"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_specialty"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Logged in")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })      

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_specialty"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "May Conatin Courses / Subjects" })  
        

class MainCourseView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = MainCourse.objects.all().order_by("-created_at")
    serializer_class = MainCourseSerializer
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_maincourse"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_maincourse"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })      

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_maincourse"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "May Contain Courses" })  
        

class CourseView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Course.objects.all().order_by("specialty")
    serializer_class = CourseSerializer
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_course"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_course"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })      

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_course"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "Error" })  
        

class ResultView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Result.objects.all().order_by("-created_at")
    serializer_class = ResultSerializer
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_result"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_result"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })      

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_result"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "Error" })  
        

class LevelView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
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
    
    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "app_control.add_level"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors) 
    
    def update(self, request, *args, **kwargs):
        perm_check = "app_control.change_level"
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })      

    def destroy(self, request, *args, **kwargs):
        perm_check = "app_control.delete_level"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "Error" })  
        

