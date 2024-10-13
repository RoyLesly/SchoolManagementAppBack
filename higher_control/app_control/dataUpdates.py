def updateResult(old, new):
    item = old.course.main_course.course_name
    if old.student.user.first_name:
        item = old.student.user.first_name + ", " + old.course.main_course.course_name
    details = ""
    ca = 0
    exam = 0
    resit = 0
    print(old.student.user.first_name)
    print(old.ca)
    print(old.exam)
    print(old.resit)
    if (old.ca != new["ca"]):
        ca = "CA - " + str(old.ca) + " --> " + new["ca"]
    if (old.exam != new["exam"]):
        exam = "EXAM - " + str(old.exam) + " --> " + new["exam"]
    if (old.resit != new["resit"]):
        resit = "RESIT - " + str(old.resit) + " --> " + new["resit"]
    if ca:
        details = str(ca)
    if exam:
        details = str(exam)
        if ca:
            details = str(ca) + "," + details
    if resit:
        details = str(resit)
        if ca:
            details = str(ca) + "," + details
        if exam:
            details = str(exam) + "," + details
    return {"item": item, "details": details}