from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "noti_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('notification',  NotificationView, "notification" ),
router.register('complain',  ComplainView, ",complain" ),
router.register("useractivity", UserActivityView, "useractivity")


router.register('get-notification',  GetNotificationView, "get-notification" ),
router.register('get-complain',  GetComplainView, "get-complain" ),
router.register("get-useractivity", GetUserActivityView, "get-useractivity")



urlpatterns = [
    path('', include(router.urls)),
]
