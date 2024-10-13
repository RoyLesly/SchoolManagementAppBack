from import_export import resources 
from .models import *


class TimeTableWeekResource(resources.ModelResource):
    class Meta:
        model = TimeTableWeek
        

class TimeTableDayResource(resources.ModelResource):
    class Meta:
        model = TimeTableDay
        

class TimeSlotResource(resources.ModelResource):
    class Meta:
        model = TimeSlot
        
        