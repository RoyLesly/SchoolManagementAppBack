from django.db import models
from higher_control.user_control.models import CustomUser
from django_tenants.models import DomainMixin, TenantMixin

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
