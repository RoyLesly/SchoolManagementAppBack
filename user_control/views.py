from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group, Permission
from .models import check_permission, UserProfile, PasswordToken, Appearance
from app_control.serializers import UserProfileSerializer, UserProfileLecturerSerializer, UserProfileStudentSerializer
from .serializers import (
    UserCreateSerializer, UserUpdateSerializer, CustomUser, CustomUserSerializer, LogoutSerialiser,
    LoginSerialiser, UpdatePasswordUserSerializer, ResetPasswordUserSerializer, UserActivities, 
    ForgotPasswordSerializer, UserActivitiesSerializer, GetUserSerializer, CreatePasswordUserSerializer,
    GroupSerializer, PermissionSerializer, AssignGroupsToUserSerializer, AppearanceSerializer,
    AssignPermissionsToGroupSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from datetime import datetime
from back.utils import create_access_token, create_refresh_token, get_query, CustomPagination
from back.custom_methods import IsAuthenticatedCustom
from django.utils import timezone
from datetime import timedelta
from user_control.functions import send_token_to_email
import random
from rest_framework.authentication import get_authorization_header


def add_user_activity(user, action):
    UserActivities.objects.create(
        # user_id=user.id,
        username=user.username,
        action=action
    )


class GroupView(ModelViewSet):

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


class UserCRUDView(ModelViewSet):

    '''THIS VIEWSET CRUD FOR CUSTOMUSER'''

    http_method_names = ["get", "post", "put", "delete"]
    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer
    serializer_class_create = UserCreateSerializer
    serializer_class_read = GetUserSerializer
    serializer_class_update = UserUpdateSerializer
    pagination_class = CustomPagination       # This limits to 100
    # permission_classes = [ IsAuthenticatedCustom ]

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
    
    def create(self, request):
        perm_check = "user_control.add_customuser"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        valid_request = self.serializer_class_create(data=request.data["payload"])

        try:
            if valid_request.is_valid():
                if CustomUser.objects.filter(username=request.data["payload"]["username"]):
                    return Response( {"errors": "UserName Exist Already"} )
            else:
                return Response( {"errors": valid_request.errors} )
        except:
            return Response( {"errors": valid_request.errors} )
        
        try:
            CustomUser.objects.create(**valid_request.validated_data)
        except:
            return Response( {"errors": "Server Error"} )

        add_user_activity(request.user, "added new user")

        return Response(
            {"success": "User Created Successfully"},
            status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        perm_check = "user_control.change_customuser"
        if (request.data["payload"]["updated_by_id"] < 1):
            return Response({"errors": "User Not Loggin" }) 
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
         
        object = self.get_object()
        serializer = self.serializer_class_update(data=request.data["payload"], instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data })            
        return Response({"errors": serializer.errors })  
    
    def destroy(self, request, *args, **kwargs):
        perm_check = "user_control.delete_customuser"
        check_permission(request.data["payload"]["deleted_by_id"], perm_check)
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        if not CustomUser.objects.get(id=request.data["payload"]["deleted_by_id"]).is_superuser:
            return Response({"errors": "Contact Systems Administrator" }) 
        object = self.get_object()
        if object.is_superuser:
            return Response({ "errors": "Cannot Delete This User"})
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "User May Contain Profile " }) 
    

