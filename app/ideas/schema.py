import graphene
from ideas.mutations import createIdea

class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    create_idea = createIdea.Field()

schema = graphene.Schema(mutation=Mutation)