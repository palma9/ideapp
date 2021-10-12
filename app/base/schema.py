import graphene
from users.schema import schema as UserSchema
from ideas.schema import schema as ideaSchema


class Query(ideaSchema.Query, UserSchema.Query, graphene.ObjectType):
    pass


class Mutation(ideaSchema.Mutation, UserSchema.Mutation, graphene.ObjectType):
    pass


class Subscription(ideaSchema.Subscription, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
