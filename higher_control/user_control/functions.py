import importlib
from datetime import datetime
from django.core.files import File
from qrcode import make
from io import BytesIO
from PIL import Image
now = datetime.now()
from higher_control.fees_control.choices import ACCOUNT_NAME


def create_schoolfees(sender, **kwargs):
    module_school_fees = importlib.import_module("higher_control.fees_control").models.SchoolFees
    userprofile = kwargs['instance']
    if not kwargs['created']:
        try:
            module_account = importlib.import_module("higher_control.fees_control").models.Account
            for ac_name in ACCOUNT_NAME:
                if not module_account.objects.get(name=ac_name[0]):
                    m_acc = module_account.objects.create(
                        name = ac_name[0],
                        balance=0,
                        status=False,
                    )
                    m_acc.save()
        except:
            pass
        try:           
            if userprofile.user.role == "student":
                if userprofile.specialty:
                    if module_school_fees.objects.filter(userprofile=userprofile):
                        pass
                    else:
                        try:
                            print("CREATING SCHOOL FESS 2 ===============================")
                            schoolFees = module_school_fees.objects.create(
                                    userprofile = userprofile,
                                    balance = userprofile.specialty.tuition,
                                    platform_charges = userprofile.specialty.school.school_identification.platform_charges,
                                )
                            schoolFees.save()
                        except:
                            pass
        except:
            pass
    else:
        if userprofile.user.role == "student":
            if userprofile.specialty:
                try:
                    if not module_school_fees.objects.filter(userprofile=userprofile):
                        schoolFees = module_school_fees.objects.create(
                                userprofile = userprofile,
                                balance = userprofile.specialty.tuition,
                            )
                        schoolFees.save()
                except:
                    pass


def create_profile(sender, **kwargs):
    module_user_profile = importlib.import_module("higher_control.user_control").models.UserProfile
    module_primary_profile = importlib.import_module("primary_control.prim_user_control").models.PrimaryProfile
    module_secondary_profile = importlib.import_module("secondary_control.sec_user_control").models.SecondaryProfile
    # module_vocationation_profile = importlib.import_module("vocational_control.voc_user_control").models.VocationalProfile
    created_item = kwargs['instance']
    if kwargs['created']:

        print(created_item.school, 64)



def create_appearance(sender, **kwargs):
    module_appearance = importlib.import_module("higher_control.user_control").models.Appearance
    created_item = kwargs['instance']
    if kwargs['created']:
        appearance = module_appearance.objects.create(
            user=created_item,
        )
        appearance.save()


def create_code_profile(sender, **kwargs):
    instance_user_profile = kwargs["instance"]
    instance_user_profile.matricle = instance_user_profile.user.matricle
    if instance_user_profile.code:
        pass
    else:
        if instance_user_profile.specialty:
            if instance_user_profile.specialty.school:
                if instance_user_profile.specialty.school.school_identification:
                    if instance_user_profile.specialty.school.school_identification.front_end and instance_user_profile.id:
                        qrcode_image = make(instance_user_profile.specialty.school.school_identification.front_end + "/pageMyResult/" + str(instance_user_profile.specialty.school.id) + "/" + str(instance_user_profile.id))
                        canvas = Image.new("RGB", (400, 400), "white")
                        canvas.paste(qrcode_image)
                        fname = f'code-{instance_user_profile.user.username}' + '.png'
                        buffer = BytesIO()
                        canvas.save(buffer, "PNG")
                        instance_user_profile.code.save(fname, File(buffer), save=False)
                        canvas.close()
                        instance_user_profile.save()


def create_result_from_profile(sender, **kwargs):
    module_course = importlib.import_module("higher_control.app_control").models.Course
    module_result = importlib.import_module("higher_control.app_control").models.Result
    module_publish = importlib.import_module("higher_control.app_control").models.Publish
    module_user = importlib.import_module("higher_control.user_control").models.CustomUser
    users = module_user.objects.all()
    for u in users:
        u.save()
        
    instance_user_profile = kwargs["instance"]
    try:
        pub = module_publish.objects.filter(specialty__id=instance_user_profile.specialty.id)
        specialty_courses = module_course.objects.filter(specialty__id=kwargs["instance"].specialty.id)
        if specialty_courses:
            for course in specialty_courses:
                if pub:
                    pub_semester = pub.get(semester=course.semester)
                    if not module_result.objects.filter(student=kwargs["instance"], course=course):
                        try:
                            res = module_result.objects.create(
                                student = kwargs["instance"],
                                course = course,
                                publish_ca = pub_semester.ca,
                                publish_exam = pub_semester.exam,
                                publish_resit = pub_semester.resit,
                            )
                            res.save()
                        except:
                            print("RESULT 85 NOT CREATED")
                else:
                    try:
                        res = module_result.objects.create(
                            student = kwargs["instance"],
                            course = course,
                        )
                        res.save()
                    except:
                        print("RESULT NOT CREATED")
    # else:
    except:
        pass


# SIGNAL OK
def profile_activate_deactivate_results(sender, **kwargs):
    print("Activate deactivate ===============================")
    module_result = importlib.import_module("higher_control.app_control").models.Result
    module_user_profile = importlib.import_module("higher_control.user_control").models.UserProfile
    instance_user_profile = kwargs["instance"]


def preinscription_post_save(sender, instance, created, *args, **kwargs):
    if instance.action == "UPDATING":
        pass
    if created and (instance.action == "ADMISSION" or instance.action == "CREATING") and not instance.admission_status:
        if instance.action == "ADMISSION":
            instance.admission_status = True
            instance.status == "ADMITTED"
        else:
            instance.status == "PENDING"
        instance.generate_reg_number()
        instance.save()




