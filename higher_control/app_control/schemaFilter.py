import django_filters
from .models import *


class SchoolIdentificationFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(field_name="code", lookup_expr="icontains")
    version = django_filters.CharFilter(field_name="version", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
    ))

    class Meta:
        model = SchoolIdentification
        fields = ('code', 'version',)


class SchoolInfoHigherFilter(django_filters.FilterSet):
    campus = django_filters.CharFilter(field_name="campus", lookup_expr="icontains")
    school_identification_id = django_filters.NumberFilter(field_name="school_identification__id", lookup_expr="exact")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id',), 
        ('campus', 'campus',), 
    ))

    class Meta:
        model = SchoolInfoHigher
        fields = [ 'id', 'campus', 'school_identification_id',]


class DomainFilter(django_filters.FilterSet):
    domain_name = django_filters.CharFilter(field_name="domain_name", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id',), 
        ('domain_name', 'domain_name',), 
    ))

    class Meta:
        model = Domain
        fields = ['domain_name']


class FieldFilter(django_filters.FilterSet):
    domain_id = django_filters.NumberFilter(field_name="domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="domain__domain_name", lookup_expr="icontains")
    
    field_name = django_filters.CharFilter(field_name="field_name", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('domain_id', 'domain_id'), 
        ('domain_name', 'domain_name'),
        ('field_name', 'field_name'),
    ))

    class Meta:
        model = Field
        fields = [ 'domain_id', 'domain_name', 'field_name' ]


class MainSpecialtyFilter(django_filters.FilterSet):
    domain_id = django_filters.NumberFilter(field_name="field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="field__domain__domain_name", lookup_expr="icontains")
    field_id = django_filters.NumberFilter(field_name="field__field_id", lookup_expr="exact")
    field_name = django_filters.CharFilter(field_name="field__field_name", lookup_expr="icontains")
    
    specialty_name = django_filters.CharFilter(field_name="specialty_name", lookup_expr="icontains")
    specialty_name_short = django_filters.CharFilter(field_name="specialty_name_short", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('field__domain__domain_name', 'domain_name'), 
        ('specialty_name', 'specialty_name'),
    ))

    class Meta:
        model = MainSpecialty
        fields = [ 'domain_id', 'domain_name', 'field_id', 'field_name', 'specialty_name', 'specialty_name_short' ]


class SpecialtyFilter(django_filters.FilterSet):
    domain_id = django_filters.NumberFilter(field_name="main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="main_specialty__field__domain__domain_name", lookup_expr="icontains")
    field_id = django_filters.NumberFilter(field_name="main_specialty__field__field_id", lookup_expr="exact")
    field_name = django_filters.CharFilter(field_name="main_specialty__field__field_name", lookup_expr="icontains")
    specialty_name = django_filters.CharFilter(field_name="main_specialty__specialty_name", lookup_expr="icontains")
    specialty_name_short = django_filters.CharFilter(field_name="main_specialty__specialty_name_short", lookup_expr="icontains")
    
    school_id = django_filters.NumberFilter(field_name="school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="school__campus", lookup_expr="icontains")
    region = django_filters.CharFilter(field_name="school__region", lookup_expr="icontains")
    town = django_filters.CharFilter(field_name="school__town", lookup_expr="icontains")
    level_id = django_filters.NumberFilter(field_name="level__id", lookup_expr="exact")
    level = django_filters.NumberFilter(field_name="level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="academic_year", lookup_expr="icontains")
    tuition = django_filters.NumberFilter(field_name="tuition", lookup_expr="exact")
    registration = django_filters.NumberFilter(field_name="registration", lookup_expr="exact")
    payment_one = django_filters.NumberFilter(field_name="payment_one", lookup_expr="exact")
    payment_two = django_filters.NumberFilter(field_name="payment_two", lookup_expr="exact")
    payment_three = django_filters.NumberFilter(field_name="payment_three", lookup_expr="exact")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('main_specialty__field__domain__domain_name', 'domain_name'), 
        ('main_specialty__specialty_name', 'specialty_name'),
        ('academic_year', 'academic_year'), 
        ('level__level', 'level'), 
        ('tuition', 'tuition'), 
    ))

    class Meta:
        model = Specialty
        fields = [ 'domain_id', 'domain_name', 'field_id', 'field_name', 'specialty_name', 'specialty_name_short', 'tuition', 'academic_year', 'level' ]


class MainCourseFilter(django_filters.FilterSet):
    course_name = django_filters.CharFilter(field_name="course_name", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id', ), 
        ('course_name', 'course_name', ), 
    ))

    class Meta:
        model = MainCourse
        fields = [ 'course_name' ]



