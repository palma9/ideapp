from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """ Custom model to manage app users """

    email = models.EmailField(
        blank=False,
        unique=True,
        max_length=254,
        verbose_name=_('email address')
    )
    
    follows = models.ManyToManyField(
        to="users.CustomUser",
        related_name="follow",
        symmetrical=False,
        through="FollowRequest"
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'


    @property
    def my_following(self):
        accepted_requests = self.following.filter(pending=False)
        return [request.following for request in accepted_requests]
    
    @property
    def my_followers(self):
        accepted_requests = self.followers.filter(pending=False)
        return [request.follower for request in accepted_requests]


class FollowRequest(models.Model):
    follower = models.ForeignKey(CustomUser, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name="followers", on_delete=models.CASCADE)
    pending = models.BooleanField(default=True)
    request_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following',)
