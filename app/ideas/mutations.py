import graphene

from ideas.inputs import IdeaInput
from ideas.models import Idea
from ideas.types import IdeaType
from users.models import CustomUser


class createIdea(graphene.Mutation):
    class Arguments:
        input = IdeaInput(required=True)
    
    idea = graphene.Field(IdeaType)
    
    def mutate(self, info, input):
        user = info.context.user

        idea = Idea(
            content=input.content,
            user=CustomUser.objects.get(id=user.id),
            visibility=Idea.VisibilityChoices(input.visibility)
        )

        idea.save()

        return createIdea(idea=idea)
