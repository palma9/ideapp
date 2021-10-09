import graphene
from graphql_auth import mutations as AuthMutations

from users.mutations import Follow


class Query(graphene.ObjectType):
    pass


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


schema = graphene.Schema(mutation=Mutation)