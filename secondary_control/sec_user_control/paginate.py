from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import TruncYear, TruncMonth, TruncDay
from django.db.models import Count, Sum
from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from rest_framework.response import Response
from .models import check_permission, UserProfile
from app_control.serializers import UserProfileSerializer
from .serializers import (
    UserCreateSerializer, UserUpdateSerializer, CustomUser, UserActivity, 
    UserActivitySerializer, GetUserSerializer, GroupSerializer, PermissionSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from back.utils import *
from back.custom_methods import IsAuthenticatedCustom


def add_user_activity(user, action):
    UserActivity.objects.create(
        # user_id=user.id,
        username=user.username,
        action=action
    )


class PageGroupView(ModelViewSet):

    '''THIS VIEWSET CRU FOR GROUP'''

    http_method_names = [ "post", "get", "put"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        perm_check = "view_group"
        if self.request.method.lower() != "get":
            return self.queryset
        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)
        results = self.queryset

        if keyword:
            search_fields = ("")
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        return results
    

class PagePermissionView(ModelViewSet):

    '''THIS VIEWSET GET FOR PERMISSIONS'''

    http_method_names = [ "post", "get", "put"]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)
        results = self.queryset

        if keyword:
            search_fields = ("")
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        return results


class PageUserCRUDView(ModelViewSet):

    '''THIS VIEWSET CRUD FOR CUSTOMUSER'''

    http_method_names = ["get", "post", "put", "delete"]
    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer
    serializer_class_create = UserCreateSerializer
    serializer_class_read = GetUserSerializer
    serializer_class_update = UserUpdateSerializer
    pagination_class = CustomPagination       # This limits to 100
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        kpi = data.pop("kpi", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
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
        if kpi:
            p = Q(**{"%s" % searchField: value})
            try:
                results = results.filter(p)
            except:
                pass
        
        return results
    

class PageUserActivityView(ModelViewSet):
    serializer_class = UserActivitySerializer
    http_method_names = ["get"]
    queryset = UserActivity.objects.all()
    permission_classes = (IsAuthenticatedCustom, )
    pagination_class = CustomPagination

    class Meta:
        ordering = ("-created_at", )         
    

class PageUserProfilesStudentsView(ModelViewSet):
    http_method_names = ["get",]
    queryset = UserProfile.objects.all().order_by("-id").filter(user__role="student")
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        results = self.queryset
        return results 
    

class PageUserProfilesLecturersView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = UserProfile.objects.all().order_by("-created_at").filter(user__role="teacher")
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [ IsAuthenticated, ]

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        results = self.queryset
        return results 


class PageUserProfilesView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = UserProfile.objects.all().order_by("-id")
    serializer_class = UserProfileSerializer
    pagination_class = CustomPagination       # This limits to 100
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [ IsAuthenticated, ]

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset
        data = querydict_to_dict(self.request.query_params)
        kpi = data.pop("kpi", None)
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
            print(results.count(), 4)
        if kpi:
            p = Q(**{"%s" % searchField: value})
            try:
                results = results.filter(p)
            except:
                pass
        return results 
    

    def create(self, request, *args, **kwargs):
        data = request.data["payload"]
        if (data["created_by_id"] == 0):
            raise Exception("User Not Login") 
        perm_check = "user_control.add_userprofile"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        if (request.data["payload"]["role"] == "teacher"):
            serializer = self.serializer_class(data=data)
        if (request.data["payload"]["role"] == "student"):
            serializer = self.serializer_class(data=data)
        else:
            serializer = self.serializer_class(data=data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors)        
    
    def update(self, request, *args, **kwargs):
        perm_check = "user_control.change_userprofile"      
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        data = request.data["payload"]
        prof = self.get_object()
        serializer = self.serializer_class(data=data, instance=prof)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data}) 
        return Response({"errors": serializer.errors}) 
        
    
    def destroy(self, request, *args, **kwargs):
        perm_check = "user_control.delete_userprofile"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "Profile May Contain Results !!!" }) 


    

class KpiCustomUserCountsView(ViewSet):
    http_method_names = ["get", ]
    permission_classes = [ IsAuthenticated, ]

    def list(self, request):
        results = CustomUser.objects.filter(is_superuser=False)
        all_users = results.count()
        non_active_users = results.filter(is_active=False).count()
        active_users = results.filter(is_active=True).count()
        admin_users = results.filter(role="admin").count()
        lecturer_users = results.filter(role="teacher").count()
        student_users = results.filter(role="student").count()
       
        return Response({ 
            "count": { 
                "all_users": all_users,
                "admin_users": admin_users,
                "lecturer_users": lecturer_users,
                "student_users": student_users,
                "active_users": active_users,
                "non_active_users": non_active_users,
            } 
        })
    

