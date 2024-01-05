import importlib
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


now = datetime.now()
# date = now().date()
# time = now().time()


def generate_matricle(sender, **kwargs):
    module_custom_user = importlib.import_module("user_control").models.CustomUser
    all_users_this_year = module_custom_user.objects.filter(created_at__year=now.strftime("%Y"))
    instance = kwargs["instance"]
    pref = str(now.strftime("%Y")[2: 4]) + "SJH"
    if kwargs["created"]:
        if all_users_this_year:
            mat = [f.matricle for f in all_users_this_year if "SJH" in f.matricle]
            strip_mat = [int(i[5:]) for i in mat]
            try:  
                if (len(strip_mat) > 0) :         
                    mat = pref + str(strip_mat[-1] + 1).zfill(4) 
                else:
                    mat = pref + str(instance.id).zfill(4)
            except:
                mat = pref + str(instance.id).zfill(4)
        else:
            mat = pref + str(instance.id).zfill(4)
        if (instance.role == "student"):
            instance.matricle = mat
            instance.save()
        else:
            instance.matricle = instance.id
            instance.save()


def create_profile(sender, **kwargs):
    module_user_profile = importlib.import_module("user_control").models.UserProfile
    created_item = kwargs['instance']
    if kwargs['created']:
        prof = module_user_profile.objects.create(
                user = created_item,
            )
        prof.save()


def create_appearance(sender, **kwargs):
    module_appearance = importlib.import_module("user_control").models.Appearance
    created_item = kwargs['instance']
    if kwargs['created']:
        appearance = module_appearance.objects.create(
                user = created_item,
                # created_by = created_item.created_by,
            )
        appearance.save()


def create_result_from_profile(sender, **kwargs):
    module_course = importlib.import_module("app_control").models.Course
    module_result = importlib.import_module("app_control").models.Result
    try:
        courses_student = module_course.objects.filter(specialty__id=kwargs["instance"].specialty.id)
        if courses_student:
            for cou in courses_student:
                try:
                    module_result.objects.create(
                        student = kwargs["instance"],
                        course = cou,
                    )
                    print("RESULT CREATED")
                except:
                    print("RESULT NOT CREATED")
                    pass
    except:
        pass


def send_email_update(sender, **kwargs):
    instance = kwargs["instance"]
    user = instance.user
    if kwargs["created"]:
        pass
    else:
        email = instance.user.email
        first_name = ""
        last_name = ""
        if not email:
            email = "roylesly@gmail.com"
            print("Email Cannot Be Blank")
        if not user.first_name:
            first_name = "Student"
            print("First Name Cannot Be Blank")
        if not user.last_name:
            last_name = ""
            print("Last Name Cannot Be Blank")
        subject = 'Account update'
        try:
            message = f"Hi, {first_name} {last_name} Your account has been updated. " \
                    f"follow these procedures to set your password.\n\n 1) click check user.\n" \
                    f"2) enter username as '{user.username}' and click check user.\n 3) you will receive a confirmation of account existence and " \
                    f"redirected to create and confirm password.\n 4) after it's successfully created, your will be redirected " \
                    f"to login page enter your username and password you just created. click on login.\n\n" \
                    f"To check user https://result.st-joan.com/PageHome/CheckUser\n\n"\
                    f"____________________________\n"\
                  f"You are recieving this mail because your account was updated, if you already setup a password, don't consider following any of these steps"
            send_mail(subject, message, "nleslynsom@gmail.com", [email], fail_silently=False, )
        except:
            print("MAIL NOT SENT")


def send_token_to_email(instance, **kwargs):
    if instance:
        if not instance.user.email:
            raise Exception("User Has No Email")
        subject = 'st-joan Account Password Reset'        
        try:
            message = f"Hi, {instance.first_name.capitalize()} {instance.last_name.capitalize()} Your have Requested for a password Reset. " \
                    f"follow these procedures to reset your password.\n\n" \
                    f"1) Copy the copy below and paste in the field provided"\
                    f"2) Create New Password and Confirm"\
                    f"{instance.t}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email], fail_silently=False, )
        except:
            raise Exception("Email Not Sent, Contact Admin")
        

def send_confirmation_email(sender, instance, created, **kwargs):       # See signals as well
    if created:
        pass
    else:
        subject = 'Please confirm your email address'
        message = f"Hi, {instance.username.capitalize()} Your account has been updated. Please click the link below " \
                  f"to login {settings.SITE_URL} and follow these procedure to set your password. click check user" \
                  f"enter username as  and click check user, you will receive a confirmation of account existence and " \
                  f"redirected to create and confirm password after it's successfully created your will be redirected " \
                  f"to login page enter your username and password you just created and click on login." \
                  f"To check user https://result.st-joan.com/PageHome/CheckUser"
        send_mail(subject, message, settings.EMAIL_HOST_USER, ["tanyiclifort@gmail.com"], fail_silently=False)




