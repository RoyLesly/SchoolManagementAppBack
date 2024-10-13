from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "app_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('secondaryclassroom',  SecondaryClassRoomView, "secondaryclassroom" ),
router.register('secondarymainsubject',  SecondaryMainSubjectView, "secondarymainsubject" ),
router.register('secondarysubject',  SecondarySubjectView, "secondarysubject" ),
router.register('secondarylevel',  SecondaryLevelView, "secondarylevel" ),
router.register('secondaryresult',  SecondaryResultView, "secondaryresult" ),
router.register('secondarypublish',  SecondaryPublishView, "secondarypublish" ),

router.register('get-sec-classroom',  GetSecondaryClassRoomView, "get-sec-classroom" ),
router.register('get-sec-mainsubject',  GetSecondaryMainSubjectView, "get-sec-mainsubject" ),
router.register('get-sec-subject',  GetSecondarySubjectView, "get-sec-subject" ),
router.register('get-sec-level',  GetSecondaryLevelView, "get-sec-level" ),
router.register('get-sec-result',  GetSecondaryResultView, "get-sec-result" ),
router.register('get-sec-publish',  GetSecondaryPublishView, "get-sec-publish" ),
router.register('get-result-transcript',  GetSecondaryResultTranscriptView, "get-sec-result-transcript" ),
router.register('get-sec-result-classroom',  GetSecondaryResultClassroomView, "get-sec-result-classroom" ),


# router.register('semester',  GetSemesterView, "semester" ),
router.register('academic-year',  GetSecondaryAcademicYearView, "academic-year" ),
router.register('my-classrooms',  GetSecondaryMyClassRoomsView, "my-specialties" ),



urlpatterns = [
    path('', include(router.urls)),
]
