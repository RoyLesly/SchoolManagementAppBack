from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *

app_name = "secondary_control.sec_user_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register("secondaryprofile", SecondaryProfileView, "secondaryprofile")
router.register("get-secondaryprofile", GetSecondaryProfileView, "get-secondaryprofile")

urlpatterns = [
    path('', include(router.urls)),
    path('check-password', CheckPasswordView.as_view(), name="check-password"),
]
