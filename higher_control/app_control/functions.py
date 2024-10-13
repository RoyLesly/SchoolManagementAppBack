import importlib
from datetime import datetime
from higher_control.noti_control.models import Notification

now = datetime.now()

        
def create_school_identification(sender, **kwargs):
    module_school_iden = importlib.import_module("higher_control.app_control").models.SchoolIdentification
    print(11, module_school_iden)
    if kwargs['created']:
        if not module_school_iden.objects.all():
            print(11, module_school_iden)
            school_iden = module_school_iden.objects.create(
                code="ABC12XYZ",
            )
            school_iden.save()


def create_result_from_course(sender, **kwargs):
    module_user_profile = importlib.import_module("higher_control.user_control").models.UserProfile
    module_result = importlib.import_module("higher_control.app_control").models.Result
    module_publish = importlib.import_module("higher_control.app_control").models.Publish
    created_course = kwargs['instance']
    created_course_specialty_id = created_course.specialty.id
    user_profiles = module_user_profile.objects.filter(specialty__id=created_course_specialty_id)
    pub = module_publish.objects.filter(specialty__id=created_course.specialty.id, semester=created_course.semester)
    if user_profiles:
        for prof in user_profiles:
            if pub:
                try:
                    module_result.objects.get_or_create(
                        student = prof,
                        course = created_course,
                        publish_ca = pub[0].ca,
                        publish_exam = pub[0].exam,
                        publish_resit = pub[0].resit,
                    )
                except:
                    print("line 33 ========> Error")
                    pass
            else:
                try:
                    module_result.objects.create(
                        student = prof,
                        course = created_course,
                    )
                except:
                    print("line 43 ========> Error")
                    pass


def create_publish_from_specialty(sender, **kwargs):
    module_publish = importlib.import_module("higher_control.app_control").models.Publish
    instance = kwargs["instance"]
    if (kwargs["created"]):
        pub_one = module_publish.objects.filter(specialty__id=instance.id, semester="I")
        pub_two = module_publish.objects.filter(specialty__id=instance.id, semester="II")
        if not pub_one:
            module_publish.objects.create(
                specialty = instance,
                semester = "I",
                ca = False,
                exam = False,
                resit = False,
                created_by = instance.created_by,
                updated_by = instance.updated_by,
            )
        if not pub_two:
            module_publish.objects.create(
                specialty = instance,
                semester = "II",
                ca = False,
                exam = False,
                resit = False,
                created_by = instance.created_by,
                updated_by = instance.updated_by,
            )


def create_publish_from_result(sender, **kwargs):
    module_publish = importlib.import_module("higher_control.app_control").models.Publish
    instance = kwargs["instance"]
    if (kwargs["created"]):
        pub = module_publish.objects.filter(specialty__id=instance.student.specialty.id, semester=instance.course.semester)
        if not pub:
            module_publish.objects.create(
                specialty = instance.student.specialty,
                semester = "I",
                ca = False,
                exam = False,
                resit = False,
                created_by = instance.created_by,
                updated_by = instance.updated_by,
            )
        if not pub:
            module_publish.objects.create(
                specialty = instance.student.specialty,
                semester = "II",
                ca = False,
                exam = False,
                resit = False,
                created_by = instance.created_by,
                updated_by = instance.updated_by,
            )


def update_results_from_publish(sender, **kwargs):
    module_result = importlib.import_module("higher_control.app_control").models.Result
    module_notification = importlib.import_module("higher_control.noti_control").models.Notification
    instance = kwargs["instance"]
    if not kwargs["created"]:
        try:
            results = module_result.objects.filter(student__specialty__id=instance.specialty.id, course__semester=instance.semester)
            if results:
                for res in results:
                    print(res)
                    res.publish_ca = instance.ca
                    res.publish_exam = instance.exam
                    res.publish_resit = instance.resit
                    res.save()
        except:
            pass
        if instance.ca:
            message_one = "Ca Results Published",
        if instance.exam:
            message_one = "Exam Results Published",
        if instance.resit:
            message_one = "ExaResitm Results Published",
           



