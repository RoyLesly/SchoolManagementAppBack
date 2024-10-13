ROLE_CHOICES = (
    ("admin", "admin"), ("teacher", "teacher"), ("student", "student")
)

TARGET_CHOICES = (
    ("schools", "schools"), ("domains", "domains"), 
    ("specialty", "specialty"), ("custom", "custom")
)

CUSTOM_NOTI_QUERY_CHOICES = (
    ("unassigned_students", "unassigned_students"), 
    ("fees", "fees"), ("announcement", "announcement")
)

NOTI_TYPE_CHOICES = (
    ("time", "time"), ("fees", "fees"), ("announcement", "announcement"), ("results", "results")
)

COMPLAIN_TYPE_CHOICES = (
    ("request", "request"), ("complain", "complain")
)
