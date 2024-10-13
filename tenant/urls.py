from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsGet import *


app_name = "tenant"

router = routers.DefaultRouter(trailing_slash=False)

router.register('tenant',  TenantView, "tenant" ),
router.register('get-tenant',  GetTenantView, "get-tenant" ),
router.register('domain',  DomainView, "domain" ),
router.register('get-domain',  GetDomainView, "get-domain" ),


urlpatterns = [
    path('', include(router.urls)),
]
