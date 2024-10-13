from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "fees_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('secschoolfees',  SecSchoolFeesView, "secschoolfees" ),
router.register('get-secschoolfees',  GetSecSchoolFeesView, "get-secschoolfees" ),
router.register('sectransactions',  SecTransactionsView, "sectransactions" ),
router.register('get-sectransactions',  GetSecTransactionsView, ",get-sectransactions" ),
router.register('activationkey',  ActivationKeyView, "activationkey" ),
router.register('get-activationkey',  ActivationKeyView, ",get-activationkey" ),

urlpatterns = [
    path('', include(router.urls)),
]
