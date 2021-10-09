from graphene_django.types import DjangoObjectType
from users.models import CustomUser, FollowRequest


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', "email", "username")


class FollowType(DjangoObjectType):
    class Meta:
        model = FollowRequest