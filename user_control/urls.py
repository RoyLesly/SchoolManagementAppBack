from django.urls import path, include
from rest_framework import routers
from user_control.models import UserActivities
from user_control.views import (
    UserCRUDView, LoginView, LogoutView, PasswordView, PasswordForgotView,
    MeView, UserActivitiesView, UserActivitiesView, GroupView, 
    PermissionView, AssignGroupsToUserView, UserProfilesView,
    AssignPermissionsGroupView, AppearanceView
)

app_name = "user_control"

router = routers.DefaultRouter(trailing_slash=False)
router.register("login", LoginView, "login")
router.register("logout", LogoutView, "logout")

router.register("crud-user", UserCRUDView, "create user")

router.register("me", MeView, "me")
router.register("create-update-reset-password", PasswordView, "create-update-reset-password")
router.register("forgot-password", PasswordForgotView, "forget_password")


router.register("assign-group-to-user", AssignGroupsToUserView, "assign-group-to-user")
router.register("assign-permissions-to-group", AssignPermissionsGroupView, "assign-permissions-to-group")

router.register("activities-log", UserActivitiesView, "activities log")
router.register("user-profiles", UserProfilesView, "user-profiles")
router.register("appearance", AppearanceView, "appearance")

router.register('groups',  GroupView, "groups" ),
router.register('permissions',  PermissionView, "permissions" ),


urlpatterns = [
    path('', include(router.urls)),
]
