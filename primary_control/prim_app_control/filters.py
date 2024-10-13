import django_filters
from .models import *


class PrimaryClassRoomFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    domain = django_filters.CharFilter(lookup_expr="icontains")
    level__id = django_filters.CharFilter(lookup_expr="exact")
    level__level = django_filters.CharFilter(lookup_expr="icontains")
    level__option = django_filters.CharFilter(lookup_expr="icontains")
    academic_year = django_filters.CharFilter(lookup_expr="icontains")
    tuition = django_filters.CharFilter(lookup_expr="icontains")
    registration = django_filters.CharFilter(lookup_expr="icontains")
    school__id = django_filters.CharFilter(lookup_expr="exact")
    school__campus__id = django_filters.CharFilter(lookup_expr="exact")
    school__campus__region = django_filters.CharFilter(lookup_expr="icontain")
    school__campus__name = django_filters.CharFilter(lookup_expr="icontain")
    class meta:
        model = PrimaryClassRoom
        fields = {
            'id': [ "exact" ],
        }


class PrimaryMainSubjectFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    subject_name = django_filters.CharFilter(lookup_expr="icontains")
    class meta:
        model = PrimaryMainSubject
        fields = {
            'id': [ "exact" ],
        }
    

class PrimarySubjectFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    main_subject__subject_name = django_filters.CharFilter(lookup_expr="icontains")
    subject_code = django_filters.CharFilter(lookup_expr="icontains")
    subject_type = django_filters.CharFilter(lookup_expr="icontains")
    subject_coefficient = django_filters.CharFilter(lookup_expr="icontains")
    assigned = django_filters.CharFilter(lookup_expr="icontains")
    assigned_to__full_name = django_filters.CharFilter(lookup_expr="icontains")
    classroom__domain = django_filters.CharFilter(lookup_expr="icontains")
    classroom__academic_year = django_filters.CharFilter(lookup_expr="icontains")
    classroom__level__id = django_filters.CharFilter(lookup_expr="icontains")
    classroom__level__level = django_filters.CharFilter(lookup_expr="icontains")
    classroom__level__option = django_filters.CharFilter(lookup_expr="icontains")
    classroom__tuition = django_filters.CharFilter(lookup_expr="icontains")
    classroom__school__campus__id = django_filters.CharFilter(lookup_expr="icontains")
    assigned_to__id = django_filters.CharFilter(lookup_expr="exact")
    class meta:
        model = PrimarySubject
        fields = {
        }


class PrimaryLevelFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr="exact")
    level = django_filters.CharFilter(lookup_expr="icontains")
    option = django_filters.CharFilter(lookup_expr="icontains")

    class meta:
        model = PrimaryLevel
        fields = {
        }


# class PrimaryResultFilter(django_filters.FilterSet):
#     id = django_filters.CharFilter(lookup_expr="exact")
#     student__id = django_filters.CharFilter(lookup_expr="exact")
#     student__user__full_name = django_filters.CharFilter(lookup_expr="icontains")
#     student__user__matricle = django_filters.CharFilter(lookup_expr="iexact")
#     student__user__telephone = django_filters.CharFilter(lookup_expr="icontains")
#     subject__id = django_filters.CharFilter(lookup_expr="exact")
#     subject__classroom__id = django_filters.CharFilter(lookup_expr="exact")
#     subject__classroom__main_classroom = django_filters.CharFilter(lookup_expr="icontains")
#     subject__classroom__academic_year = django_filters.CharFilter(lookup_expr="icontains")
#     subject__classroom__domain = django_filters.CharFilter(lookup_expr="icontains")

#     publish_exam_1 = django_filters.BooleanFilter()
#     publish_exam_2 = django_filters.BooleanFilter()
#     publish_exam_3 = django_filters.BooleanFilter()
#     publish_seq_1 = django_filters.BooleanFilter()
#     publish_seq_2 = django_filters.BooleanFilter()
#     publish_seq_3 = django_filters.BooleanFilter()
#     publish_seq_4 = django_filters.BooleanFilter()
#     publish_seq_5 = django_filters.BooleanFilter()
#     publish_seq_6 = django_filters.BooleanFilter()
#     active = django_filters.BooleanFilter()

#     class meta:
#         model = PrimaryResult
#         fields = {
#             'created_at': [ 'exact', 'gte', 'lte', 'gt', 'lt', 'year', 'year__gt', 'year__lt', 'month', 'month__gt', 'month__lt', 'day', 'day__gt', 'day__lt' ],
#         }


# class PrimaryPublishFilter(django_filters.FilterSet):
#     id = django_filters.CharFilter(lookup_expr="exact")
#     classroom__id = django_filters.CharFilter(lookup_expr="exact")
#     classroom__main_classroom = django_filters.CharFilter(lookup_expr="icontains")
#     classroom__academic_year = django_filters.CharFilter(lookup_expr="icontains")
#     term = django_filters.CharFilter(lookup_expr="iexact")
#     sequence = django_filters.CharFilter(lookup_expr="iexact")

#     class meta:
#         model = PrimaryPublish
#         fields = {
#             'id': [ "exact" ],
#         }
