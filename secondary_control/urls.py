from django.urls import path, include

app_name = "secondary_control"

urlpatterns = [
    path('sec_user_control/', include('secondary_control.sec_user_control.urls')),
    path('sec_app_control/', include('secondary_control.sec_app_control.urls')),
    path('sec_fees_control/', include('secondary_control.sec_fees_control.urls')),
]