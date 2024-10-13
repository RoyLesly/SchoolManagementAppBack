from rest_framework import serializers


class GetSecondaryProfileSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)
    user__id = serializers.IntegerField(read_only=True)
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
    secondary_classroom__id = serializers.IntegerField(read_only=True)
    secondary_classroom__domain = serializers.CharField(read_only=True)
    secondary_classroom__level__id = serializers.IntegerField(read_only=True)
    secondary_classroom__level__level = serializers.CharField(read_only=True)
    secondary_classroom__level__option = serializers.CharField(read_only=True)
    secondary_classroom__academic_year = serializers.CharField(read_only=True)
    secondary_classroom__school__id = serializers.IntegerField(read_only=True)
    secondary_classroom__school__school_name = serializers.CharField(read_only=True)
    secondary_classroom__registration = serializers.CharField(read_only=True)
    secondary_classroom__tuition = serializers.CharField(read_only=True)
    secondary_classroom__payment_one = serializers.CharField(read_only=True)
    secondary_classroom__payment_two = serializers.CharField(read_only=True)
    secondary_classroom__payment_three = serializers.CharField(read_only=True)
    secondary_classroom__school__campus__id = serializers.IntegerField(read_only=True)
    secondary_classroom__school__campus__name = serializers.CharField(read_only=True)
    secondary_classroom__school__campus__region = serializers.CharField(read_only=True)
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
