from django.db import models


class PrimaryProfile(models.Model):
    user = models.ForeignKey("user_control.CustomUser", related_name="primaryprofile_user", null=True, on_delete=models.PROTECT )
    primary_classroom = models.ForeignKey("prim_app_control.PrimaryClassRoom", blank=True, null=True, related_name='primaryprofile_classroom', on_delete=models.SET_NULL)
    active = models.BooleanField(default=True, blank=False)
    code = models.ImageField(blank=True, null=True, upload_to="code")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [ 
            models.UniqueConstraint(fields=["primary_classroom", "user"], name="unique_primaryprofile"),
        ]

    def __str__(self):
        return f"{self.user.username}"          

# post_save.connect(create_code_profile, sender=UserProfile)
# post_save.connect(create_result_from_profile, sender=UserProfile)
# post_save.connect(profile_activate_deactivate_results, sender=UserProfile)
# post_save.connect(create_schoolfees, sender=UserProfile)