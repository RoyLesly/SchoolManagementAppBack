from datetime import datetime
import importlib


def deactivate_notifications(sender, **kwargs):
    now = datetime.now().date()
    notif = importlib.import_module("higher_control.noti_control").models.Notification
    if kwargs["created"]:
        created = kwargs["instance"]
        if created.created_at < now:
            created.status = False
        else:
            created.status = True
            created.save()
    else:
        noti = notif.objects.filter(status=True, created_at__year=now.year)
        for n in noti:
            if n.ending_at < now:
                n.status = False
                # n.save()
