import graphene
from graphql_jwt.decorators import login_required

from ideas.inputs import IdeaInput
from ideas.models import Idea
from ideas.types import IdeaType
from users.models import CustomUser


class createIdea(graphene.Mutation):
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

        return createIdea(idea=idea)


class updateIdeaVisibility(graphene.Mutation):
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