class LoginView(ModelViewSet):
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerialiser

    def create(self, request):
        valid_request = self.serializer_class(data=request.data["payload"])
        if not valid_request.is_valid():
            return Response({"errors": valid_request.errors })
                    
        user = authenticate(
            username=valid_request.validated_data["username"],
            password=valid_request.validated_data.get("password", None)
        )
        if not user:
            return Response(
                {"errors": "Invalid Username or Password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        access = create_access_token(user.id, 10)
        refresh = create_refresh_token(user.id, 1)
        user.last_login = datetime.now()
        user.save()

        response = Response()
        response.set_cookie(key="refresh", value=refresh, httponly=True)
        response.data = {
            "success" : {
                "refresh": refresh, 
                "user": {
                    "id": user.id, 
                    "token": access, 
                    "username": user.username, 
                    "role": user.role, 
                    "is_active": user.is_active,
                    "last_login": user.last_login
                }
            }
        }
        add_user_activity(user, "logged in")
        return response
    

class LogoutView(ModelViewSet):
    http_method_names = ["post"]
    serializer_class = LogoutSerialiser

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        if not valid_request.is_valid():
            raise Exception(valid_request.errors)
        response = Response()
        response.delete_cookie('jwt')
        response.data = { "message": "success" }
        try:
            user = CustomUser.objects.get(id = valid_request.validated_data["user_id"]),
            return response
        except:
            raise Exception("User ID Not Found")


class PasswordView(ModelViewSet):
    serializer_class_create = CreatePasswordUserSerializer
    serializer_class_update = UpdatePasswordUserSerializer
    serializer_class_reset = ResetPasswordUserSerializer
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()

    def create(self, request):

        # UPDATING PASSWORD
        if (request.data["payload"]["action"] == "updating_password"):
            valid_request = self.serializer_class_update(data=request.data["payload"])
            if (request.data["payload"]["updated_by_id"] < 1):
                return Response({ "errors": "Not Logged In" })
            if not valid_request.is_valid():
                raise Exception(valid_request.errors)
            user = CustomUser.objects.filter(
                id=valid_request.validated_data["user_id"])
            if not user:
                raise Exception("User with Id not Found")
            username = user[0].username
            user2 = authenticate(
                username=username,
                password=valid_request.validated_data.get("password", None)
            )
            if user2:
                user2.set_password(valid_request.validated_data["newPassword"])
                user2.save()
                add_user_activity(user[0], "updated password")
                return Response({"success": "User Password Updated"})
            if not user2:
                return Response({"error": "Operation Error"})
            

        # CREATING PASSWORD
        if (request.data["payload"]['action'] == "creating_password"):
            valid_request = self.serializer_class_create(data=request.data["payload"])
            if not valid_request.is_valid():
                return Response({ "errors": valid_request.errors })
            
            user = CustomUser.objects.filter(id=valid_request.validated_data["user_id"])[0]
            if not user:
                return Response({ "error": "User Not Found With This ID" })
            else:
                if (len(user.password) > 4):
                    return Response({ "errors": "User Has Password, Consider Updating.f.." })
                user.set_password(valid_request.validated_data["password"])
                user.save()
                add_user_activity(user, "updated password")
                return Response({ "success": "Password Creation Successful !!!" })
            

        # RESTIING PASSWORD
        if (request.data["payload"]["action"] == "resetting_password"):
            valid_request = self.serializer_class_reset(data=request.data["payload"])
            if (request.data["payload"]["updated_by_id"] < 1):
                return Response({ "errors": "Not Logged In" })
            if not valid_request.is_valid():
                return Response({ "errors": valid_request.errors })
            try:
                account = CustomUser.objects.get(id=valid_request.validated_data["account_to_reset_id"])
            except:
                return Response({"errors": "Not Valid Account"})
            user = CustomUser.objects.get(id=request.data["payload"]["updated_by_id"])
            
            try:
                if account.is_superuser:
                    if not user.is_superuser:
                        return Response({"errors": "Contact Admin"})
                    account.set_password(valid_request.validated_data["password"])
                    account.save()
                    add_user_activity(user, "reset password for " + account.username)
                    return Response({"success": "Reset Password - " + account.username})
            except:
                return Response({"errors": "Operation Failed"})
           

class PasswordForgotView(ModelViewSet):
    serializer_class = ForgotPasswordSerializer
    http_method_names = ["post"]    

    def create(self, request):
        all_tokens = PasswordToken.objects.all()
        for tok in all_tokens:
            if (timezone.now() - tok.updated_at) > timedelta(minutes=30):
                tok.expired = True
                tok.save()

        # FORGOTTEN PASSWORD
        valid_request = self.serializer_class(data=request.data["payload"])
        if not valid_request.is_valid():
            raise Exception(valid_request.errors)
        
        if (request.data["payload"]["auth_method"] == "username"):
            all_users = CustomUser.objects.filter( username=valid_request.validated_data["data"] )
            if not all_users:
                return Response({"error": "No Account Found !!!"})
            all_profile = UserProfile.objects.filter( user=all_users[0] )
            if not all_profile:
                return Response({"error": "No Account Found !!!"})
            profile = all_profile[0]
            
        if (request.data["payload"]["auth_method"] == "email"):
            all_profile = UserProfile.objects.filter( email=valid_request.validated_data["data"] )
            if not all_profile:
                return Response({"error": "No Account Found !!!"})
            profile = all_profile[0]
        t = random.randint(100000, 999999)

        if not profile:
            return Response({"error": "No Account Found !!!"})
        all_tokens = PasswordToken.objects.filter(user_profile=profile).order_by("-created_at")
        if not all_tokens:
            # token = PasswordToken.objects.create(
            #     user_profile=profile,
            #     token=t,
            #     expired=False,
            #     sent_mail=False
            # )
            # token.save()
            try:
                token = PasswordToken.objects.create(
                    user_profile=profile,
                    token=t,
                    expired=False,
                    sent_mail=False
                )
                token.save()
                try:
                    send_token_to_email(token)
                except:
                    raise Exception("NOT SET MAIL")
            except:
                raise Exception("NOT SET MAIL")
        else:
            token = all_tokens[0]
            if token.expired:
                token.token = t
                token.expired = False
                token.sent_mail = False
                token.save()
                send_token_to_email(token)
                raise Exception("New Token Generated and Sending")
            if not token.expired:
                if token.sent_mail:
                    raise Exception("Sent Already, Check Email")
                if not token.sent_mail:
                    send_token_to_email(token)
                    raise Exception("Resending Token")
        return Response({"success": "Check Your Email"})
            

class MeView(ModelViewSet):
    serializer_class = CustomUserSerializer
    http_method_names = ["get"]
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticatedCustom, )

    def list(self, request):
        data1 = CustomUser.objects.get(id=request.user.id)
        user = {
            "id": data1.id,
            "username": data1.username,
            "last_login": data1.last_login,
            "created_at": data1.created_at,
            "role": data1.role,
            "email": data1.email,
        }
        return Response(user)


class UserActivitiesView(ModelViewSet):
    serializer_class = UserActivitiesSerializer
    http_method_names = ["get"]
    queryset = UserActivities.objects.all()
    permission_classes = (IsAuthenticatedCustom, )
    pagination_class = CustomPagination

    class Meta:
        ordering = ("-created_at", )         
    

class UserProfilesView(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = UserProfile.objects.all().order_by("-created_at")
    serializer_class = UserProfileSerializer
    serializer_class_lecturer = UserProfileLecturerSerializer
    serializer_class_student = UserProfileStudentSerializer
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
        perm_check = "user_control.add_userprofile"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        if (request.data["payload"]["role"] == "teacher"):
            serializer = self.serializer_class_lecturer(data=data)
        if (request.data["payload"]["role"] == "student"):
            serializer = self.serializer_class_student(data=data)
        else:
            serializer = self.serializer_class(data=data, instance=object)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data )
            return Response({"success": serializer.data })  
        raise Exception(serializer.errors)        
    
    def update(self, request, *args, **kwargs):
        perm_check = "user_control.change_userprofile"      
        check_permission(request.data["payload"]["updated_by_id"], perm_check)
        data = request.data["payload"]
        batch_update = data["multiple"]
        prof = self.get_object()
        if not batch_update:
            if (request.data["payload"]["role"] == "teacher"):
                serializer = self.serializer_class_lecturer(data=data, instance=prof)
            if (request.data["payload"]["role"] == "student"):
                serializer = self.serializer_class_student(data=data, instance=prof)
            else:
                serializer = self.serializer_class(data=data, instance=prof)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": serializer.data}) 
            return Response({"errors": serializer.errors}) 
        else:
            if (request.data["payload"]["role"] == "student"):
                print("updating multiple_student")
                all_profiles_with_user_id = UserProfile.objects.filter(user_id=prof.user.id)
                print("updating multiple_student 2")
                for p in all_profiles_with_user_id:
                    print("updating multiple_student 4")
                    serializer = self.serializer_class_student(data=data, instance=p)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response({"errors": serializer.errors}) 
            else:
                print("updating multiple_teacher")
                all_profiles_with_user_id = UserProfile.objects.filter(user_id=prof.user.id)
                for p in all_profiles_with_user_id:
                    serializer = self.serializer_class(data=data, instance=p)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response({"errors": serializer.errors}) 
            return Response({"success": serializer.data}) 
        
    
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


class AppearanceView(ModelViewSet):
    http_method_names = ["get", "put", "delete"]
    queryset = Appearance.objects.all().order_by("-created_at")
    serializer_class = AppearanceSerializer
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
       
    
    def update(self, request, *args, **kwargs):
        if (request.data["payload"]["updated_by_id"] < 1):
            raise Exception("User Not Loggin")  
        data = request.data["payload"]
        app = self.get_object()
        serializer = self.serializer_class(data=data, instance=app)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data}) 
        return Response({"errors": serializer.errors})         
    
    def destroy(self, request, *args, **kwargs):
        if (request.data["payload"]["deleted_by_id"] < 1):
            raise Exception("User Not Loggin")  
        object = self.get_object()
        try:
            object.delete()
            return Response({"success": "Deleted" })            
        except:
            return Response({"errors": "Appearance Delete Failed !!!" }) 


class AssignGroupsToUserView(ModelViewSet):
    http_method_names = ["put"]
    queryset = CustomUser.objects.all()
    serializer_class = AssignGroupsToUserSerializer

    def update(self, request, pk=None):
        data = request.data["payload"]
        object = self.get_object()
        perm_check = "auth.change_group"
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        serializer = self.serializer_class(data=data, instance=object)
        # raise Exception(data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data}) 
        raise Exception(serializer.errors)
        return Response({"errors": serializer.errors }) 
    

class AssignPermissionsGroupView(ModelViewSet):
    http_method_names = ["put"]
    queryset = Group.objects.all()
    serializer_class = AssignPermissionsToGroupSerializer

    def update(self, request, pk=None):
        perm_check = "auth.change_permission"        
        check_permission(request.data["payload"]["created_by_id"], perm_check)
        data = request.data["payload"]
        object = self.get_object()
        serializer = self.serializer_class(data=data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": serializer.data}) 
        raise Exception(serializer.errors)
        return Response({"errors": serializer.errors }) 