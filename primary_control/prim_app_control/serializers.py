from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import *
from higher_control.user_control.serializersGet import CustomUserSerializer
from higher_control.user_control.models import UserProfile



class PrimaryLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimaryLevel
        fields = "__all__"
        dept = 1


class PrimaryClassRoomSerializer(serializers.ModelSerializer):
    # school = SchoolInfoSerializer(read_only=True)
    school_id = serializers.CharField(write_only=True, required=True)
    level = PrimaryLevelSerializer(read_only=True)
    level_id = serializers.CharField(write_only=True, required=True)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = PrimaryClassRoom
        fields = "__all__"
        dept = 1


class PrimaryMainSubjectSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = PrimaryMainSubject
        fields = "__all__"
        dept = 1


class PrimarySubjectSerializer(serializers.ModelSerializer):
    main_subject = PrimaryMainSubjectSerializer(read_only=True)
    main_subject_id = serializers.CharField(write_only=True, required=True)
    classroom = PrimaryClassRoomSerializer(read_only=True)
    classroom_id = serializers.CharField(write_only=True, required=True)
    assigned_to = CustomUserSerializer(read_only=True)
    assigned_to_id = serializers.CharField(write_only=True, required=False)
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True, required=False)
    updated_by = CustomUserSerializer(read_only=True)
    updated_by_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = PrimarySubject
        fields = "__all__"
        dept = 1


class PrimaryProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True, required=True)
    classroom = PrimaryClassRoomSerializer(read_only=True)
    classroom_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
        dept = 2


# LIST SERIALIZERS =======================================================================================================


class GetPrimaryClassRoomSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    level__id = serializers.IntegerField(read_only=True)
    level__level = serializers.CharField(read_only=True)
    level__option = serializers.CharField(read_only=True)
    domain = serializers.CharField(read_only=True)
    school__id = serializers.IntegerField(read_only=True)
    school__campus__id = serializers.IntegerField(read_only=True)
    school__school_name = serializers.CharField(read_only=True)
    school__campus__name = serializers.CharField(read_only=True)
    school__campus__region = serializers.CharField(read_only=True)
    academic_year = serializers.CharField(read_only=True)
    level__level = serializers.CharField(read_only=True)
    tuition = serializers.IntegerField(read_only=True)
    registration = serializers.IntegerField(read_only=True)
    payment_one = serializers.IntegerField(read_only=True)
    payment_two = serializers.IntegerField(read_only=True)
    payment_three = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetPrimaryMainSubjectSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    subject_name = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)


class GetPrimarySubjectSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    main_subject__id = serializers.CharField(read_only=True)
    main_subject__subject_name = serializers.CharField(read_only=True)
    classroom__id = serializers.CharField(read_only=True)
    classroom__main_classroom = serializers.CharField(read_only=True)
    classroom__school__campus__region = serializers.CharField(read_only=True)
    classroom__school__campus__name = serializers.CharField(read_only=True)
    classroom__academic_year = serializers.CharField(read_only=True)
    classroom__level__level = serializers.CharField(read_only=True)
    classroom__level__option = serializers.CharField(read_only=True)
    subject_code = serializers.CharField(read_only=True)
    subject_type = serializers.CharField(read_only=True)
    subject_coefficient = serializers.CharField(read_only=True)
    assigned = serializers.CharField(read_only=True)
    assigned_to__id = serializers.CharField(read_only=True)
    assigned_to__full_name = serializers.CharField(read_only=True)
    date_assigned = serializers.CharField(read_only=True)
    created_by__id = serializers.CharField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)

    main_course__course_name = serializers.CharField(read_only=True)
    specialty__main_specialty__specialty_name = serializers.CharField(read_only=True)
    specialty__academic_year = serializers.CharField(read_only=True)
    specialty__level__level = serializers.CharField(read_only=True)
                    

class GetPrimaryLevelSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    level = serializers.CharField(read_only=True)
    option = serializers.CharField(read_only=True)


class GetPrimaryResultSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    student__id = serializers.CharField(read_only=True)
    student__user__full_name = serializers.CharField(read_only=True)
    student__classroom__level__level = serializers.CharField(read_only=True)
    student__classroom__level__option = serializers.CharField(read_only=True)
    student__classroom__academic_year = serializers.CharField(read_only=True)
    subject__id = serializers.IntegerField(read_only=True)
    subject__main_subject__subject_name = serializers.CharField(read_only=True)
    subject__assigned_to__id = serializers.CharField(read_only=True)
    subject__classroom__id = serializers.IntegerField(read_only=True)
    subject__main_subject__subject_name = serializers.CharField(read_only=True)
    subject__assigned_to__full_name = serializers.CharField(read_only=True)
    seq_1 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    seq_2 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    seq_3 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    seq_4 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    seq_5 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    seq_6 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    average_term_1 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    average_term_2 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    average_term_3 = serializers.DecimalField(max_digits=5, decimal_places=1, read_only=True)
    passed_1 = serializers.BooleanField(read_only=True)
    passed_2 = serializers.BooleanField(read_only=True)
    passed_3 = serializers.BooleanField(read_only=True)
    published_seq_1 = serializers.BooleanField(read_only=True)
    published_seq_2 = serializers.BooleanField(read_only=True)
    published_seq_3 = serializers.BooleanField(read_only=True)
    published_seq_4 = serializers.BooleanField(read_only=True)
    published_seq_5 = serializers.BooleanField(read_only=True)
    published_seq_6 = serializers.BooleanField(read_only=True)
    published_term_1 = serializers.BooleanField(read_only=True)
    published_term_2 = serializers.BooleanField(read_only=True)
    published_term_3 = serializers.BooleanField(read_only=True)
    active = serializers.BooleanField(read_only=True)
    created_by__id = serializers.IntegerField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
    updated_by__full_name = serializers.CharField(read_only=True)
                    

class GetPrimaryPublishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    classroom__id = serializers.IntegerField(read_only=True)
    classroom__level__level = serializers.CharField(read_only=True)
    classroom__level__option = serializers.CharField(read_only=True)
    classroom__academic_year = serializers.CharField(read_only=True)
    classroom__domain = serializers.CharField(read_only=True)
    publish_item = serializers.CharField(read_only=True)
    publish_type = serializers.CharField(read_only=True)
    portal = serializers.CharField(read_only=True)
    publish = serializers.BooleanField(read_only=True)
    created_by__full_name = serializers.CharField(read_only=True)
                    