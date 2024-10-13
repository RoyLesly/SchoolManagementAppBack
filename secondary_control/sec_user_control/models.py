from django.db import models
from django.db.models.signals import post_save
from .functions import *
from .choices import *

class SecondaryProfile(models.Model):
    user = models.ForeignKey("user_control.CustomUser", related_name="secondaryprofile_user", null=True, on_delete=models.PROTECT )
    secondary_classroom = models.ForeignKey("sec_app_control.SecondaryClassRoom", blank=True, null=True, related_name='secondaryprofile_classroom', on_delete=models.SET_NULL)
    active = models.BooleanField(default=True, blank=False)
    session = models.CharField(default="Morning", choices=SESSION_CHOICES, max_length=10, blank=False, null=False)
    code = models.ImageField(blank=True, null=True, upload_to="code")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [ 
            models.UniqueConstraint(fields=["secondary_classroom", "user"], name="unique_secondaryprofile"),
        ]

    def __str__(self):
        return f"{self.user.username}"          

post_save.connect(create_code_sec_profile, sender=SecondaryProfile)
# post_save.connect(create_result_from_profile, sender=UserProfile)
# post_save.connect(profile_activate_deactivate_results, sender=UserProfile)
# post_save.connect(create_schoolfees, sender=UserProfile)