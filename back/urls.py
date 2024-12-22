from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
from higher_control.user_control.views import MyTokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from back.views import *
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView


router = DefaultRouter()

# Register ViewSets with the router
router.register(r"mesomb", MeSombPaymentViewSet, basename="mesomb")

urlpatterns = [
    # Include router URLs for ViewSets
    path("", include(router.urls)),

    # Define paths for regular views
    path('token/', csrf_exempt(MyTokenObtainPairView.as_view()), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('download', download_apk, name="download"),
    # path('graphql', GraphQLView.as_view(graphiql=True)),  # GraphiQL enabled for testing
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),


    # Admin and app-specific URLs
    path('e-admin/', admin.site.urls),
    path('tenant/', include('tenant.urls')),
    path('higher/', include('higher_control.urls')),
    path('secondary/', include('secondary_control.urls')),
    path('primary/', include('primary_control.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_reset/confirm/', include('django_rest_passwordreset.urls', namespace='password_confirm')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
