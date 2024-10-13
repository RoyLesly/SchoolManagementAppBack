DARK_MODE_CHOICES = (
    ("light", "light"), ("dark", "dark"), ("system", "system")
)


SEMESTER_CHOICES = (
    ("I", "I"), ("II", "II"),
)

COURSE_TYPE_CHOICES = (
    ("Fundamental", "Fundamental"), ("Transversal", "Transversal"), ("Professional", "Professional"),
)

DEPT_CHOICES = (
    ("Administration", "Administration"), ("Student", "Student"), ("Lecturer", "Lecturer"), ("Accounting", "Accounting"),
)

ROLE_CHOICES = (
    ("superadmin", "superadmin"), ("admin", "admin"), ("teacher", "teacher"), ("student", "student"), ("data entry", "data entry"),
)

TITLE_CHOICES = (
    ("Prof", "Prof"), ("Mr", "Mr"), ("Mrs", "Mrs"), ("Engr", "Engr"), ("Dr", "Dr"), ("Miss", "Miss"),
)

LANG_CHOICES = (
    ("en", "En"), ("fr", "Fr"), ("de", "De"), ("es", "Es"),
)


SESSION_CHOICES = (
    ("Morning", "Morning"), ("Evening", "Evening"),
)

LEVEL_CHOICES = (
    ("100", "100"), ("200", "200"), ("300", "300"), ("400", "400"), ("500", "500"),
)

PROGRAM_CHOICES = (
    ("HND", "HND"), ("BTS", "BTS"), ("AQP", "AQP"), ("BSC", "BSC"), ("LICENSE", "LICENSE"), ("MASTERS", "MASTERS"), ("DPQ", "DPQ"), ("OND", "OND")
)

PAGE_CHOICES = (
    ("DE", "DE"), ("Accounting", "Accounting")
)

OPERATOR = (
    ("MTN", "MTN"), ("ORANGE", "ORANGE")
)

REASON = (
    ("Registration", "Registration"), ("Tuition", "Tuition"), 
)

GENDER = (
    ("Male", "Male"), ("Female", "Female")
    )
    
AUDIENCE = (
    ("student", "student"), ("teacher", "teacher"), ("all", "all"),
    )
    
NOTIFICATION = (
    ("CA", "CA"), ("EXAM", "EXAM"), ("RESIT", "RESIT"), ("TIME TABLE", "TIME TABLE"),  ("ANNOUNCEMENT", "ANNOUNCEMENT"), 
    )

PREINSCRIPTION_STATUS = (
    ("PENDING", "PENDING"), ("ADMITTED", "ADMITTED")
    )

PREINSCRIPTION_ACTION = (
    ("CREATING", "CREATING"), ("UPDATING", "UPDATING"), ("VERIFICATION", "VERIFICATION"), ("ADMISSION", "ADMISSION")
    )
