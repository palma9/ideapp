from graphene_django.types import DjangoObjectType
from users.models import CustomUser, FollowRequest


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', "email", "username")


class FollowerType(DjangoObjectType):
    class Meta:
        model = FollowRequest
        fields = ('id', 'follower', 'pending', 'request_date')


class FollowingType(DjangoObjectType):
    class Meta:
        model = FollowRequest
        fields = ('id', 'following', 'pending', 'request_date')