class CourseFilter(django_filters.FilterSet):
    domain_id = django_filters.NumberFilter(field_name="specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    field_id = django_filters.NumberFilter(field_name="specialty__main_specialty__field__field_id", lookup_expr="exact")
    field_name = django_filters.CharFilter(field_name="specialty__main_specialty__field__field_name", lookup_expr="icontains")
    specialty_name = django_filters.CharFilter(field_name="specialty__main_specialty__specialty_name", lookup_expr="icontains")
    specialty_name_short = django_filters.CharFilter(field_name="specialty__main_specialty__specialty_name_short", lookup_expr="icontains")
    level_id = django_filters.NumberFilter(field_name="specialty__level__id", lookup_expr="exact")
    level = django_filters.NumberFilter(field_name="specialty__level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="specialty__academic_year", lookup_expr="icontains")
    school_id = django_filters.NumberFilter(field_name="specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="specialty__school__campus", lookup_expr="icontains")
    region = django_filters.CharFilter(field_name="specialty__school__region", lookup_expr="icontains")
    town = django_filters.CharFilter(field_name="specialty__school__town", lookup_expr="icontains")
    
    course_name = django_filters.CharFilter(field_name="main_course__course_name", lookup_expr="icontains")
    course_code = django_filters.CharFilter(field_name="course_code", lookup_expr="icontains")
    course_type = django_filters.CharFilter(field_name="course_type", lookup_expr="icontains")
    course_credit = django_filters.NumberFilter(field_name="course_credit", lookup_expr="exact")
    semester = django_filters.CharFilter(field_name="semester", lookup_expr="icontains")
    completed = django_filters.BooleanFilter(field_name="completed")
    paid = django_filters.BooleanFilter(field_name="paid")
    hours = django_filters.NumberFilter(field_name="hours", lookup_expr="exact")
    hours_left = django_filters.NumberFilter(field_name="hours_left", lookup_expr="exact")
    assigned_to_id = django_filters.NumberFilter(field_name="assigned_to__id", lookup_expr="exact")
    assigned_to_full_name = django_filters.CharFilter(field_name="assigned_to__full_name", lookup_expr="icontains")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('main_course__course_name', 'course_name'), 
        ('specialty__school__campus', 'campus'), 
        ('specialty__main_specialty__field__domain__domain_name', 'domain_name'), 
        ('specialty__main_specialty__specialty_name', 'specialty_name'), 
        ('academic_year', 'academic_year'), 
        ('level__level', 'level'), 
        ('tuition', 'tuition'), 
    ))

    class Meta:
        model = Course
        fields = ['domain_id', 'domain_name', 'field_id', 'field_name', 'specialty_name', 'specialty_name_short', 'level_id', 'level',
                'academic_year', 'school_id', 'campus', 'region', 'town', 'course_name', 'course_code', 'course_type', 'course_credit', 'semester',
                'completed', 'paid', 'hours', 'hours_left', 'assigned_to_id', 'assigned_to_full_name' 
        ]



class ResultFilter(django_filters.FilterSet):
    domain_id = django_filters.NumberFilter(field_name="course__specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="course__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    field_id = django_filters.NumberFilter(field_name="course__specialty__main_specialty__field__field_id", lookup_expr="exact")
    field_name = django_filters.CharFilter(field_name="course__specialty__main_specialty__field__field_name", lookup_expr="icontains")
    specialty_name = django_filters.CharFilter(field_name="course__specialty__main_specialty__specialty_name", lookup_expr="icontains")
    specialty_name_short = django_filters.CharFilter(field_name="course__specialty__main_specialty__specialty_name_short", lookup_expr="icontains")
    level_id = django_filters.NumberFilter(field_name="course__specialty__level__id", lookup_expr="exact")
    level = django_filters.NumberFilter(field_name="course__specialty__level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="course__specialty__academic_year", lookup_expr="icontains")
    school_id = django_filters.NumberFilter(field_name="course__specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="course__specialty__school__campus", lookup_expr="icontains")

    course_id = django_filters.NumberFilter(field_name="course__id", lookup_expr="exact")
    course_name = django_filters.CharFilter(field_name="course__main_course__course_name", lookup_expr="icontains")
    course_code = django_filters.CharFilter(field_name="course__course_code", lookup_expr="icontains")
    course_type = django_filters.CharFilter(field_name="course__course_type", lookup_expr="icontains")
    course_credit = django_filters.NumberFilter(field_name="course__course_credit", lookup_expr="exact")
    semester = django_filters.CharFilter(field_name="course__semester", lookup_expr="icontains")
    assigned_to_id = django_filters.NumberFilter(field_name="course__assigned_to__id", lookup_expr="exact")
    assigned_to_full_name = django_filters.CharFilter(field_name="course__assigned_to__full_name", lookup_expr="icontains")
    student_id = django_filters.NumberFilter(field_name="student__id", lookup_expr="exact")
    user_id = django_filters.NumberFilter(field_name="student__user__id", lookup_expr="exact")
    full_name = django_filters.CharFilter(field_name="student__user__full_name", lookup_expr="icontains")
    matricle = django_filters.CharFilter(field_name="student__user__matricle", lookup_expr="icontains")
    
    average = django_filters.NumberFilter(field_name="average", lookup_expr='exact')
    validated = django_filters.BooleanFilter(field_name="validated")
    closed = django_filters.BooleanFilter(field_name="closed")
    active = django_filters.BooleanFilter(field_name="active")
    publish_ca = django_filters.BooleanFilter(field_name="publish_ca")
    publish_exam = django_filters.BooleanFilter(field_name="publish_exam")
    publish_resit = django_filters.BooleanFilter(field_name="publish_resit")

    created_at = django_filters.DateTimeFromToRangeFilter(field_name="created_at", lookup_expr="icontains")
    updated_at = django_filters.DateTimeFromToRangeFilter(field_name="updated_at", lookup_expr="icontains")
    created_by = django_filters.CharFilter(field_name="created_by__full_name", lookup_expr="icontains")
    updated_by = django_filters.CharFilter(field_name="updaated_by__full_name", lookup_expr="icontains")


    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('student__user__full_name', 'full_name'), 
        ('student__user__matricle', 'matricle'), 
        ('course__main_course__course_name', 'course_name'), 
        ('course__specialty__school__campus', 'campus'), 
        ('course__specialty__main_specialty__field__domain__domain_name', 'domain_name'), 
        ('course__specialty__main_specialty__specialty_name', 'specialty_name'), 
        ('course__academic_year', 'academic_year'), 
        ('course__level__level', 'level'), 
    ))

    class Meta:
        model = Result
        fields = [ 'domain_id', 'domain_name', 'field_id', 'field_name', 'specialty_name', 'specialty_name_short', 'level_id', 'level', 'academic_year', 'school_id', 'campus', 
                'course_id', 'course_name', 'course_code', 'course_type', 'course_credit', 'semester', 'assigned_to_id', 'assigned_to_full_name',
                'student_id', 'user_id', 'full_name', 'matricle', 
                'average', 'validated', 'closed', 'active', 'publish_ca', 'publish_exam', 'publish_resit',
                'created_at', 'created_by__full_name', 'updated_at', 'updated_by__full_name'
        ]



class PublishFilter(django_filters.FilterSet):
    domain_id = django_filters.NumberFilter(field_name="course__specialty__main_specialty__field__domain__id", lookup_expr="exact")
    domain_name = django_filters.CharFilter(field_name="course__specialty__main_specialty__field__domain__domain_name", lookup_expr="icontains")
    specialty_id = django_filters.NumberFilter(field_name="course__specialty__id", lookup_expr="exact")
    specialty_name = django_filters.CharFilter(field_name="course__specialty__main_specialty__specialty_name", lookup_expr="icontains")
    specialty_name_short = django_filters.CharFilter(field_name="course__specialty__main_specialty__specialty_name_short", lookup_expr="icontains")
    level_id = django_filters.NumberFilter(field_name="course__specialty__level__id", lookup_expr="exact")
    level = django_filters.NumberFilter(field_name="course__specialty__level__level", lookup_expr="exact")
    academic_year = django_filters.CharFilter(field_name="course__specialty__academic_year", lookup_expr="icontains")
    school_id = django_filters.NumberFilter(field_name="course__specialty__school__id", lookup_expr="exact")
    campus = django_filters.CharFilter(field_name="course__specialty__school__campus", lookup_expr="icontains")
    
    semester = django_filters.CharFilter(field_name="semester", lookup_expr="icontains")
    ca = django_filters.BooleanFilter(field_name="ca")
    exam = django_filters.BooleanFilter(field_name="exam")
    resit = django_filters.BooleanFilter(field_name="resit")
    portal_ca = django_filters.BooleanFilter(field_name="portal_ca")
    portal_exam = django_filters.BooleanFilter(field_name="portal_exam")
    portal_resit = django_filters.BooleanFilter(field_name="portal_resit")

    ordering = django_filters.OrderingFilter(fields=(
        ('id', 'id'), 
        ('specialty__school__campus', 'campus'), 
        ('specialty__main_specialty__field__domain__domain_name', 'domain_name'), 
        ('specialty__main_specialty__specialty_name', 'specialty_name'), 
        ('specialty__academic_year', 'academic_year'), 
        ('specialty__level__level', 'level',), 
        ('semester', 'semester',), 
    ))

    class Meta:
        model = Publish
        fields = [ 'domain_id', 'domain_name', 'specialty_name', 'specialty_name_short', 'level', 'academic_year', 'school_id', 'campus', 
                'semester', 'ca', 'exam', 'resit', 'portal_ca', 'portal_exam', 'portal_resit'
        ]


class LevelFilter(django_filters.FilterSet):
    level = django_filters.NumberFilter(field_name="level", lookup_expr="exact")

    ordering = django_filters.OrderingFilter(fields=(
        ('level', 'level'), 
    ))

    class Meta:
        model = Level
        fields = [ 'level',]
