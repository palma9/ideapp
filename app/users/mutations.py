import graphene
from graphql_jwt.decorators import login_required

from users.models import CustomUser, FollowRequest
from users.types import FollowType


class Follow(graphene.Mutation):
    """ The logged user send a Follow request to another """
    class Arguments:
        user_id = graphene.Int(required=True)
    
    follow = graphene.Field(FollowType)
    
    @login_required
    def mutate(self, info, user_id):
        my_user = info.context.user

        if my_user.id == user_id:
            raise Exception("You can't follow yourself")

        user_to_follow = CustomUser.objects.get(id=user_id)
        follow_request = FollowRequest(follower=my_user,following=user_to_follow)
        follow_request.save()

        return Follow(follow=follow_request)


class AcceptFollower(graphene.Mutation):
    """ The logged user can accept a received follow request """
    class Arguments:
        user_id = graphene.Int(required=True)
    
    follower = graphene.Field(FollowType)

    @login_required
    def mutate(self, info, user_id):
        my_user = info.context.user

        follower = FollowRequest.objects.get(follower_id=user_id, following_id=my_user.id, pending=True)
        follower.pending = False
        follower.save()

        return AcceptFollower(follower=follower)
