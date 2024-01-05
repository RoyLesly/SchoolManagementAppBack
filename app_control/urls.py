from django.urls import path, include
from rest_framework import routers
from .views import *
from .paginate import *

app_name = "app_control"

router = routers.DefaultRouter(trailing_slash=False)
router.register('domain',  DomainView, "domain" ),
router.register('mainspecialty',  MainSpecialtyView, ",mainspecialty" ),
router.register('specialty',  SpecialtyView, "specialty" ),
router.register('maincourse',  MainCourseView, "maincourse" ),
router.register('course',  CourseView, "course" ),
router.register('result',  ResultView, "result" ),
router.register('level',  LevelView, "level" ),

router.register('result-academic-year',  ResultAcademicYearView, "result" ),

# PAGINATION
router.register('page-domain',  PageDomainView, "page-domain" ),
router.register('page-mainspecialty',  PageMainSpecialtyView, "page-mainspecialty" ),
router.register('page-specialty',  PageSpecialtyView, "page-specialty" ),
router.register('page-maincourse',  PageMainCourseView, "page-maincourse" ),
router.register('page-course',  PageCourseView, "page-course" ),
router.register('page-result',  PageResultView, "page-result" ),
router.register('page-level',  PageLevelView, "page-level" ),

# KPI
router.register("kpi-app", KpiAppControlView, "kpi-app")

# DROPDOWNS
router.register("dropdowns", DropdownsView, "dropdowns")


urlpatterns = [
    path('', include(router.urls)),
]
