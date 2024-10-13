import importlib
from datetime import datetime
from decimal import Decimal

now = datetime.now()

# def update_time_table_from_time_table(sender, **kwargs):
#     if not kwargs['created']:
#         module_time_table = importlib.import_module("time_control").models.TimeTable
#         created_item = kwargs['instance']
#         specialty_time_tables = module_time_table.objects.filter(specialty__id=created_item.specialty.id)
#         for tb in specialty_time_tables:
#             if not tb.id == created_item.id:
#                 tb.publish = False
#                 tb.save()

def update_course_hours_left(sender, **kwargs):
    if not kwargs['created']:
        module_course = importlib.import_module("higher_control.app_control").models.Course
        created_item = kwargs['instance']
        if created_item.action == "OUT":
            course = module_course.objects.get(id=created_item.course.id)
            course.hours_left -= Decimal(created_item.hours)
            course.save()

