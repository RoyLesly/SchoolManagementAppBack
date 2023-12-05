from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "app_control"

router = routers.DefaultRouter(trailing_slash=False)
router.register('domain',  DomainView, "domain" ),
router.register('mainspecialty',  MainSpecialtyView, ",mainspecialty" ),
router.register('maincourse',  MainCourseView, "maincourse" ),
router.register('specialty',  SpecialtyView, "specialty" ),
router.register('course',  CourseView, "course" ),
router.register('result',  ResultView, "result" ),
router.register('level',  LevelView, "level" ),


urlpatterns = [
    path('', include(router.urls)),
]
