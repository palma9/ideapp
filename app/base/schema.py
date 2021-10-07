import graphene
from users.schema import schema as UserSchema


class Query(graphene.ObjectType):
    pass


class Mutation(UserSchema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation)
