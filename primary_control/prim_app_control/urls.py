from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "primary_control.prim_app_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('primaryclassroom',  PrimaryClassRoomView, "primaryclassroom" ),
router.register('primarymainsubject',  PrimaryMainSubjectView, "primarymainsubject" ),
router.register('primarysubject',  PrimarySubjectView, "primarysubject" ),
router.register('primarylevel',  PrimaryLevelView, "primarylevel" ),
# router.register('primaryresult',  PrimaryResultView, "primaryresult" ),
# router.register('primarypublish',  PrimaryPublishView, "primarypublish" ),

# router.register('get-sec-classroom',  GetPrimaryClassRoomView, "get-sec-classroom" ),
# router.register('get-sec-mainsubject',  GetPrimaryMainSubjectView, "get-sec-mainsubject" ),
# router.register('get-sec-subject',  GetPrimarySubjectView, "get-sec-subject" ),
# router.register('get-sec-level',  GetPrimaryLevelView, "get-sec-level" ),
# router.register('get-sec-result',  GetPrimaryResultView, "get-sec-result" ),
# router.register('get-sec-publish',  GetPrimaryPublishView, "get-sec-publish" ),
# router.register('get-result-transcript',  GetPrimaryResultTranscriptView, "get-sec-result-transcript" ),
# router.register('get-sec-result-classroom',  GetPrimaryResultClassroomView, "get-sec-result-classroom" ),


# router.register('semester',  GetSemesterView, "semester" ),
# router.register('academic-year',  GetPrimaryAcademicYearView, "academic-year" ),
# router.register('my-classrooms',  GetPrimaryMyClassRoomsView, "my-specialties" ),



urlpatterns = [
    path('', include(router.urls)),
]
