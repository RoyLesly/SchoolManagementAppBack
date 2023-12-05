from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=UserProfile)
def send_confirmation_email(sender, instance, created, **kwargs):
    print("line 10")
    if created:
        pass
    else:
        subject = 'Please confirm your email address'
        message = f"Hi, {instance.user.first_name.capitalize()} Your account has been updated. Please click the link below " \
                  f"to login {settings.SITE_URL} and follow these procedure to set your password. click check user" \
                  f"enter username as  and click check user, you will receive a confirmation of account existence and " \
                  f"redirected to create and confirm password after it's successfully created your will be redirected " \
                  f"to login page enter your username and password you just created and click on login." \
                  f"To check user https://result.st-joan.com/PageHome/CheckUser"
        send_mail(subject, message, settings.EMAIL_HOST_USER, ["roylesly@gmail.com"], fail_silently=False)
        