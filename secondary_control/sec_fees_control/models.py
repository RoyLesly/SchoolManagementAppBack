from django.db import models
from higher_control.user_control.models import CustomUser, UserProfile
from django.db.models.signals import post_save
from .choices import *
from .functions import *


class ActivationKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='secpayment_method_created_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='secpayment_method_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Activation"

    def __str__(self):
        return f"{self.key}"


class SecSchoolFees(models.Model):
    secondaryprofile = models.OneToOneField("sec_user_control.SecondaryProfile", related_name="secschoolfees_userprofile", null=False, on_delete=models.PROTECT )
    platform_charges = models.IntegerField(default=1000)
    platform_paid = models.BooleanField(default=False)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # return "s"
        return f"{self.secondaryprofile.user.username} -  {self.secondaryprofile.secondary_classroom.level}"

    class Meta:
        ordering = ("-balance",)
        verbose_name_plural = "Sec School Fees"
    
    
class SecTransactions(models.Model):
    secschoolfees = models.ForeignKey(SecSchoolFees, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    reason = models.CharField(max_length=255, choices=REASON, blank=False, null=False)
    ref = models.CharField(max_length=35, blank=True, null=True)

    amount = models.IntegerField(blank=False, null=False)
    telephone = models.IntegerField(blank=True, null=True)
    payer_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, default="Pending")
    operator = models.CharField(max_length=255, choices=OPERATOR, null=True, blank=True)

    created_by = models.ForeignKey(CustomUser, null=True, related_name='sec_transaction_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='sec_transaction_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.secschoolfees.secondaryprofile.user.username}"
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Sec Transactions"

post_save.connect(update_tuition_balance_from_transaction, sender=SecTransactions)
