import importlib
from datetime import datetime, date
from random import randint

now = datetime.now()

def update_tuition_balance_from_transaction(sender, **kwargs):
    module_school_fees = importlib.import_module("higher_control.fees_control").models.SchoolFees
    created_item = kwargs['instance']
    sf = module_school_fees.objects.get(id=created_item.schoolfees.id)
    if kwargs['created']:
        if created_item.account == "SCHOLARSHIP":
            sf.balance -= created_item.amount
        if created_item.account == "TUITION":
            sf.balance -= created_item.amount
        if created_item.account == "PLATFORM CHARGES":
            if sf.platform_charges <= created_item.amount:
                sf.platform_paid = True
        sf.save()
        

def update_account_balance_from_transaction(sender, **kwargs):
    module_account = importlib.import_module("higher_control.fees_control").models.Account
    created_item = kwargs['instance']
    if kwargs['created']:
        if created_item.operation_type == "transfer":
            frm = module_account.objects.get(id=created_item.from_account, year=created_item.schoolfees.userprofile.specialty.academic_year)
            to = module_account.objects.get(id=created_item.to_account, year=created_item.schoolfees.userprofile.specialty.academic_year)
            frm.balance -= created_item.amount
            to.balance += created_item.amount
            frm.save()
            to.save()
        if created_item.operation_type == "income" or created_item.operation_type == "outcome":
            try:
                acc = module_account.objects.get(name=created_item.account, year=created_item.schoolfees.userprofile.specialty.academic_year)
            except:
                acc = module_account.objects.create(
                    name=created_item.account, 
                    number=str(date.today().year)[2: 4] + created_item.reason.capitalize()[0] + str(randint(100, 999)), 
                    year=created_item.schoolfees.userprofile.specialty.academic_year,
                    balance=created_item.amount,
                    status=True,
                )
            if acc:
                if created_item.operation_type == "income":
                    acc.balance += created_item.amount
                if created_item.operation_type == "outcome":
                    acc.balance -= created_item.amount
                acc.status = acc.balance > 0
                acc.save()

        

