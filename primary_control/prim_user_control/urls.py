from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *

app_name = "primary_control.prim_user_control"

router = routers.DefaultRouter(trailing_slash=False)

# router.register("group", GroupView, "group")
# router.register("permission", PermissionView, "permission")
# router.register("useractivity", UserActivityView, "useractivity")
router.register("userprofile", PrimaryProfileView, "userprofile")
# router.register("department", DepartmentView, "department")


# router.register("get-group", GetGroupView, "get-group")
# router.register("get-permission", GetPermissionView, "get-permission")
# router.register("get-useractivity", GetUserActivityView, "get-useractivity")
router.register("get-userprofile", GetPrimaryProfileView, "get-userprofile")

urlpatterns = [
    path('', include(router.urls)),
]
