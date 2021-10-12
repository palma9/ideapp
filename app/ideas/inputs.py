import graphene
from ideas.models import Idea

class IdeaInput(graphene.InputObjectType):
    content = graphene.String()
    visibility = graphene.String(default_value=Idea.VisibilityChoices.public.value)