from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from back.utils import *
from django.db.models import Q
from django.db import IntegrityError
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from app_control.serializers import *
from django.shortcuts import redirect


# GET RESOURCES


class ViewTeacherGet(ViewSet):
    http_method_names = ["get" ]
    permission_classes = [ IsAuthenticated ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        model = param.pop("model", None)
        searchField = param.pop("searchField", None)
        searchFieldArray = param.pop("searchField[]", None)
        value = param.pop("value", None)
        valueArray = param.pop("value[]", None)
        page = param.pop("page", None)
        l = param.pop("fieldList[]", None)
        json = param.pop("json", False)
        # dictionary = param.pop("dict", False)
        exact = param.pop("exact", False)
        data = CustomUser.objects.filter(is_superuser=False).exclude(role="student").order_by("-id")

        pagination = 100
        previous = False
        next = False

        count = data.count()
        serializer = CustomUserSerializer(data, many=True)
        if page:
            if int(page) == 1: 
                start = 0
                end = int(page) * pagination
            else: 
                start = (int(page) - 1) * pagination
                end = int(page) * pagination
            data = data[start:end]
            if (count >= end):
                next=True
            else:
                next=False
            if start > 0:
                previous = True

  
        if l:
            return Response({ 
                "count": count,
                "next": next,
                "previous": previous,
                "results": data.values_list(*l),
            })
        elif (json == "yes"):
            return Response({ 
                "count": count,
                "next": next,
                "previous": previous,
                "results": serializer.data,
            })
        return Response({ 
            "count": count,
            "next": next,
            "previous": previous,
            "results": data.values_list(),
        })
    
  

class ViewGet(ViewSet):
    http_method_names = ["get" ]
    permission_classes = [ IsAuthenticated ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        model = param.pop("model", None)
        searchField = param.pop("searchField", None)
        searchFieldArray = param.pop("searchField[]", None)
        value = param.pop("value", None)
        valueArray = param.pop("value[]", None)
        page = param.pop("page", None)
        l = param.pop("fieldList[]", None)
        json = param.pop("json", False)
        # dictionary = param.pop("dict", False)
        exact = param.pop("exact", False)

        if (model == "CustomUser"):
            data = CustomUser.objects.filter(is_superuser=False).order_by("-id")
        elif (model == "UserProfile"):
            data = UserProfile.objects.all().order_by("-id")
        elif (model == "Specialty"):
            data = UserActivity.objects.all().order_by("-id")
        elif (model == "UserActivity"):
            data = UserActivity.objects.all().order_by("-id")
        elif (model == "Program"):
            data = Program.objects.all().order_by("-id")

        pagination = 100
        previous = False
        next = False

        if searchField:
            try:
                if value:
                    query = get_query(value, [searchField])
                    data = data.filter(query)
            except:
                pass
        elif searchFieldArray:
            try:
                if valueArray:
                    if (exact == "true"):
                        query = get_query_exact(valueArray, searchFieldArray)
                    else:
                        query = get_query(valueArray, searchFieldArray)
                    data = data.filter(query)
            except:
                pass
        count = data.count()
        if page:
            if int(page) == 1: 
                start = 0
                end = int(page) * pagination
            else: 
                start = (int(page) - 1) * pagination
                end = int(page) * pagination
            data = data[start:end]
            if (count >= end):
                next=True
            else:
                next=False
            if start > 0:
                previous = True
        if json == "yes":
            if (model == "CustomUser"):
                serializer = CustomUserSerializer(data, many=True)
            if (model == "UserProfile"):
                serializer = UserProfileSerializer(data, many=True)
            if (model == "Program"):
                serializer = ProgramSerializer(data, many=True)
  
        if l:
            return Response({ 
                "count": count,
                "next": next,
                "previous": previous,
                "results": data.values_list(*l),
            })
        elif (json == "yes"):
            return Response({ 
                "count": count,
                "next": next,
                "previous": previous,
                "results": serializer.data,
            })
        return Response({ 
            "count": count,
            "next": next,
            "previous": previous,
            "results": data.values_list(),
        })
    
  

# GET REVERSE RESOURCES

class ViewGetReverse(ViewSet):
    http_method_names = ["get", ]
    permission_classes = [ IsAuthenticated, ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        model = param.pop("model", None)
        page = param.pop("page", None)
        searchField = param.pop("searchField", None)
        searchFieldTwo = param.pop("searchFieldTwo", None)
        searchFieldArray = param.pop("searchField[]", None)
        value = param.pop("value", None)
        valueTwo = param.pop("valueTwo", None)
        valueArray = param.pop("value[]", None)

        l = param.pop("fieldList[]", None)

        pagination = 100
        previous = False
        next = False

        if (model == "UserProfile_Specialty"):
            ''' GETTING SPECIALTIES OF ALL USER-PROFILES OF A CUSTOMUSER'''
            userprofiles_qs = UserProfile.objects.filter(user__id=value).order_by("id")
            data = Specialty.objects.filter(userprofile_specialty__in=list(userprofiles_qs)).distinct()
        elif (model == "MainSpecialty"):
            data = UserProfile.objects.all().order_by("-id")
        elif (model == "Specialty"):
            data = UserActivity.objects.all().order_by("-id")


        if searchField:
            try:
                if value:
                    query = get_query_exact(value, [searchField])
                    data = data.filter(query)
            except:
                pass
        if searchFieldArray:
            try:
                if valueArray:
                    query = get_query_exact(valueArray, searchFieldArray)
                    data = data.filter(query)
            except:
                pass
        if searchFieldTwo:
            try:
                if valueTwo:
                    query = get_query_exact(valueTwo, searchFieldTwo)
                    data = data.filter(query)
            except:
                pass
        count = data.count()
        if page:
            if int(page) == 1: 
                start = 0
                end = int(page) * pagination
            else: 
                start = (int(page) - 1) * pagination
                end = int(page) * pagination
            data = data[start:end]
            if (count >= end):
                next=True
            else:
                next=False
            if start > 0:
                previous = True
        if l:
            return Response({ 
                "count": count,
                "next": next,
                "previous": previous,
                "results": data.values_list(*l),
            })
        return Response({ 
            "count": count,
            "next": next,
            "previous": previous,
            "results": data.values_list(),
        })
    


# CREATE RESOURCES

class ViewPost(ViewSet):
    http_method_names = ["post" ]
    permission_classes = [ IsAuthenticated ]

    def create(self, request):
        data = request.data["payload"]
        user = request.user
        model = data.pop("model", None)
        active = data.pop("active", None)
        if (active ):
            data = {**data, active: False, "updated_by_id": user.id}
            if (active == "false"):
                data = {**data, active: False, "updated_by_id": user.id}
                return
            if (active == "False"):
                data = {**data, active: False, "updated_by_id": user.id}
                return
            if (active == False):
                data = {**data, active: False, "updated_by_id": user.id}
                return
        else:
            data = {**data, active: True, "updated_by_id": user.id}

        if (model == "CustomUser"):
            serializer = CustomUserSerializer(data=data) 

        if (model == "UserProfile"):
            serializer = UserProfileSerializer(data=data) 

        if (model == "Program"):
            serializer = ProgramSerializer(data=data) 

        elif (model == "UserActivity"):
            serializer = UserActivitySerializer(data=data)
        
        if serializer.is_valid():
            try:
                serializer.save()
                UserActivity.objects.create(
                    username=user.username,
                    action="Created " + model,
                )
                return Response({"success": serializer.data }) 
            except IntegrityError as e:
                return Response({"errors": e.args[0] })  
        return Response({"errors": serializer.errors })  



# UPDATE RESOURCES

class ViewPut(ViewSet):
    http_method_names = ["put" ]
    permission_classes = [ IsAuthenticated ]

    def update(self, request, pk=None):
        data = request.data["payload"]
        user = request.user
        model = data.pop("model", None)
        active = data.pop("active", None)
        if (active == False):
            data = {**data, "active": False, "updated_by_id": user.id}
        if (active == True):
            data = {**data, "active": True, "updated_by_id": user.id}
        # return

        if (model == "CustomUser"):
            object = CustomUser.objects.get(id=pk)
            serializer = CustomUserSerializer(data=data, instance=object)
            item = object.username

        if (model == "UserProfile"):
            object = UserProfile.objects.get(id=pk)
            serializer = UserProfileSerializer(data=data, instance=object)
            item = object.user.username

        elif (model == "UserActivity"):
            object = UserActivity.objects.get(id=pk)
            serializer = UserActivitySerializer(data=data, instance=object)
            item = object.username

        elif (model == "Program"):
            object = Program.objects.get(id=pk)
            serializer = ProgramSerializer(data=data, instance=object)
            item = object.name
        
        if serializer.is_valid():
            serializer.save()
            UserActivity.objects.create(
                username=user.username,
                action="Updated" + model,
                item=item,
            )
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors })  
    


# Delete User Resources
class ViewDelete(ViewSet):
    http_method_names = ["delete" ]
    permission_classes = [ IsAuthenticated ]

    def delete(self, request, pk=None):
        data = request.data["payload"]
        user = request.user
        model = data.pop("model", None)
        active = data.pop("active", None)
        if (active == False):
            data = {**data, "active": False, "updated_by_id": user.id}
        if (active == True):
            data = {**data, "active": True, "updated_by_id": user.id}
        # return

        if (model == "CustomUser"):
            object = CustomUser.objects.delete(id=pk)
            serializer = CustomUserSerializer(data=data, instance=object)

        if (model == "UserProfile"):
            object = UserProfile.objects.delete(id=pk)
            serializer = UserProfileSerializer(data=data, instance=object)

        if (model == "Program"):
            object = Program.objects.delete(id=pk)
            serializer = ProgramSerializer(data=data, instance=object)

        elif (model == "UserActivity"):
            object = UserActivity.objects.delete(id=pk)
            serializer = UserActivitySerializer(data=data, instance=object)
        
        if serializer.is_valid():
            serializer.save()
            UserActivity.objects.create(
                username=user.username,
                action="Deleted" + model,
                item=item,
            )
            return Response({"success": serializer.data })  
        return Response({"errors": serializer.errors }) 

    

# GET USER BY USERNAME OR MATRICLE

class ViewGetUser(ViewSet):
    http_method_names = ["get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        username = param.pop("username", None)
        search = param.pop("searchField", None)
        value = param.pop("value", None)
        print(param)

        if username:
            try:
                user = CustomUser.objects.get(username=username)
            except:
                try:
                    user = CustomUser.objects.get(matricle=username)
                except:
                    user = False
            if user:
                return Response({ "success": {"matricle": user.matricle, "username": user.username} })
        if search:
            try:
                user = CustomUser.objects.get(email=value)
            except:
                return Response({ "error": "No Account with this Email! Contact Admin" })
            if user:
                return Response({ "results": 
                    {
                        "matricle": user.matricle, 
                        "username": user.username,
                        "email": user.email
                    } 
                })
        
        return Response({ "error": "Invalid Credentials" })
        
        
def user_verify_email(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if not user.email_confirmed:
        user.email_confirmed = True
        user.save()
        return redirect("https://resultbrains.econneq.com")
    else:
        return redirect("https://resultbrains.econneq.com")
        
        
        