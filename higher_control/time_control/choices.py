REASON = (
    ("TUITION", "TUITION"),
    ("REGISTRATION", "REGISTRATION"),
    ("SCHOLARSHIP", "SCHOLARSHIP"),
    ("PLATFORM CHARGES", "PLATFORM CHARGES"),
)


OPERATOR = (
    ("MTN", "MTN"), ("ORANGE", "ORANGE")
)

PAYMENT_STATUS = (
    ("Pending", "Pending"), ("Completed", "Completed")
)

PAYMENT_METHODS = (
    ("BANK", "BANK"), 
    ("MTN", "MTN"),
    ("ORANGE", "ORANGE"), 
    ("DIRECT", "DIRECT"),
)

TIMESLOT_CHOICES = (
    ("PENDING", "PENDING"), 
    ("CHECKED-IN", "CHECKED-IN"),
    ("CHECKED-OUT", "CHECKED-OUT"),
    ("NOT-CHECKED-IN", "NOT-CHECKED-IN"), 
    ("OUT-BY-SYSTEM", "OUT-BY-SYSTEM"),
)

TIMESLOT_ACTIONS = (
    ("PENDING", "PENDING"), 
    ("IN", "IN"), 
    ("OUT", "OUT"),
    ("OUT-BY-SYSTEM", "OUT-BY-SYSTEM"),
)

