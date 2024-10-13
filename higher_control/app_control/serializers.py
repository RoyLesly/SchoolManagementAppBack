from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *
from higher_control.user_control.serializers import CustomUserSerializer, GetCustomUserSerializer
from higher_control.user_control.models import UserProfile, Program


class AssignPermissionsToGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Permission.objects.all(), required=True)

    class Meta:
        model = Group
        fields = ("__all__")


class SchoolIdentificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolIdentification
        fields = ("__all__")


class SchoolInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolInfo
        fields = ("__all__")


class CampusSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Campus
        fields = "__all__"


class SchoolInfoSerializer(serializers.ModelSerializer):
    campus = CampusSerializer(read_only=True)
    campus_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = SchoolInfo
        fields = "__all__"


class DomainSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Domain
        fields = "__all__"
        dept = 1


class FieldSerializer(serializers.ModelSerializer):
    domain = DomainSerializer(read_only=True)
    domain_id = serializers.CharField(write_only=True, required=True)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Field
        fields = "__all__"
        dept = 1


class MainSpecialtySerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    field_id = serializers.CharField(write_only=True, required=True)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MainSpecialty
        fields = "__all__"
        dept = 1


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = "__all__"
        dept = 1


class SpecialtySerializer(serializers.ModelSerializer):
    school = SchoolInfoSerializer(read_only=True)
    school_id = serializers.CharField(write_only=True, required=True)
    main_specialty = MainSpecialtySerializer(read_only=True)
    main_specialty_id = serializers.CharField(write_only=True, required=True)
    level = LevelSerializer(read_only=True)
    level_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Specialty
        fields = "__all__"
        dept = 1


class MainCourseSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MainCourse
        fields = "__all__"
        dept = 1


class CourseSerializer(serializers.ModelSerializer):
    main_course = MainCourseSerializer(read_only=True)
    main_course_id = serializers.CharField(write_only=True, required=True)
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=True)
    assigned_to = CustomUserSerializer(read_only=True)
    assigned_to_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Course
        fields = "__all__"
        dept = 1


class ProgramSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Program
        fields = "__all__"
        dept = 1


class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True, required=True)
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=False)
    program = ProgramSerializer(read_only=True)
    program_id = serializers.CharField(write_only=True, required=False)
    code = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = "__all__"
        dept = 2


class ResultSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.CharField(write_only=True, required=False)
    student = UserProfileSerializer(read_only=True)
    student_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Result
        fields = "__all__"
        dept = 1


class PublishSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer(read_only=True)
    specialty_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Publish
        fields = "__all__"
        dept = 1


class SysCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SysCategory
        fields = "__all__"


class SysConstantSerializer(serializers.ModelSerializer):
    sys_category = SysCategorySerializer(read_only=True)
    sys_category_id = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = SysConstant
        fields = "__all__"






# LIST SERIALIZERS =======================================================================================================




class GetSchoolIdentificationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    back_end = serializers.CharField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetSchoolInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    school_name = serializers.CharField(read_only=True)
    school_name_short = serializers.CharField(read_only=True)
    school_type = serializers.CharField(read_only=True)
    director = serializers.CharField(read_only=True)
    main_campus = serializers.CharField(read_only=True)
    campus_id = serializers.IntegerField(read_only=True)
    address = serializers.CharField(read_only=True)
    campus__name = serializers.CharField(read_only=True)
    town = serializers.CharField(read_only=True)
    campus__region = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    region = serializers.CharField(read_only=True)
    po_box = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    niu = serializers.CharField(read_only=True)
    telephone_one = serializers.CharField(read_only=True)
    telephone_two = serializers.CharField(read_only=True)
    website = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetCampusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    region = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)


class GetDomainSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    domain_name = serializers.CharField(read_only=True)


class GetFieldSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    field_name = serializers.CharField(read_only=True)
    domain__id = serializers.IntegerField(read_only=True)
    domain__domain_name = serializers.CharField(read_only=True)


class GetMainSpecialtySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    specialty_name = serializers.CharField(read_only=True)
    specialty_name_short = serializers.CharField(read_only=True)
    field__id = serializers.IntegerField(read_only=True)
    field__field_name = serializers.CharField(read_only=True)
    field__domain__id = serializers.IntegerField(read_only=True)
    field__domain__domain_name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetSpecialtySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    main_specialty__id = serializers.IntegerField(read_only=True)
    main_specialty__specialty_name = serializers.CharField(read_only=True)
    main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    main_specialty__field__domain__name = serializers.CharField(read_only=True)
    main_specialty__field__id = serializers.IntegerField(read_only=True)
    main_specialty__field__field_name = serializers.CharField(read_only=True)
    school__id = serializers.IntegerField(read_only=True)
    academic_year = serializers.CharField(read_only=True)
    level__id = serializers.IntegerField(read_only=True)
    level__level = serializers.CharField(read_only=True)
    tuition = serializers.IntegerField(read_only=True)
    registration = serializers.IntegerField(read_only=True)
    payment_one = serializers.IntegerField(read_only=True)
    payment_two = serializers.IntegerField(read_only=True)
    payment_three = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetMainCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    main_course__id = serializers.IntegerField(read_only=True)
    main_course__course_name = serializers.CharField(read_only=True)
    specialty__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    specialty__main_specialty__field__domain__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__field__domain__domain_name = serializers.CharField(read_only=True)
    specialty__school__campus__region = serializers.CharField(read_only=True)
    specialty__school__campus__name = serializers.CharField(read_only=True)
    course_code = serializers.CharField(read_only=True)
    course_type = serializers.CharField(read_only=True)
    semester = serializers.CharField(read_only=True)
    course_credit = serializers.CharField(read_only=True)
    completed = serializers.CharField(read_only=True)
    assigned = serializers.BooleanField(read_only=True)
    paid = serializers.CharField(read_only=True)
    assigned_to__id = serializers.CharField(read_only=True)
    assigned_to__full_name = serializers.CharField(read_only=True)
    hours = serializers.IntegerField(read_only=True)
    hours_left = serializers.IntegerField(read_only=True)
    date_assigned = serializers.CharField(read_only=True)
    created_by__id = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    main_course__course_name = serializers.CharField(read_only=True)
    specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    specialty__academic_year = serializers.CharField(read_only=True)
    specialty__level__level = serializers.IntegerField(read_only=True)
    specialty__id = serializers.IntegerField(read_only=True)
                    

class GetResultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student__id = serializers.IntegerField(read_only=True)
    student__user__first_name = serializers.CharField(read_only=True)
    student__user__full_name = serializers.CharField(read_only=True)
    student__specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    student__specialty__academic_year = serializers.CharField(read_only=True)
    student__specialty__level__level = serializers.CharField(read_only=True)
    student__specialty__school__school_name = serializers.CharField(read_only=True)
    student__specialty__school__address = serializers.CharField(read_only=True)
    student__specialty__school__region = serializers.CharField(read_only=True)
    course__id = serializers.IntegerField(read_only=True)
    course__specialty__id = serializers.IntegerField(read_only=True)
    course__main_course__course_name = serializers.CharField(read_only=True)
    course__semester = serializers.CharField(read_only=True)
    course__assigned_to__id = serializers.IntegerField(read_only=True)
    course__assigned_to__full_name = serializers.CharField(read_only=True)
    course__course_code = serializers.CharField(read_only=True)
    course__course_credit = serializers.IntegerField(read_only=True)

    # ca = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)
    # exam = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)
    # resit = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)
    # average = serializers.DecimalField(max_digits=4, decimal_places=1, read_only=True)
    ca = serializers.IntegerField(read_only=True)
    exam = serializers.IntegerField(read_only=True)
    resit = serializers.IntegerField(read_only=True)
    average = serializers.IntegerField(read_only=True)

    validated = serializers.BooleanField(read_only=True)
    publish_ca = serializers.IntegerField(read_only=True)
    publish_exam = serializers.IntegerField(read_only=True)
    publish_resit = serializers.IntegerField(read_only=True)
    closed = serializers.CharField(read_only=True)
    active = serializers.CharField(read_only=True)
    created_by__id = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)
                    


class GetPublishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    specialty__id = serializers.IntegerField(read_only=True)
    specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    specialty__academic_year = serializers.CharField(read_only=True)
    specialty__level__level = serializers.CharField(read_only=True)
    semester = serializers.CharField(read_only=True)
    ca = serializers.BooleanField(read_only=True)
    exam = serializers.BooleanField(read_only=True)
    resit = serializers.BooleanField(read_only=True)
    portal_ca = serializers.BooleanField(read_only=True)
    portal_exam = serializers.BooleanField(read_only=True)
    portal_resit = serializers.BooleanField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)
                    

class GetLevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    level = serializers.CharField(read_only=True)
                    

class GetSysCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
                    

class GetSysConstantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    sys_category__id = serializers.IntegerField(read_only=True)
    sys_category__name = serializers.CharField(read_only=True)
    
    