from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "fees_control"

router = routers.DefaultRouter(trailing_slash=False)

router.register('schoolfees',  SchoolFeesView, "schoolfees" ),
router.register('get-schoolfees',  GetSchoolFeesView, ",get-schoolfees" ),
router.register('transactions',  TransactionsView, "transactions" ),
router.register('get-transactions',  GetTransactionsView, ",get-transactions" ),
router.register('activationkey',  ActivationKeyView, "activationkey" ),
router.register('get-activationkey',  ActivationKeyView, ",get-activationkey" ),

urlpatterns = [
    path('', include(router.urls)),
]
