import graphene
from graphene_django.types import DjangoObjectType
from .models import Notification, Complain, UserActivity
from higher_control.user_control.models import CustomUser

# Notification Type
class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        fields = (
            "id",
            "message",
            "target",
            "schools",
            "domains",
            "specialty",
            "custom",
            "role",
            "noti_type",
            "status",
            "ending_at",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )

# Complain Type
class ComplainType(DjangoObjectType):
    class Meta:
        model = Complain
        fields = (
            "id",
            "message",
            "complain_type",
            "status",
            "ending_at",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        )

# UserActivity Type
class UserActivityType(DjangoObjectType):
    class Meta:
        model = UserActivity
        fields = (
            "id",
            "user",
            "action",
            "item",
            "details",
            "created_at",
            "updated_at",
        )

# Query Class
class Query(graphene.ObjectType):
    all_notifications = graphene.List(NotificationType)
    all_complains = graphene.List(ComplainType)
    all_user_activities = graphene.List(UserActivityType)

    notification_by_id = graphene.Field(NotificationType, id=graphene.ID())
    complain_by_id = graphene.Field(ComplainType, id=graphene.ID())
    user_activity_by_user = graphene.List(UserActivityType, user_id=graphene.ID())

    def resolve_all_notifications(self, info):
        return Notification.objects.all()

    def resolve_all_complains(self, info):
        return Complain.objects.all()

    def resolve_all_user_activities(self, info):
        return UserActivity.objects.all()

    def resolve_notification_by_id(self, info, id):
        return Notification.objects.get(pk=id)

    def resolve_complain_by_id(self, info, id):
        return Complain.objects.get(pk=id)

    def resolve_user_activity_by_user(self, info, user_id):
        return UserActivity.objects.filter(user_id=user_id)

# Mutations
class CreateNotification(graphene.Mutation):
    class Arguments:
        message = graphene.String(required=True)
        target = graphene.String()
        custom = graphene.String()
        role = graphene.String()
        noti_type = graphene.String()
        status = graphene.Boolean()
        ending_at = graphene.Date()
        created_by_id = graphene.ID(required=True)

    notification = graphene.Field(NotificationType)

    def mutate(self, info, message, created_by_id, **kwargs):
        created_by = CustomUser.objects.get(id=created_by_id)
        notification = Notification(message=message, created_by=created_by, **kwargs)
        notification.save()
        return CreateNotification(notification=notification)

class CreateComplain(graphene.Mutation):
    class Arguments:
        message = graphene.String(required=True)
        complain_type = graphene.String()
        status = graphene.Boolean()
        ending_at = graphene.Date()
        created_by_id = graphene.ID(required=True)

    complain = graphene.Field(ComplainType)

    def mutate(self, info, message, created_by_id, **kwargs):
        created_by = CustomUser.objects.get(id=created_by_id)
        complain = Complain(message=message, created_by=created_by, **kwargs)
        complain.save()
        return CreateComplain(complain=complain)

class CreateUserActivity(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        action = graphene.String(required=True)
        item = graphene.String(required=True)
        details = graphene.String(required=True)

    user_activity = graphene.Field(UserActivityType)

    def mutate(self, info, user_id, action, item, details):
        user = CustomUser.objects.get(id=user_id)
        user_activity = UserActivity(user=user, action=action, item=item, details=details)
        user_activity.save()
        return CreateUserActivity(user_activity=user_activity)

class Mutation(graphene.ObjectType):
    create_notification = CreateNotification.Field()
    create_complain = CreateComplain.Field()
    create_user_activity = CreateUserActivity.Field()

# Schema Definition
schema = graphene.Schema(query=Query, mutation=Mutation)
