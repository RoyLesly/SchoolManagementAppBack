from django.db import models
from higher_control.user_control.models import CustomUser, UserProfile
from django.db.models.signals import post_save
from .choices import *
from .functions import *


class ActivationKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='payment_method_created_by', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='payment_method_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Activation"

    def __str__(self):
        return f"{self.key}"


class SchoolFees(models.Model):
    userprofile = models.OneToOneField( UserProfile, related_name="schoolfees_userprofile", null=True, on_delete=models.PROTECT )
    platform_charges = models.IntegerField(default=1000)
    platform_paid = models.BooleanField(default=False)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.userprofile.user.first_name}-{self.userprofile.specialty.academic_year}-PI{self.userprofile.id}-UI{self.userprofile.user.id}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "School Fees"

    
class Account(models.Model):
    name = models.CharField(max_length=35, blank=True, null=True)
    number = models.CharField(max_length=35, blank=True, null=True)
    year = models.CharField(blank=False, null=False, default="2023/2024")
    balance = models.IntegerField(blank=False, null=False, default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.number}"
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Accounts"
        constraints = [ 
            models.UniqueConstraint(fields=["name", "year"], name="unique_account")
        ]

    
class Transactions(models.Model):
    schoolfees = models.ForeignKey(SchoolFees, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    account = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=255, default="Edit", blank=False, null=False)
    ref = models.CharField(max_length=35, blank=True, null=True)
    operation_type = models.CharField(max_length=8, default="income", null=False, blank=False)
    origin = models.CharField(max_length=8, default="admin", null=False, blank=False)

    amount = models.IntegerField(blank=False, null=False)
    telephone = models.IntegerField(blank=True, null=True)
    payer_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, default="Pending")
    from_account = models.ForeignKey(Account, blank=True, null=True, related_name='from_account', on_delete=models.PROTECT)
    to_account = models.ForeignKey(Account, blank=True, null=True, related_name='to_account', on_delete=models.PROTECT)
    operator = models.CharField(max_length=255, choices=OPERATOR, null=True, blank=True)

    created_by = models.ForeignKey(CustomUser, null=True, related_name='transaction_created_by', on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='transaction_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.schoolfees.userprofile.user.first_name}"
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Transactions"

post_save.connect(update_tuition_balance_from_transaction, sender=Transactions)
post_save.connect(update_account_balance_from_transaction, sender=Transactions)


class TranscriptApplication(models.Model):
    userprofile = models.OneToOneField( UserProfile, related_name="transcript_userprofile", null=True, on_delete=models.PROTECT )
    print_count = models.IntegerField(null=False, blank=False, default=0 )
    status = models.CharField(max_length=20, choices=TRANSCRIPT_APPLICATION_STATUS, null=False, blank=False)
    approved_by = models.ForeignKey(CustomUser, null=True, related_name='trancript_approved_by', on_delete=models.SET_NULL)
    approved_at = models.DateTimeField(null=True, blank=True)
    printed_by = models.ForeignKey(CustomUser, null=True, related_name='transcript_printed_by', on_delete=models.SET_NULL)
    printed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.userprofile.user.username} -  {self.userprofile.specialty.main_specialty.specialty_name}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Transcript Applications"