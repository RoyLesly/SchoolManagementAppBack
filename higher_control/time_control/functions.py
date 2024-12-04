from decimal import Decimal

def update_course_hours_left(sender, **kwargs):
    instance = kwargs['instance']
    if instance.course and instance.hours:
        if instance.action == "OUT":
            course = instance.course
            course.hours_left = max(course.hours_left - Decimal(instance.hours), Decimal(0))
            if course.hours_left < 0.75:
                course.completed = True
            course.save()
