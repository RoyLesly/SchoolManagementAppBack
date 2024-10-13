from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import ( 
    TokenRefreshView,
)
from higher_control.user_control.views import MyTokenObtainPairView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('token/', csrf_exempt(MyTokenObtainPairView.as_view()), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('admin/', admin.site.urls),
    path('tenant/', include('tenant.urls')),
    path('higher/', include('higher_control.urls')),
    path('secondary/', include('secondary_control.urls')),
    path('primary/', include('primary_control.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_reset/confirm/', include('django_rest_passwordreset.urls', namespace='password_confirm')),

] \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
