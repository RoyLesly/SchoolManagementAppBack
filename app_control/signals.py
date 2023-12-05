



def send_mail(sender, **kwargs):
    instance = kwargs["instance"]
    sub = "TESTING"
    message1 = f"{instance.address}"
    message2 = f"{instance.email}"
    print(message1, "LINE 41")
    print(message2, "LINE 42")