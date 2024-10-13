from django.db.models.signals import post_save, pre_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.dispatch import receiver
from .models import Course, Publish
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
import re


# signal course assignment
@receiver(post_save, sender=Course)
def send_email_on_course_assignment(sender, created, instance, **kwargs):
    if created:
        instance.assigned = True
        regex = re.compile('[^a-zA-Z ]')
        link = f"https://resultbrains.econneq.com"
        username = f"{instance.assigned_to.full_name}"
        course = f"{instance.main_course}"
        course_title = regex.sub('', course)
        course_code = f"{instance.course_code}"
        specialty = f"{instance.specialty}"
        semester = f"{instance.semester}"
        hours = f"{instance.hours}"
        subject = "Course Assignment"
        recipient = f"{instance.assigned_to.email}"
        context = {
            "link": link,
            "username": username,
            "course_title": course_title,
            "course_code": course_code,
            "specialty": specialty,
            "semester": semester,
            "hours": hours,
            "recipient": recipient,
        }
        html_message = render_to_string("content/course_assign_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient, ]
        )

        message.attach_alternative(html_message, "text/html")
        message.send()


# update course assignment
@receiver(pre_save, sender=Course)
def send_email_on_course_assignment_update(sender, created, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        regex = re.compile('[^a-zA-Z ]')
        link = f"https://resultbrains.econneq.com"
        username = f"{instance.assigned_to.full_name}"
        course = f"{instance.main_course}"
        course_title = regex.sub('', course)
        course_code = f"{instance.course_code}"
        specialty = f"{instance.specialty}"
        semester = f"{instance.semester}"
        hours = f"{instance.hours}"
        subject = "Course Assignment"
        recipient = f"{instance.assigned_to.email}"
        context = {
            "link": link,
            "username": username,
            "course_title": course_title,
            "course_code": course_code,
            "specialty": specialty,
            "semester": semester,
            "hours": hours,
            "recipient": recipient,
        }
        html_message = render_to_string("content/course_assign_email.html", context=context)
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient, ]
        )

        message.attach_alternative(html_message, "text/html")
        message.send()

# # Published result signals
# @receiver(post_save, sender=Publish)
# def send_mail_Publish_result(sender, created, instance, **kwargs):
#     if created:
#         pass
#     elif instance.ca is True and instance.exam is False and instance.resit is False:
#         link = f"https://resultbrains.econneq.com"
#         specialty = f"{instance.specialty}"
#         semester = f"{instance.semester}"
#         result_type = f"Continuous Assessment"
#         publish_by = f"{instance.updated_by.capitalize()}"
#         subject = "CA Result Published"
#         context = {
#             "link": link,
#             "specialty": specialty,
#             "semester": semester,
#             "result_type": result_type,
#             "publish_by": publish_by
#         }
#         html_message = render_to_string("content/publish_result_email.html", context=context)
#         plain_message = strip_tags(html_message)
#
#         message = EmailMultiAlternatives(
#             subject=subject,
#             body=plain_message,
#             from_email=settings.EMAIL_HOST_USER,
#             to=["jezehclive@gmail.com"],
#             bcc=["wemoov13@gmail.com"]
#         )
#
#         message.attach_alternative(html_message, "text/html")
#         message.send()
#
#     elif instance.ca is True and instance.exam is True and instance.resit is False:
#         link = f"https://resultbrains.econneq.com"
#         specialty = f"{instance.specialty}"
#         semester = f"{instance.semester}"
#         result_type = f"Exams"
#         publish_by = f"{instance.updated_by}"
#         subject = "Exam Result Published"
#         context = {
#             "link": link,
#             "specialty": specialty,
#             "semester": semester,
#             "result_type": result_type,
#             "publish_by": publish_by
#         }
#         html_message = render_to_string("content/publish_result_email.html", context=context)
#         plain_message = strip_tags(html_message)
#
#         message = EmailMultiAlternatives(
#             subject=subject,
#             body=plain_message,
#             from_email=settings.EMAIL_HOST_USER,
#             to=["jezehclive@gmail.com"],
#             bcc=["wemoov13@gmail.com"]
#         )
#
#         message.attach_alternative(html_message, "text/html")
#         message.send()
#
#     elif instance.ca is True and instance.exam is True and instance.resit is True:
#         link = f"https://resultbrains.econneq.com"
#         specialty = f"{instance.specialty}"
#         semester = f"{instance.semester}"
#         result_type = f"Resit"
#         publish_by = f"{instance.updated_by}"
#         subject = "Resit Result Published"
#         context = {
#             "link": link,
#             "specialty": specialty,
#             "semester": semester,
#             "result_type": result_type,
#             "publish_by": publish_by
#         }
#         html_message = render_to_string("content/publish_result_email.html", context=context)
#         plain_message = strip_tags(html_message)
#
#         message = EmailMultiAlternatives(
#             subject=subject,
#             body=plain_message,
#             from_email=settings.EMAIL_HOST_USER,
#             to=["jezehclive@gmail.com"],
#             bcc=["wemoov13@gmail.com"]
#         )
#
#         message.attach_alternative(html_message, "text/html")
#         message.send()
