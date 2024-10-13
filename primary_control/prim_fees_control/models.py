from django.db import models
from higher_control.user_control.models import CustomUser, UserProfile
from django.db.models.signals import post_save
from .choices import *
from .functions import *


class PrimActivationKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='primpayment_method_created_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='primpayment_method_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Activation"

    def __str__(self):
        return f"{self.key}"


class PrimSchoolFees(models.Model):
    primaryprofile = models.OneToOneField("prim_user_control.PrimaryProfile", related_name="primschoolfees_userprofile", null=True, on_delete=models.PROTECT )
    platform_charges = models.IntegerField(default=1000)
    platform_paid = models.BooleanField(default=False)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.userprofile.user.username} -  {self.userprofile.specialty.main_specialty.specialty_name}"

    class Meta:
        ordering = ("-balance",)
        verbose_name_plural = "Sec School Fees"
    
    
class PrimTransactions(models.Model):
    primschoolfees = models.ForeignKey(PrimSchoolFees, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    reason = models.CharField(max_length=255, choices=REASON, blank=False, null=False)
    ref = models.CharField(max_length=35, blank=True, null=True)

    amount = models.IntegerField(blank=False, null=False)
    telephone = models.IntegerField(blank=True, null=True)
    payer_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, default="Pending")
    operator = models.CharField(max_length=255, choices=OPERATOR, null=True, blank=True)

    created_by = models.ForeignKey(CustomUser, null=True, related_name='prim_transaction_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='prim_transaction_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.schoolfees.userprofile.user.username}"
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Prim Transactions"

post_save.connect(update_tuition_balance_from_transaction, sender=PrimTransactions)
