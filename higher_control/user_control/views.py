from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import Group, Permission
from .models import *
from back.middleware import *
from back.utils import *
from higher_control.user_control.serializers import *
from higher_control.app_control.serializers import UserProfileSerializer
from .serializers import *
from rest_framework_simplejwt.views import (TokenObtainPairView,)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django_filters import rest_framework as filters
from .filters import *
from higher_control.noti_control.views import add_user_activity
from django.shortcuts import redirect


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [IsAuthenticatedWithAPIKey]
    pass



class GroupView(ModelViewSet):

    '''THIS VIEWSET CRU FOR GROUP'''

    http_method_names = [ "post", "get", "put"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
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
    
    def create(self, request, *args, **kwargs):
        perm_check = "auth.add_group"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
            
        if (request.data["payload"]["created_by_id"] == 0):
            raise Exception("User Not Loggin") 
        serializer = self.serializer_class(data=request.data["payload"])

        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data }) 
        raise Exception(serializer.errors)
        return Response({"errors": serializer.errors })  

    def update(self, request, *args, **kwargs):
        perm_check = "auth.change_group"
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
        perm_check = "auth.delete_group"
        check_permission(request.data["payload"]["created_by_id"], perm_check)

        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin") 
        object = self.get_object()
        try:
            object.delete()  
            return Response({"success": "DELETED" })     
        except:
            return Response({"errors": "NOT DELETED"}) 
       

class PermissionView(ModelViewSet):

    '''THIS VIEWSET CRU FOR PERMISSIONS'''

    http_method_names = [ "post", "get", "put"]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
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
    
    def create(self, request, *args, **kwargs):
        perm_check = "auth.add_permission"
        check_permission(request.data["payload"]["created_by_id"], perm_check)        
        if (request.data["payload"]["created_by_id"] == 0):
            raise Exception("User Not Loggin")                     
        serializer = self.serializer_class(data=request.data["payload"])
        if serializer.is_valid():
            raise Exception(serializer.data)
            serializer.save()
            return Response({"success": serializer.data }) 
        return Response({"errors": serializer.errors })  

    def update(self, request, *args, **kwargs):
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")
        perm_check = "auth.change_permission"
        check_permission(request.data["payload"]["created_by_id"], perm_check)  
        object = self.get_object()
        serializer = self.serializer_class(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })            
        return Response({"errors": serializer.errors })   
    
    def destroy(self, request, *args, **kwargs):
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin") 
        object = self.get_object()
        perm_check = "auth.delete_permission"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        try:
            object.delete()  
            return Response({"success": "DELETED" })     
        except:
            return Response({"errors": "NOT DELETED"}) 


class ProgramView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = Program.objects.all().order_by("-created_at")
    serializer_class = ProgramSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProgramFilter
    # permission_classes = [ IsAuthenticatedCustom ]


class DepartmentView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = Department.objects.all().order_by("-created_at")
    serializer_class = DepartmentSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter
    # permission_classes = [ IsAuthenticatedCustom ]


class UserProfileView(ModelViewSet):
    http_method_names = [ "post", "put", "delete"]
    queryset = UserProfile.objects.all().order_by("-created_at")
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserProfileFilter
    # permission_classes = [ IsAuthenticatedCustom ]


class CustomUserView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = CustomUser.objects.all().order_by("-full_name")
    serializer_class = CustomUserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter
    # permission_classes = [ IsAuthenticatedCustom ]


class PreInscriptionView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = PreInscription.objects.all().order_by("-full_name")
    serializer_class = PreInscriptionSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PreInscriptionFilter
    # permission_classes = [ IsAuthenticatedCustom ]


class AppearanceView(ModelViewSet):
    http_method_names = [ "post", "get", "put", "delete"]
    queryset = Appearance.objects.all().order_by("-created_at")
    serializer_class = AppearanceSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppearanceFilter
    # permission_classes = [ IsAuthenticatedCustom ]
    

class CheckPasswordView(APIView):
    http_method_names = [ "post", ]
    serializer_class = CustomUserSerializer

    def post(self, request):
        user = CustomUser.objects.filter(matricle=request.data["matricle"])
        if not user:
            return Response({"errors": "No Account Found" })
        if len(user) < 1:
            return Response({"errors": "No Account Found" })
        else:
            if user[0].password == "":
                return Response({"fail": {
                    "id": user[0].id,
                    "username": user[0].username,
                    "matricle": user[0].matricle,
                } })
            else:
                return Response({
                    "id": user[0].id,
                    "username": user[0].username,
                    "matricle": user[0].matricle,
                })
    

class CreatePasswordView(ModelViewSet):
    http_method_names = [ "put", ]
    serializer_class = CreatePasswordUserSerializer

    def update(self, request, pk=None):
        valid_request = self.serializer_class(data=request.data)
        if not valid_request.is_valid():
            raise Exception(valid_request.errors)
        user = CustomUser.objects.get(id=pk)
        if user and (valid_request.validated_data["password"] == valid_request.validated_data["confirm_password"]):
            if (len(user.password) > 4):
                return Response({ "errors": "User Has Password, Consider Updating." })
            user.set_password(valid_request.validated_data["password"])
            user.password_set == True
            user.save()
            add_user_activity(user, "created-password", "password", str(user.username) + "password-created")
            return Response({ "success": "Password Creation Successful." })
        return Response({"errors": "Wrong / No Password for User" })


class UpdatePasswordView(ModelViewSet):
    http_method_names = [ "put", ]
    serializer_class = UpdatePasswordUserSerializer

    def update(self, request):
        data = request.data["payload"]
        user = authenticate(
            username=data["username"],
            password=data.validated_data.get("password", None)
        )
        if user:
            user.set_password(data.validated_data["newPassword"])
            user.save()
            add_user_activity(user.id, "Update-Password", user.username, "update-password-for-ID:" + user.id)
            return Response({"success": "User Password Updated"})
        return Response({"errors": "Wrong / No Password for User" }) 
    

class ResetPasswordView(ModelViewSet):
    http_method_names = [ "put", ]
    serializer_class = ResetPasswordUserSerializer

    def update(self, request):
        data = request.data["payload"]
        try:
            user = CustomUser.objects.get(id=data["user_id"])
            account = CustomUser.objects.get(id=data["account_id"])
            if user.is_superuser:
                if account.is_superuser:
                    return Response({"error": "Contact Admin"})
                account.set_password(account.validated_data["password"])
                account.save()
                add_user_activity(user.id, "Reset-Password", account.username, "reset password for ID:" + account.id)
                return Response({"success": "Reset-Password-" + account.username})
            else:
                return Response({"errors": "Contact Admin"})
        except:
            return Response({"error": "Operation Failed"})  

        
def user_verify_email(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if not user.email_confirmed:
        user.email_confirmed = True
        user.save()
        return redirect("https://resultbrains.econneq.com")
    else:
        return redirect("https://resultbrains.econneq.com")
        
