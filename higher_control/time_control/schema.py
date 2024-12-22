import graphene
from graphene_django.types import DjangoObjectType
from .models import TimeTableWeek, TimeTableDay, TimeSlot
from higher_control.user_control.models import CustomUser
from higher_control.app_control.models import Specialty, Course

# TimeTableWeek Type
class TimeTableWeekType(DjangoObjectType):
    class Meta:
        model = TimeTableWeek
        fields = (
            "id",
            "year_week",
            "specialty",
            "publish",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )

# TimeTableDay Type
class TimeTableDayType(DjangoObjectType):
    class Meta:
        model = TimeTableDay
        fields = (
            "id",
            "timetableweek",
            "date",
            "day",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )

# TimeSlot Type
class TimeSlotType(DjangoObjectType):
    class Meta:
        model = TimeSlot
        fields = (
            "id",
            "course",
            "timetableday",
            "title",
            "start",
            "end",
            "status",
            "action",
            "start_time",
            "end_time",
            "duration",
            "hours",
            "session",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )

# Query Class
class Query(graphene.ObjectType):
    all_timetable_weeks = graphene.List(TimeTableWeekType)
    all_timetable_days = graphene.List(TimeTableDayType)
    all_timeslots = graphene.List(TimeSlotType)

    timetable_weeks_count = graphene.Int()
    timetable_days_count = graphene.Int()
    timeslots_count = graphene.Int()

    timetable_week_by_id = graphene.Field(TimeTableWeekType, id=graphene.ID())
    timetable_day_by_id = graphene.Field(TimeTableDayType, id=graphene.ID())
    timeslot_by_id = graphene.Field(TimeSlotType, id=graphene.ID())

    # Resolvers for lists
    def resolve_all_timetable_weeks(self, info):
        return TimeTableWeek.objects.all()

    def resolve_all_timetable_days(self, info):
        return TimeTableDay.objects.all()

    def resolve_all_timeslots(self, info):
        return TimeSlot.objects.all()

    # Resolvers for counts
    def resolve_timetable_weeks_count(self, info):
        return TimeTableWeek.objects.count()

    def resolve_timetable_days_count(self, info):
        return TimeTableDay.objects.count()

    def resolve_timeslots_count(self, info):
        return TimeSlot.objects.count()

    # Resolvers for single objects by ID
    def resolve_timetable_week_by_id(self, info, id):
        return TimeTableWeek.objects.get(pk=id)

    def resolve_timetable_day_by_id(self, info, id):
        return TimeTableDay.objects.get(pk=id)

    def resolve_timeslot_by_id(self, info, id):
        return TimeSlot.objects.get(pk=id)



# Mutations for TimeTableWeek
class CreateTimeTableWeek(graphene.Mutation):
    class Arguments:
        year_week = graphene.String(required=True)
        specialty_id = graphene.ID(required=True)
        created_by_id = graphene.ID(required=True)

    timetable_week = graphene.Field(TimeTableWeekType)

    def mutate(self, info, year_week, specialty_id, created_by_id):
        specialty = Specialty.objects.get(id=specialty_id)
        created_by = CustomUser.objects.get(id=created_by_id)
        timetable_week = TimeTableWeek(year_week=year_week, specialty=specialty, created_by=created_by)
        timetable_week.save()
        return CreateTimeTableWeek(timetable_week=timetable_week)

# Mutations for TimeTableDay
class CreateTimeTableDay(graphene.Mutation):
    class Arguments:
        timetableweek_id = graphene.ID(required=True)
        date = graphene.Date(required=True)
        day = graphene.String(required=True)
        created_by_id = graphene.ID(required=True)

    timetable_day = graphene.Field(TimeTableDayType)

    def mutate(self, info, timetableweek_id, date, day, created_by_id):
        timetableweek = TimeTableWeek.objects.get(id=timetableweek_id)
        created_by = CustomUser.objects.get(id=created_by_id)
        timetable_day = TimeTableDay(timetableweek=timetableweek, date=date, day=day, created_by=created_by)
        timetable_day.save()
        return CreateTimeTableDay(timetable_day=timetable_day)

# Mutations for TimeSlot
class CreateTimeSlot(graphene.Mutation):
    class Arguments:
        timetableday_id = graphene.ID(required=True)
        course_id = graphene.ID(required=True)
        title = graphene.String(required=True)
        start = graphene.DateTime()
        end = graphene.DateTime()
        created_by_id = graphene.ID(required=True)

    timeslot = graphene.Field(TimeSlotType)

    def mutate(self, info, timetableday_id, course_id, title, start, end, created_by_id):
        timetableday = TimeTableDay.objects.get(id=timetableday_id)
        course = Course.objects.get(id=course_id)
        created_by = CustomUser.objects.get(id=created_by_id)
        timeslot = TimeSlot(
            timetableday=timetableday,
            course=course,
            title=title,
            start=start,
            end=end,
            created_by=created_by
        )
        timeslot.save()
        return CreateTimeSlot(timeslot=timeslot)

# Root Mutation
class Mutation(graphene.ObjectType):
    create_timetable_week = CreateTimeTableWeek.Field()
    create_timetable_day = CreateTimeTableDay.Field()
    create_time_slot = CreateTimeSlot.Field()

# Schema Definition
schema = graphene.Schema(query=Query, mutation=Mutation)
