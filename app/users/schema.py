import graphene
from graphql_auth import mutations as AuthMutations
from graphql_jwt.decorators import login_required

from users.models import FollowRequest
from users.mutations import AcceptFollower, DenyFollower, Follow
from users.types import FollowerType, FollowingType


class Query(graphene.ObjectType):
    follow_requests = graphene.List(FollowerType)
    following = graphene.List(FollowingType)
    followers = graphene.List(FollowerType)

    @login_required
    def resolve_follow_requests(self, info):
        user = info.context.user
        return FollowRequest.objects.filter(following=user.id, pending=True).order_by("-request_date")

    @login_required
    def resolve_following(self, info):
        user = info.context.user
        return FollowRequest.objects.filter(follower=user.id, pending=False)

    @login_required
    def resolve_followers(self, info):
        user = info.context.user
        return FollowRequest.objects.filter(following=user.id, pending=False)


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
    Accept_follower = AcceptFollower.Field()
    deny_follower = DenyFollower.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)