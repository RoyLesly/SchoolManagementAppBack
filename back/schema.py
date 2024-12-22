import graphene
from higher_control.app_control.schema import Query as HigherAppQuery
from higher_control.chat_control.schema import Query as HigherChatQuery
from higher_control.fees_control.schema import Query as HigherFeesQuery
from higher_control.noti_control.schema import Query as HigherNotiQuery
from higher_control.time_control.schema import Query as HigherTimeQuery
from higher_control.user_control.schema import Query as HigherUserQuery

# Combine all queries into a single Query class
class Query(HigherAppQuery, HigherChatQuery, HigherFeesQuery, HigherNotiQuery, HigherTimeQuery, HigherUserQuery, graphene.ObjectType):
    pass

# Create the unified schema
schema = graphene.Schema(query=Query)