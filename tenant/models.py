from django.db import models
from higher_control.user_control.models import CustomUser
from django_tenants.models import DomainMixin, TenantMixin
from .choices import *
from django.core.validators import EmailValidator, RegexValidator


TYPE = (
    ("Primary", "Primary"), ("Secondary", "Secondary"),
    ("University", "University"), ("Vocational", "Vocational"),
)


class Tenant(TenantMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    school_name = models.CharField(max_length=50)
    school_type = models.CharField(choices=TYPE, max_length=50)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    """
    USE THIS WITH CAUTION!
    Set this flag to true on a parent class if you want the schema to be
    automatically deleted if the tenant row gets deleted.
    """
    auto_drop_schema = True

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f"{self.school_name}"


class Domain(DomainMixin):
    pass


class CreatedUpdatedModel(models.Model):
    created_by = models.ForeignKey(CustomUser, null=True, on_delete=models.PROTECT, related_name="%(class)s_created_by")
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name="%(class)s_updated_by")
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class SchoolIdentification(CreatedUpdatedModel):
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    code = models.CharField(max_length=8, null=False, blank=False)
    version = models.CharField(max_length=10, blank=False)
    director = models.CharField(max_length=50, blank=False, null=False, default="Edit")
    platform_charges = models.IntegerField(blank=False, null=False, default=1000)
    name = models.CharField(max_length=80, null=False, blank=False, default="")
    support_number_one = models.CharField(max_length=15, null=False, blank=False, default="693358642")
    support_number_two = models.CharField(max_length=15, null=False, blank=False, default="690640864")
    status = models.BooleanField(default=True, null=False, blank=False)
    back_end = models.CharField(max_length=75, default="http://127.0.0.1:8000", null=False, blank=False)
    front_end = models.CharField(max_length=75, default="http://apitest.econneq.com", null=False, blank=False)
    created_by = models.ForeignKey(CustomUser, null=True, related_name='schoolidentification_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='schoolidentification_updated_by', on_delete=models.PROTECT)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
    

class Setting(CreatedUpdatedModel):
    prefix = models.CharField(max_length=10,  blank=False, null=False, default="TEST")
    method = models.IntegerField(blank=False, null=False, default=2)
    school_type = models.CharField(max_length=15, choices=CAMPUS_TYPES, null=False, blank=False, default="Higher")
    school_name = models.CharField(max_length=50, blank=False)
    short_name = models.CharField(max_length=20, blank=False)   
    main_school = models.BooleanField(default=False)
    address = models.CharField(max_length=20, blank=False, null=False, default="Douala")
    region = models.CharField(max_length=12, choices=REGION_CHOICES, blank=False)
    town = models.CharField(max_length=10, blank=False, null=False, default="Douala")
    country = models.CharField(max_length=12, blank=False, default="CAMEROON")
    po_box = models.CharField(max_length=50, blank=False)
    niu = models.CharField(max_length=50, blank=False)    
    website = models.CharField(max_length=45, blank=False, null=False, default="https://test.e-conneq.com")
    latitude = models.CharField(max_length=10, blank=False, default=3.8436864)
    longitude = models.CharField(max_length=10, blank=False, default=11.4917376)
    landing_message_main = models.CharField(blank=False, null=False, default="Welcome")
    logo_campus = models.ImageField(upload_to='school_logo/', null=True, blank=True)
    registration_seperate_tuition = models.BooleanField(blank=False, null=False, default=True)
    schoolfees_control = models.CharField(max_length=255, blank=False, null=False, default="0.50, 0.80, 0.99, 1, 1, 1")
    welcome_message = models.CharField(max_length=255, blank=False, null=False, default="Welcome To, Econneq")
    radius = models.IntegerField(blank=False, default=100)
    email = models.CharField( max_length=40,  blank=False, 
        validators=[EmailValidator(message="Enter a valid email address.")]
    )    
    telephone = models.CharField( max_length=15, blank=False,  null=False, 
        default="+237670000000", 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+XXX XXXXXXXXX'. Up to 15 digits allowed."
        )]
    )
    created_by = models.ForeignKey(CustomUser, null=True, related_name='school_created_by', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, null=True, related_name='school_updated_by', on_delete=models.SET_NULL)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        