from django.urls import path, include

app_name = "higher_control"

urlpatterns = [
    path('higher_user_control/', include('higher_control.user_control.urls')),
    path('higher_app_control/', include('higher_control.app_control.urls')),
    path('higher_fees_control/', include('higher_control.fees_control.urls')),
    path('higher_noti_control/', include('higher_control.noti_control.urls')),
    path('higher_time_control/', include('higher_control.time_control.urls')),
    # path('higher_chat_control/', include('higher_control.chat_control.urls')),
]