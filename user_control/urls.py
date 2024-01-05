from django.urls import path, include
from rest_framework import routers
from user_control.models import UserActivities
from .views import *
from .paginate import *

app_name = "user_control"

router = routers.DefaultRouter(trailing_slash=False)
router.register("login", LoginView, "login")
router.register("check-user", CheckUserView, "login")
router.register("logout", LogoutView, "logout")

router.register("crud-user", UserCRUDView, "create user")

router.register("me", MeView, "me")
router.register("create-update-reset-password", PasswordView, "create-update-reset-password")

router.register("assign-group-to-user", AssignGroupsToUserView, "assign-group-to-user")
router.register("assign-permissions-to-group", AssignPermissionsGroupView, "assign-permissions-to-group")

router.register("activities-log", UserActivitiesView, "activities log")
router.register("user-profiles", UserProfilesView, "user-profiles")
router.register("user-profiles-students/", UserProfilesStudentsView, "user-profiles-students")
router.register("user-profiles-lecturers/", UserProfilesLecturersView, "user-profiles-lecturers")
router.register("appearance", AppearanceView, "appearance")

router.register('groups',  GroupView, "groups" ),
router.register('permissions',  PermissionView, "permissions" ),

# PAGINATION
router.register('page-groups',  PageGroupView, "page-groups" ),
router.register('page-permissions',  PagePermissionView, "page-permissions" ),
router.register("page-crud-user", PageUserCRUDView, "page-create user")
router.register("page-activities-log", PageUserActivitiesView, "page-activities-log")
router.register("page-user-profiles-students/", PageUserProfilesStudentsView, "page-user-profiles-students")
router.register("page-user-profiles-lecturers/", PageUserProfilesLecturersView, "page-user-profiles-lecturers")
router.register("page-user-profiles", PageUserProfilesView, "page-user-profiles")

# KPI
router.register("kpi-custom-user-counts", KpiCustomUserCountsView, "kpi-custom-user")
router.register("kpi-user-profile-specialty-one-counts", KpiUserProfileSpecialtyCountOneView, "kpi-user-profile-specialty-one-counts")
router.register("kpi-user-profile-specialty-two-counts", KpiUserProfileSpecialtyCountTwoView, "kpi-user-profile-specialty-one-counts")
router.register("kpi-yearly-model-count-list", KpiYearlyModelCountListView, "kpi-yearly-model-count-list")


urlpatterns = [
    path('', include(router.urls)),
    path("verify_email/<int:pk>/", verify_email, name="verify_email"),
]
