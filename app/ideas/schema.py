from django.db.models.query_utils import Q
import graphene
from graphql_jwt.decorators import login_required
from users.models import CustomUser
from users.types import UserType

from ideas.mutations import createIdea, updateIdeaVisibility, deleteIdea
from ideas.types import IdeaType
from ideas.models import Idea

class Query(graphene.ObjectType):
    my_ideas = graphene.List(IdeaType)
    user_ideas = graphene.List(IdeaType, user_id=graphene.Int(required=True))
    ideas_timeline = graphene.List(IdeaType)

    @login_required
    def resolve_my_ideas(self, info):
        """ Return a list of my ideas """
        my_user = info.context.user
        return Idea.objects.filter(user__id=my_user.id).order_by('-date_created')

    def resolve_user_ideas(self, info, user_id):
        """ Return a list of ideas from an user """
        my_user = info.context.user
        target_user = CustomUser.objects.get(id=user_id)
        private_ideas = Idea.VisibilityChoices.private.value
        if my_user.id and user_id == my_user.id:  # Show all my ideas
            filter = Q(user_id = my_user.id)
        elif my_user.id and target_user in my_user.my_following:  # I'm following him, so show public and protected ones
            filter = Q(user_id = user_id) & ~Q(visibility=private_ideas)
        else:  # People I'm not following. Only can see public ideas
            filter = Q(user_id = user_id) & Q(visibility=Idea.VisibilityChoices.public.value)
        return Idea.objects.filter(filter).order_by('-date_created')

    @login_required
    def resolve_ideas_timeline(self, info):
        """ Return a timeline of ideas from users I'm following and mine """
        my_user = info.context.user
        my_following = my_user.my_following
        private_ideas = Idea.VisibilityChoices.private.value
        return Idea.objects.filter(Q(user=my_user) | Q(user__in=my_following) & ~Q(visibility=private_ideas)).order_by('date_created')


class Mutation(graphene.ObjectType):
    create_idea = createIdea.Field()
    update_idea_visibility = updateIdeaVisibility.Field()
    delete_idea = deleteIdea.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)