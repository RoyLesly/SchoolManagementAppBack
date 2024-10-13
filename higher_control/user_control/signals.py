from django.db.models.signals import post_save, pre_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.dispatch import receiver
from .models import CustomUser, UserProfile
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_rest_passwordreset.signals import reset_password_token_created
import importlib


# update full name
@receiver(pre_save, sender=CustomUser)
def update_customuser_full_name(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        instance.full_name = f"{instance.first_name} {instance.last_name}"


# Notify user creation            
@receiver(post_save, sender=CustomUser)
def send_email_notification(sender, created, instance, **kwargs):
    module_school_name = importlib.import_module("higher_control.app_control").models.SchoolInfo
    if created and instance.role != "student":
        verification_link = f"https://apibrains.econneq.com/user/user_verify_email/{instance.pk}/"
        username = f"{instance.username.capitalize()}"
        subject = "Account Updates"
        receivers = f"{instance.email}"
        matricle = f"{instance.matricle}"
        school = module_school_name.objects.get(id=1)
        message = f"Welcome Your Account Has Been Created on the System"
        context = {
            "verification_link": verification_link,
            "username": username,
            "receivers": receivers,
            "matricle": matricle,
            "school": school,
            "message": message,
        }
        html_message = render_to_string("content/account_update_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[receivers, ],
            bcc=["wemoov13@gmail.com"],
        )

        message.attach_alternative(html_message, "text/html")
        message.send()


# send password token       
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'token': reset_password_token.key,
        'reset_password_url': "https://"
    }

    email_html_message = render_to_string('content/password_reset_email.html', context)
    email_plaintext_message = render_to_string('content/password_reset_email.txt', context)

    msg = EmailMultiAlternatives(
        subject="Password Reset for {title}".format(title=reset_password_token.user.first_name),
        body=email_plaintext_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[reset_password_token.user.email, ]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
