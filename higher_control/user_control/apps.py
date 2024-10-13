from django.apps import AppConfig


class UserControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'higher_control.user_control'

    # def ready(self):
    #     import user_control.signals
    