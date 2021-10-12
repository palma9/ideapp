from graphene_django.types import DjangoObjectType
from ideas.models import Idea

from users.types import UserType  # Necesary to show user fields on query response 

class IdeaType(DjangoObjectType):
    class Meta:
        model = Idea
        fields = ('id', 'content', 'date_created', 'user', 'visibility')