from datetime import datetime


matricle_format_name = "BU"

def registration_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.generate_registration_number()
        instance.save()
        