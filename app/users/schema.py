import graphene
from graphql_auth import mutations as AuthMutations
from graphql_jwt.decorators import login_required

from users.models import CustomUser, FollowRequest
from users.mutations import AcceptFollower, DenyFollower, Follow, Unfollow, removeFollower
from users.types import FollowerType, UserType


class Query(graphene.ObjectType):
    follow_requests = graphene.List(FollowerType)
    following = graphene.List(UserType)
    followers = graphene.List(UserType)
    users = graphene.List(UserType, username=graphene.String(required=False))

    @login_required
    def resolve_follow_requests(self, info):
        """ Return a list of pending logged user follow requests """
        user = info.context.user
        return FollowRequest.objects.filter(following=user.id, pending=True).order_by("-request_date")

    @login_required
    def resolve_following(self, info):
        """ Return a list of users followed by logged user """
        user = info.context.user
        follow_request = FollowRequest.objects.filter(follower=user.id, pending=False)
        return [follow.following for follow in follow_request]

    @login_required
    def resolve_followers(self, info):
        """ Return a list of logged user followers """
        user = info.context.user
        follow_request = FollowRequest.objects.filter(following=user.id, pending=False)
        return [follow.follower for follow in follow_request]

    @login_required
    def resolve_users(self, info, **kwargs):
        """ Return a list of users filtered by usernames """
        user = info.context.user  # I dont want to search myself
        username = kwargs.get('username', "")
        return CustomUser.objects.filter(username__contains=username).exclude(username=user.username)

class Mutation(graphene.ObjectType):
    register = AuthMutations.Register.Field()
    login = AuthMutations.ObtainJSONWebToken.Field()
    password_reset_email = AuthMutations.SendPasswordResetEmail.Field()
    restore_password = AuthMutations.PasswordReset.Field()
    change_password = AuthMutations.PasswordChange.Field()
    verify_token = AuthMutations.VerifyToken.Field()
    refresh_token = AuthMutations.RefreshToken.Field()
    revoke_token = AuthMutations.RevokeToken.Field()

    follow = Follow.Field()
    accept_follower = AcceptFollower.Field()
    deny_follower = DenyFollower.Field()
    unfollow = Unfollow.Field()
    remove_follower = removeFollower.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)