from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from higher_control.user_control.models import *
from datetime import datetime
import importlib
# from rest_framework.authentication import SessionAuthentication


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enfore_csrf(self, request):
#         return


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        user.last_login = datetime.now()
        user.password_set = True
        user.save()
        token = super().get_token(user)
        token["username"] = user.username
        token["role"] = user.role
        token["is_superuser"] = user.is_superuser
        token["permissions"] = list(user.user_permissions.values_list("codename", flat=True))
        token["dept"] = list(user.dept.all().values_list("name", flat=True))
        token["page"] = list(user.page.all().values_list("name", flat=True))
        token["school"] = list(user.school.all().values_list("id", flat=True))            
        return token



class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = "__all__"
        dept = 1


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer(read_only=True)

    class Meta:
        model = Permission
        fields = "__all__"
        dept = 1


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = "__all__"
        dept = 1


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(ROLE_CHOICES)


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    role = serializers.ChoiceField(ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        exclude = ("password",)
        # fields = "__all__"
        dept = 1


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PageSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class CampusTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = importlib.import_module("higher_control.app_control").models.Campus
        fields = "__all__"


class SchoolInfoTwoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    campus = CampusTwoSerializer(read_only=True, required=False)
    campus_id = serializers.CharField(required=True)
    module_schoolinfo = importlib.import_module("higher_control.app_control").models.SchoolInfo

    class Meta:
        model = importlib.import_module("higher_control.app_control").models.SchoolInfo
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    schoolinfo = importlib.import_module("higher_control.app_control").models.SchoolInfo
    school = serializers.PrimaryKeyRelatedField(many=True, queryset=schoolinfo.objects.all(), required=False)
    dept = DepartmentSerializer(many=True, read_only=True, required=False)
    page = PageSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = CustomUser
        exclude = ("password",)

    def create(self, validated_data):
        # campus = validated_data.pop("created_campus")
        school = validated_data.pop("school")
        print(school, 113)
        m = CustomUser.objects.create(**validated_data)
        for s in school:
            m.school.add(s)
        # for c in campus:
        #     m.created_campus.add(c)
        return m
    

class PreInscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreInscription
        fields = ("__all__")


class GetUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    user_permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = CustomUser
        fields = ("__all__")

class CheckUserSerialiser(serializers.Serializer):
    username = serializers.CharField(required=True)


class AssignGroupsToUserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Group.objects.all(), required=True)
    password = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ("__all__")


class AssignPermissionsToGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Permission.objects.all(), required=True)

    class Meta:
        model = Group
        fields = ("__all__")


class UpdatePasswordUserSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=False)


class CreatePasswordUserSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    confirm_password = serializers.CharField(required=False)


class ResetPasswordUserSerializer(serializers.Serializer):
    updated_by_id = serializers.CharField(required=True)
    account_to_reset_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class AppearanceSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.CharField(required=True, write_only=True)
    dark_mode = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = Appearance
        fields = "__all__"
        dept = 1


class ProgramSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Program
        fields = "__all__"
        dept = 1





# LIST SERIALIZERS =======================================================================================================




class GetDepartmentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetPageSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetProgramSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetUserProfileSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)
    user__id = serializers.IntegerField(read_only=True)
    user__username = serializers.CharField(read_only=True)
    user__first_name = serializers.CharField(read_only=True)
    user__last_name = serializers.CharField(read_only=True)
    user__full_name = serializers.CharField(read_only=True)
    user__matricle = serializers.CharField(read_only=True)
    user__username = serializers.CharField(read_only=True)
    user__sex = serializers.CharField(read_only=True)
    user__dob = serializers.CharField(read_only=True)
    user__pob = serializers.CharField(read_only=True)
    user__address = serializers.CharField(read_only=True)
    user__telephone = serializers.CharField(read_only=True)
    user__email = serializers.CharField(read_only=True)
    specialty__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    specialty__academic_year = serializers.CharField(read_only=True)
    specialty__tuition = serializers.CharField(read_only=True)
    specialty__level__level = serializers.IntegerField(read_only=True)
    specialty__main_specialty__field__field_name = serializers.CharField(read_only=True)
    specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    specialty__school__campus__name = serializers.CharField(read_only=True)
    specialty__school__campus__region = serializers.CharField(read_only=True)
    specialty__school__school_name = serializers.CharField(read_only=True)
    specialty__school__campus__id = serializers.CharField(read_only=True)
    program__id = serializers.CharField(read_only=True)
    program__name = serializers.CharField(read_only=True)
    active = serializers.CharField(read_only=True)
    session = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetAppearanceSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user__id = serializers.CharField(read_only=True)
    user__full_name = serializers.CharField(read_only=True)
    user__matricle = serializers.CharField(read_only=True)    
    dark_mode = serializers.CharField(read_only=True)    
    lang = serializers.CharField(read_only=True)    
    created_by__full_name = serializers.CharField(read_only=True)


class GetUserActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user__id = serializers.CharField(read_only=True)
    user__full_name = serializers.CharField(read_only=True)
    user__matricle = serializers.CharField(read_only=True)    
    action = serializers.CharField(read_only=True)    
    item = serializers.CharField(read_only=True)    
    details = serializers.CharField(read_only=True)    
    created_by__full_name = serializers.CharField(read_only=True)


class GetSchoolInfoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    school_name = serializers.CharField(read_only=True)
    school_name_short = serializers.CharField(read_only=True)
    school_type = serializers.CharField(read_only=True)
    main_campus = serializers.CharField(read_only=True)
    campus_id = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    campus__name = serializers.CharField(read_only=True)
    town = serializers.CharField(read_only=True)
    campus__region = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    region = serializers.CharField(read_only=True)
    po_box = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    niu = serializers.CharField(read_only=True)
    telephone = serializers.CharField(read_only=True)
    website = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)



class GetCustomUserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)
    matricle = serializers.CharField(read_only=True)
    user_name = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    sex = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    dob = serializers.CharField(read_only=True)
    pob = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    telephone = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    is_active = serializers.CharField(read_only=True)
    is_superuser = serializers.CharField(read_only=True)
    last_login = serializers.CharField(read_only=True)
    school__id = serializers.CharField(read_only=True)
    school__campus__id = serializers.CharField(read_only=True)
    dept = GetDepartmentSerializer(many=True, read_only=True, required=False)
    page = GetPageSerializer(many=True, read_only=True)
    school = GetSchoolInfoSerializer(many=True, read_only=True)


class GetPreInscriptionSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    registration_number = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    sex = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    telephone = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    pob = serializers.CharField(read_only=True)
    dob = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    emergency_name = serializers.CharField(read_only=True)
    emergency_town = serializers.CharField(read_only=True)
    emergency_telephone = serializers.CharField(read_only=True)
    academic_year = serializers.CharField(read_only=True)
    specialty_one = serializers.CharField(read_only=True)
    specialty_two = serializers.CharField(read_only=True)
    campus = serializers.CharField(read_only=True)
    program = serializers.CharField(read_only=True)
    level = serializers.CharField(read_only=True)
    session = serializers.CharField(read_only=True)
    admission_status = serializers.BooleanField(read_only=True)
    action = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
