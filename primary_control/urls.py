from django.urls import path, include

app_name = "primary_control"

urlpatterns = [
    path('prim_user_control/', include('primary_control.prim_user_control.urls')),
    path('prim_app_control/', include('primary_control.prim_app_control.urls')),
]