class KpiYearlyModelCountListView(ViewSet):
    http_method_names = ["get", ]
    permission_classes = [ IsAuthenticated, ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        param.pop("page", None)
        model = param.pop("model", CustomUser)
        searchField = param.pop("searchField", None)
        value = param.pop("value", None)
        results = 0

        if (model == "CustomUser"):
            metrics = { "yearly_created_at": Count('id') }
            data = CustomUser.objects.filter(is_superuser=False)
            if searchField:
                try:
                    if value:
                        query = get_query(value, [searchField])
                        data = data.filter(query)
                except:
                    pass
            results = data.filter(is_superuser=False).values("created_at__year").annotate(**metrics)

            l = (list(results))
            a = [d['created_at__year'] for d in l]
            b = [d['yearly_created_at'] for d in l]
            results = [a, b]
        elif (model == "UserProfile"):
            metrics = { "academic_year_reg": Count('id') }
            data = UserProfile.objects.filter(user__role="student")
            if searchField:
                try:
                    if value:
                        query = get_query(value, [searchField])
                        data = data.filter(query)
                        print(query, "Query")
                except:
                    pass
            results = data.filter(user__role="student").values("specialty__academic_year").annotate(**metrics)
            print(results)
            l = (list(results))
            a = [d['specialty__academic_year'] for d in l]
            a = ["No Specialty" if v is None else v for v in a]
            b = [d['academic_year_reg'] for d in l]
            results = [a, b]
            print(results, "UP=================================>")
        elif (model == "UserActivity"):
            model = UserActivity
            metrics = { "monthly_actions": Count('id') }
            results = model.objects.values("created_at__month").annotate(**metrics)
        return Response({ "list": results })
    

class KpiUserProfileSpecialtyCountOneView(ViewSet):
    http_method_names = ["get", ]
    permission_classes = [ IsAuthenticated, ]

    def list(self, request):
        user_profiles_with_specialties = UserProfile.objects.exclude(specialty=None)
        specialty_names = list(set([f.specialty.main_specialty.specialty_name for f in user_profiles_with_specialties]))
        academic_years = list(set([f.specialty.academic_year for f in user_profiles_with_specialties]))
        levels = list(set([f.specialty.level.level for f in user_profiles_with_specialties]))
        data = []
        for s in specialty_names:
            item = []
            for y in academic_years:
                item2 = []
                for l in levels:
                    a = user_profiles_with_specialties.filter(specialty__academic_year=y, specialty__main_specialty__specialty_name=s, specialty__level__level=l)
                    b = { l: a.count()}
                    item2.append(b)
                item.append({y: item2})
            data.append({s: item})
       
        return Response({ 
            "count": { 
                "list_specialty": specialty_names,
                "academic_years": academic_years,
                "list": data,
            } 
        })
    

class KpiUserProfileSpecialtyCountTwoView(ViewSet):
    http_method_names = ["get", ]
    permission_classes = [ IsAuthenticated, ]

    def list(self, request):
        user_profiles_with_specialties = UserProfile.objects.exclude(specialty=None).exclude(active=False)
        specialty_names = list(set(user_profiles_with_specialties.values_list("specialty__main_specialty__specialty_name", flat=True)))         # USE value_list() & SET
        academic_years = list(set([f.specialty.academic_year for f in user_profiles_with_specialties]))    
        data = []
        for s in specialty_names:
            item = []
            for y in academic_years:
                a = user_profiles_with_specialties.filter(specialty__main_specialty__specialty_name=s, specialty__academic_year=y)
                b = { y: a.count()}
                item.append(b)
            data.append({s: item})
       
        return Response({ 
            "count": { 
                "list_specialty": specialty_names,
                "academic_years": academic_years,
                "list": data,
            } 
        })


class KpiUserControlListView(ViewSet):
    http_method_names = ["get", ]
    permission_classes = [ IsAuthenticated, ]

    def list(self, request):
        data = querydict_to_dict(self.request.query_params)
        data.pop("page", None)
        kpi = data.pop("kpi", None)
        searchField = data.pop("searchField", None)
        searchFieldArray = data.pop("searchField[]", None)
        value = data.pop("value", None)
        valueArray = data.pop("value[]", None)
        model = data.pop("model", CustomUser)
        results = 0

        if (model == "CustomUser"):
            model = CustomUser
        elif (model == "UserProfile"):
            model = UserProfile
        elif (model == "UserActivity"):
            model = UserActivity

        if searchField:
            if kpi == "false":
                try:
                    if value:
                        query = get_query(value, [searchField])
                        results = model.objects.filter(query)
                except:
                    pass
            if kpi == "true":
                p = Q(**{"%s" % searchField: value})
                try:
                    results = model.objects.filter(p)
                except:
                    pass 
            metrics = { "academic_year_reg": Count('id') }
            o = model.objects.values("specialty__academic_year").annotate(**metrics)
        if searchFieldArray:
            try:
                if valueArray:
                    query = get_query(valueArray, searchFieldArray)
                    results = model.objects.filter(query).count()
            except:
                pass       
        return Response({ "count": results })
    

