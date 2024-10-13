import importlib
from datetime import datetime

now = datetime.now()

def update_tuition_balance_from_transaction(sender, **kwargs):
    module_school_fees = importlib.import_module("secondary_control.sec_fees_control").models.SecSchoolFees
    created_item = kwargs['instance']
    sf = module_school_fees.objects.get(id=created_item.secschoolfees.id)
    if kwargs['created']:
        if created_item.reason == "SCHOLARSHIP":
            sf.balance -= created_item.amount
        if created_item.reason == "TUITION":
            sf.balance -= created_item.amount
        if created_item.reason == "PLATFORM CHARGES":
            if sf.platform_charges <= created_item.amount:
                sf.platform_paid = True
        sf.save()
    # prof = module_user_profiles.objects.filter(user__role="student").exclude(specialty__isnull=True)
    # for p in prof:
    #     try:
    #         school_fees = module_school_fees.objects.create(
    #                 userprofile = p,
    #                 balance = p.specialty.tuition,
    #                 platform_paid = True
    #             )
    #         schoolFees.save()
    #     except:
    #         pass
        

