from django.db.models.signals import post_save
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.dispatch import receiver
from .models import CustomUser
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# @receiver(post_save, sender=CustomUser)
# def send_confirmation_email(sender, instance, created, **kwargs):
#     if created and instance.role == "student":
#         subject = 'Student Account Creation'
#         link_app = "https://result.st-joan.com"
#         username = f"{instance.username.capitalize()}"
#         matrcule = f"{instance.matricle}"
#         context = {
#             "link_app": link_app,
#             "username": username,
#             "matrcule": matrcule
#         }
#         html_message = render_to_string("content/student_account_created_email.html", context=context)
#         plain_message = strip_tags(html_message)
#
#         message = EmailMultiAlternatives(
#             subject=subject,
#             body=plain_message,
#             from_email=settings.EMAIL_HOST_USER,
#             to=["wemoov13@gmail.com"]
#         )
#
#         message.attach_alternative(html_message, "text/html")
#         message.send()
#     elif created and instance.role != "student":
#         subject = 'Lecturer Account Creation'
#         link_app = "https://result.st-joan.com"
#         username = f"{instance.username.capitalize()}"
#         context = {
#             "link_app": link_app,
#             "username": username
#         }
#         html_message = render_to_string("content/other_account_created_email.html", context=context)
#         plain_message = strip_tags(html_message)
#
#         message = EmailMultiAlternatives(
#             subject=subject,
#             body=plain_message,
#             from_email=settings.EMAIL_HOST_USER,
#             to=["wemoov13@gmail.com"]
#         )
#
#         message.attach_alternative(html_message, "text/html")
#         message.send()


@receiver(post_save, sender=CustomUser)
def send_mail_verification(sender, created, instance, **kwargs):
    if created and not instance.email_confirmed:
        verification_link = f"https://st-joan.com/back/user/verify_email/{instance.pk}/"
        username = f"{instance.username.capitalize()}"
        subject = "Email Verification (SAJOHIM)"
        receivers = f"{instance.email}"
        context = {
            "verification_link": verification_link,
            "username": username,
            "receivers": receivers
        }
        html_message = render_to_string("content/verify_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=["wemoov13@gmail.com", receivers]
        )

        message.attach_alternative(html_message, "text/html")
        message.send()


@receiver(post_save, sender=CustomUser)
def send_mail_confirmation(sender, created, instance, **kwargs):
    if instance.email_confirmed and instance.role == "student":
        subject = 'Student Account Creation'
        link_app = "https://result.st-joan.com"
        username = f"{instance.username.capitalize()}"
        matrcule = f"{instance.matricle}"
        receivers = f"{instance.email}"
        context = {
            "link_app": link_app,
            "username": username,
            "matrcule": matrcule,
            "receivers": receivers
        }
        html_message = render_to_string("content/student_account_created_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=["wemoov13@gmail.com", receivers]
        )

        message.attach_alternative(html_message, "text/html")
        message.send()

    elif instance.email_confirmed and instance.role != "student":
        subject = 'Lecturer Account Creation'
        link_app = "https://result.st-joan.com"
        username = f"{instance.username.capitalize()}"
        receivers = f"{instance.email}"
        context = {
            "link_app": link_app,
            "username": username,
            "receivers": receivers
        }
        html_message = render_to_string("content/other_account_created_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=["wemoov13@gmail.com", receivers]
        )

        message.attach_alternative(html_message, "text/html")
        message.send()

