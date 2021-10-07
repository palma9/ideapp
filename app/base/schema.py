import graphene
from users.schema import schema as UserSchema
from ideas.schema import schema as ideaSchema


class Query(graphene.ObjectType):
    pass


class Mutation(ideaSchema.Mutation, UserSchema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation)
