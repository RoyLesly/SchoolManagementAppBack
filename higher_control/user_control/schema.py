import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from .models import *
from .schemaFilter import *


# UserProfile Type
class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        filter_fields = ['id', 'session', 'user', 'active']
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "user",
            "specialty",
            "active",
            "program",
            "code",
            "session",
            "created_at",
            "updated_at",
        )


# CustomUser Type
class CustomUserType(DjangoObjectType):
    profiles = graphene.List(UserProfileType)  # Return a list of UserProfiles

    def resolve_profiles(self, info):
        return self.profiles.all()
    

    class Meta:
        model = CustomUser
        filter_fields = ['id', 'matricle', 'email', 'sex', 'full_name']
        interfaces = (graphene.relay.Node,)  # This line enables Relay pagination
        fields = (
            "id",
            "photo",
            "username",
            "matricle",
            "role",
            "email",
            "telephone",
            "first_name",
            "last_name",
            "full_name",
            "dob",
            'pob',
            "address",
            "sex",
            "title",
            'parent',
            'parent_telephone',
            'about',
            "created_at",
            "updated_at",
            "is_staff",
            "is_superuser",
            "is_active",
            "last_login",
            "school",  # Include the ManyToManyField for school
            "dept",    # Include the ManyToManyField for department
            "page",    # Include the ManyToManyField for page
        )


# Department Type
class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        filter_fields = ['id', 'name']
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "name",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )


# Program Type
class ProgramType(DjangoObjectType):
    class Meta:
        model = Program
        filter_fields = ['id', 'name']
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "name",
            "description",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )


# Appearance Type
class AppearanceType(DjangoObjectType):
    class Meta:
        model = Appearance
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "user",
            "dark_mode",
            "lang",
            "created_at",
            "updated_at",
        )


# Page Type
class PageType(DjangoObjectType):
    class Meta:
        model = Page
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "name",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )


# PreInscription Type
class PreInscriptionType(DjangoObjectType):
    class Meta:
        model = PreInscription
        filter_fields = ['id', 'registration_number', 'full_name', 'sex', 'telephone']
        interfaces = (graphene.relay.Node,) 
        fields = (
            "id",
            "registration_number",
            "first_name",
            "last_name",
            "full_name",
            "sex",
            "email",
            "telephone",
            "address",
            "pob",
            "dob",
            "status",
            "emergency_name",
            "emergency_town",
            "emergency_telephone",
            "program",
            "level",
            "session",
            "academic_year",
            "specialty_one",
            "specialty_two",
            "specialty_three",
            "campus",
            "admission_status",
            "action",
            "created_at",
            "updated_at",
        )


# Query Class
class Query(graphene.ObjectType):
    # Existing fields
    all_custom_users = DjangoFilterConnectionField(CustomUserType, filterset_class=CustomUserFilter)
    all_deprtments = DjangoFilterConnectionField(DepartmentType, filterset_class=DepartmentFilter)
    all_programs = DjangoFilterConnectionField(ProgramType, filterset_class=ProgramFilter)
    all_user_profiles = DjangoFilterConnectionField(UserProfileType, filterset_class=UserProfileFilter)
    # all_appearances = DjangoFilterConnectionField(AppearanceType, filterset_class=AppearanceFilter)
    # all_pages = graphene.List(PageType)
    all_preinscriptions = DjangoFilterConnectionField(PreInscriptionType, filterset_class=PreInscriptionFilter)

    # Count fields
    custom_users_count = graphene.Int()
    departments_count = graphene.Int()
    programs_count = graphene.Int()
    user_profiles_count = graphene.Int()
    # appearances_count = graphene.Int()
    # pages_count = graphene.Int()
    preinscriptions_count = graphene.Int()

    # Resolvers for each query
    def resolve_all_custom_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_all_departments(self, info, **kwargs):
        return Department.objects.all()

    def resolve_all_programs(self, info, **kwargs):
        return Program.objects.all()

    def resolve_all_user_profiles(self, info, **kwargs):
        return UserProfile.objects.all()

    # def resolve_all_appearances(self, info, **kwargs):
    #     return Appearance.objects.all()

    # def resolve_all_pages(self, info, **kwargs):
    #     return Page.objects.all()

    def resolve_all_preinscriptions(self, info, **kwargs):
        return PreInscription.objects.all()


    # Resolvers for count fields
    def resolve_custom_users_count(self, info, **kwargs):
        return CustomUser.objects.count()

    def resolve_departments_count(self, info, **kwargs):
        return Department.objects.count()

    def resolve_programs_count(self, info, **kwargs):
        return Program.objects.count()

    def resolve_user_profiles_count(self, info, **kwargs):
        return UserProfile.objects.count()

    # def resolve_appearances_count(self, info, **kwargs):
    #     return Appearance.objects.count()

    # def resolve_pages_count(self, info, **kwargs):
    #     return Page.objects.count()

    def resolve_preinscriptions_count(self, info, **kwargs):
        return PreInscription.objects.count()
    
        # Count fields for filtered results
    filtered_custom_users_count =  graphene.Int(
        id=graphene.Int(),
        matricle=graphene.String(),
        full_name=graphene.String(),
        school_id=graphene.Int(),
        campus=graphene.String(),
        role=graphene.String(),
        is_active=graphene.Boolean()
    )
    filtered_user_profiles_count = graphene.Int(
        id=graphene.Int(),
        matricle=graphene.String(),
        full_name=graphene.String(),
        sex=graphene.String(),
        school_id=graphene.Int(),
        campus=graphene.String(),
        academic_year=graphene.String(),
        domain_name=graphene.String(),
        specialty_name=graphene.String(),
        level=graphene.Int(),
        role=graphene.String(),
        is_active=graphene.Boolean()
    )
    filtered_preinscriptions_count = graphene.Int()

    # Resolver for filtered custom users count
    def resolve_filtered_custom_users_count(self, info, **kwargs):
        applied_filters = CustomUserFilter(data=kwargs, queryset=CustomUser.objects.all())
        return applied_filters.qs.count()

    # Resolver for filtered user profiles count
    def resolve_filtered_user_profiles_count(self, info, **kwargs):
        applied_filters = UserProfileFilter(data=kwargs, queryset=UserProfile.objects.all())
        return applied_filters.qs.count()

    # Resolver for filtered preinscriptions count
    def resolve_filtered_preinscriptions_count(self, info, **kwargs):
        applied_filters = PreInscriptionFilter(data=kwargs, queryset=PreInscription.objects.all())
        return applied_filters.qs.count()


# Create the schema
schema = graphene.Schema(query=Query)

