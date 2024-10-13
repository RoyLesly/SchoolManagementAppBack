import importlib
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


now = datetime.now()


def create_school_identification(sender, **kwargs):
    module_school_iden = importlib.import_module("secondary_control.sec_app_control").models.SchoolIdentification
    if kwargs['created']:
        if not module_school_iden.objects.all():
            print(11, module_school_iden)
            school_iden = module_school_iden.objects.create(
                code="ABC12XYZ",
            )
            school_iden.save()


def create_result_from_subject(sender, **kwargs):
    module_secondaryprofile = importlib.import_module("secondary_control.sec_user_control").models.SecondaryProfile
    module_result = importlib.import_module("secondary_control.sec_app_control").models.SecondaryResult
    module_publish = importlib.import_module("secondary_control.sec_app_control").models.SecondaryPublish
    created_subject = kwargs['instance']
    created_subject_classroom_id = created_subject.classroom.id
    user_profiles = module_secondaryprofile.objects.filter(secondary_classroom__id=created_subject_classroom_id)
    pub = module_publish.objects.filter(secondary_classroom__id=created_subject.classroom.id)
    if user_profiles:
        for prof in user_profiles:
            if pub:
                try:
                    module_result.objects.create(
                        student = prof,
                        subject = created_subject,
                    )
                except:
                    pass
            else:
                try:
                    module_result.objects.create(
                        student = prof,
                        subject = created_subject,
                    )
                except:
                    pass


def create_publish_from_result(sender, **kwargs):
    module_publish = importlib.import_module("app_control").models.Publish
    instance = kwargs["instance"]
    if (kwargs["created"]):
        pub = module_publish.objects.filter(classroom__id=instance.student.classroom.id)
        if not pub:
            pub_type = [ "term", "sequence"]
            pub_item_sequence = [
                "publish_seq_1", "publish_seq_2", "publish_seq_3", 
                "publish_seq_4", "publish_seq_5", "publish_seq_6",
            ]
            pub_item_term = [ "publish_term_1", "publish_term_2", "publish_term_3" ]

            for t in pub_type:
                if t == "term":
                    for i in pub_item_term:
                        module_publish.objects.create(
                            classroom = instance.student.classroom,
                            publish_type = t,
                            publish_item = i,
                            publish = False,
                            created_by = instance.created_by,
                            updated_by = instance.updated_by,
                        )
                if t == "sequence":
                    for i in pub_item_sequence:
                        module_publish.objects.create(
                            classroom = instance.student.classroom,
                            publish_type = t,
                            publish_item = i,
                            publish = False,
                            created_by = instance.created_by,
                            updated_by = instance.updated_by,
                        )


def update_results_from_publish(sender, **kwargs):
    module_result = importlib.import_module("app_control").models.Result
    instance = kwargs["instance"]
    if not kwargs["created"]:
        try:
            results = module_result.objects.filter(student__classroom__id=instance.classroom.id)
            pub_type = instance.publish_type
            pub_item = instance.publish_item
            if results:
                for res in results:
                    if pub_type == "term":
                        if pub_item == "publish_term_1":
                            res.publish_term_1 = instance.publish
                        if pub_item == "publish_term_2":
                            res.publish_term_2 = instance.publish
                        if pub_item == "publish_term_3":
                            res.publish_term_3 = instance.publish
                    if pub_type == "sequence":
                        if pub_item == "publish_seq_1":
                            res.publish_seq_1 = instance.publish
                        if pub_item == "publish_tseq2":
                            res.publish_seq_2 = instance.publish
                        if pub_item == "publish_seq_3":
                            res.publish_seq_3 = instance.publish
                        if pub_item == "publish_seq_4":
                            res.publish_seq_4 = instance.publish
                        if pub_item == "publish_seq_5":
                            res.publish_seq_5 = instance.publish
                        if pub_item == "publish_seq_6":
                            res.publish_seq_6 = instance.publish
                    res.save()
        except:
            pass