from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "higher_control.time_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('timetableweek',  TimeTableWeekView, "timetableweek" ),
router.register('get-timetableweek',  GetTimeTableWeekView, ",get-timetableweek" ),
router.register('timetableday',  TimeTableDayView, "timetableday" ),
router.register('get-timetableday',  GetTimeTableDayView, ",get-timetableday" ),
router.register('timeslot',  TimeSlotView, "timeslot" ),
router.register('get-timeslot',  GetTimeSlotView, ",get-timeslot" ),

urlpatterns = [
    path('', include(router.urls)),
]
