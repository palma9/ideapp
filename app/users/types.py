from graphene_django.types import DjangoObjectType
from users.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', "email", "username")