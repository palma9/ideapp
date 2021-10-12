import graphene
from graphql_jwt.decorators import login_required
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from ideas.inputs import IdeaInput
from ideas.models import Idea
from ideas.types import IdeaType
from users.models import CustomUser


channel_layer = get_channel_layer()


class createIdea(graphene.Mutation):
    """ The user create a new idea """
    class Arguments:
        input = IdeaInput(required=True)
    
    idea = graphene.Field(IdeaType)
    
    @login_required
    def mutate(self, info, input):
        user = info.context.user

        idea = Idea(
            content=input.content,
            user=CustomUser.objects.get(id=user.id),
            visibility=Idea.VisibilityChoices(input.visibility)
        )

        idea.save()

        # Send to notifyIdea subscription
        async_to_sync(channel_layer.group_send)("new_idea", {"data": idea})

        return createIdea(idea=idea)


class updateIdeaVisibility(graphene.Mutation):
    """ Used to change the visibility of a created idea """
    class Arguments:
        id = graphene.ID(required=True)
        visibility = graphene.String(required=True)
    
    idea = graphene.Field(IdeaType)

    @login_required
    def mutate(self, info, id, visibility):
        user = info.context.user
        idea = Idea.objects.get(id=id, user__id=user.id)
        idea.visibility = Idea.VisibilityChoices(visibility)
        idea.save()

        return updateIdeaVisibility(idea=idea)        

class deleteIdea(graphene.Mutation):
    """ The user delete their created ideas """
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(self, info, id):
        user = info.context.user
        try:
            idea = Idea.objects.get(id=id, user__id=user.id)
            idea.delete()
            success = True
        except Idea.DoesNotExist:
            success = False

        return deleteIdea(success=success)