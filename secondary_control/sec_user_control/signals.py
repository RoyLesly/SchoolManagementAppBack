from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.dispatch import receiver
from .models import CustomUser, UserProfile
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

# update full name
@receiver(pre_save, sender=CustomUser)
def update_customuser_full_name(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        for i in range(1, 2):
            instance.full_name = f"{instance.first_name} {instance.last_name}"

            
# useractivity create
# @receiver(post_save, sender=CustomUser)
# def register_status_change(sender, instance: CustomUser, **kwargs):
#     if instance.last_login_id != instance.cached_last_login_id:
#         # There is a status change
#         UserActivity.objects.create(
#             username=instance.username,
#             action="Login"
#             )
            
            
# Notify user creation            
@receiver(post_save, sender=CustomUser)
def send_mail_verification(sender, created, instance, **kwargs):
    if created and not instance.email_confirmed and instance.role == "student" and instance.email != None:
        verification_link = f"https://apibrains.econneq.com/user/user_verify_email/{instance.pk}/"
        username = f"{instance.username.capitalize()}"
        user_name = f"{instance.username}"
        subject = "Account Creation (THE BRAINS)"
        receivers = f"{instance.email}"
        matricle = f"{instance.matricle}"
        context = {
            "verification_link": verification_link,
            "username": username,
            "user_name": user_name,
            "receivers": receivers,
            "matricle": matricle,
        }
        html_message = render_to_string("content/student_account_created_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[receivers,]
        )

        message.attach_alternative(html_message, "text/html")
        # message.send()

    elif created and not instance.email_confirmed and instance.role != "student" and instance.email != None:
        verification_link = f"https://apibrains.econneq.com/user/user_verify_email/{instance.pk}/"
        username = f"{instance.username.capitalize()}"
        user_name = f"{instance.username}"
        subject = "Account Creation (THE BRAINS)"
        receivers = f"{instance.email}"
        context = {
            "verification_link": verification_link,
            "username": username,
            "user_name": user_name,
            "receivers": receivers
        }
        html_message = render_to_string("content/other_account_created_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[receivers,],
            bcc=["wemoov13@gmail.com"]
        )

        message.attach_alternative(html_message, "text/html")
        # message.send()
    else:
        pass
        

# notify user update
# @receiver(post_save, sender=CustomUser)
# def send_update_mail(sender, created, instance, **kwargs):
#     if created:
#         pass
#     else:
#         if instance.email is not None and not instance.email_confirmed:
#             verification_link = f"https://apibrains.econneq.com/user/user_verify_email/{instance.pk}/"
#             username = f"{instance.username.capitalize()}"
#             user_name = f"{instance.username}"
#             subject = "Account Update (The Brains)"
#             receivers = f"{instance.email}"
#             matricle = f"{instance.matricle}"
#             context = {
#                 "verification_link": verification_link,
#                 "username": username,
#                 "user_name": user_name,
#                 "receivers": receivers,
#                 "matricle": matricle,
#             }
#             html_message = render_to_string("content/account_update_email.html", context=context)
#             plain_message = strip_tags(html_message)
    
#             message = EmailMultiAlternatives(
#                 subject=subject,
#                 body=plain_message,
#                 from_email=settings.EMAIL_HOST_USER,
#                 to=[receivers, ],
#                 bcc=["wemoov13@gmail.com"]
#             )
#             message.attach_alternative(html_message, "text/html")
#             message.send()
        

# send password token       
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'token':reset_password_token.key,
        'reset_password_url': "https://resultbrains.econneq.com/pageAuthentication/PasswordAndToken"
    }

    email_html_message = render_to_string('content/password_reset_email.html', context)
    email_plaintext_message = render_to_string('content/password_reset_email.txt', context)

    msg = EmailMultiAlternatives(
        subject="Password Reset for {title}".format(title=reset_password_token.user.username),
        body=email_plaintext_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[reset_password_token.user.email,]
    )
    msg.attach_alternative(email_html_message, "text/html")
    # msg.send()

    