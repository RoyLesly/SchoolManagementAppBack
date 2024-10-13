from datetime import datetime
import importlib


def deactivate_notifications(sender, **kwargs):
    now = datetime.now().date()
    notifica = importlib.import_module("higher_control.noti_control").models.Notification
    noti = notifica.objects.filter(status=True, created_at__year=now.year)
    for n in noti:
        if n.ending_at < now:
            n.status = False
            n.save()
