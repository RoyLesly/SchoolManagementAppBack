from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *
from .viewsOpen import *

app_name = "higher_control.user_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register("group", GroupView, "group")
router.register("permission", PermissionView, "permission")
router.register("program", ProgramView, "program")
router.register("department", DepartmentView, "department")
router.register("userprofile", UserProfileView, "userprofile")
router.register("customuser", CustomUserView, "customuser")
router.register("preinscription", PreInscriptionView, "preinscription")
router.register("appearance", AppearanceView, "appearance")

# router.register("get-group", GetGroupView, "get-group")
# router.register("get-permission", GetPermissionView, "get-permission")
router.register("get-department", GetDepartmentView, "get-department")
router.register("get-userprofile", GetUserProfileView, "get-userprofile")
router.register("get-customuser", GetCustomUserView, "get-customuser")
router.register("get-preinscription", GetPreInscriptionView, "get-preinscription")
router.register("get-appearance", GetAppearanceView, "get-appearance")
router.register("get-program", GetProgramView, "get-program")

router.register("open-get-customuser", CheckCustomUserView, "open-get-customuser")
router.register("open-get-preinscription", CheckPreInscriptionView, "open-get-preinscription")


# router.register("check-password", CheckPasswordView, "check-password")
router.register("create-password", CreatePasswordView, "create-password")
router.register("update-password", UpdatePasswordView, "update-password")
# router.register("reset-password", ResetPasswordView, "reset-password")

urlpatterns = [
    path('', include(router.urls)),
    path('check-password', CheckPasswordView.as_view(), name="check-password"),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace="password_reset")),
    path('password_reset/confirm/', include('django_rest_passwordreset.urls', namespace="password_reset_cconfirm")),
    path("user_verify_email/<int:pk>/", user_verify_email, name="verify_email"),
]
