from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "higher_control.fees_control"

router = routers.DefaultRouter(trailing_slash=False)


router.register('activationkey',  ActivationKeyView, "activationkey" ),
router.register('account',  AccountView, "account" ),
router.register('schoolfees',  SchoolFeesView, "schoolfees" ),
router.register('transactions',  TransactionsView, "transactions" ),
router.register('transcript-application',  TranscriptApplicationView, "transcript-application" ),

router.register('get-activationkey',  ActivationKeyView, "get-activationkey" ),
router.register('get-account',  GetAccountView, ",get-account" ),
router.register('get-transactions',  GetTransactionsView, "get-transactions" ),
router.register('get-schoolfees',  GetSchoolFeesView, "get-schoolfees" ),
router.register('get-transcript-application',  GetTranscriptApplicationView, ",get-transcript-application" ),
router.register('get-profile-info',  GetProfileInfoView, "get-profile-info" ),

urlpatterns = [
    path('', include(router.urls)),
]
