import graphene
from graphql_jwt.decorators import login_required

from ideas.mutations import createIdea, updateIdeaVisibility
from ideas.types import IdeaType
from ideas.models import Idea

class Query(graphene.ObjectType):
    my_ideas = graphene.List(IdeaType)

    @login_required
    def resolve_my_ideas(self, info):
        """ Return a list of my ideas """
        my_user = info.context.user
        return Idea.objects.filter(user__id=my_user.id).order_by('-date_created')

class Mutation(graphene.ObjectType):
    create_idea = createIdea.Field()
    update_idea_visibility = updateIdeaVisibility.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)