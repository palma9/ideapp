from django.db import models

class Idea(models.Model):

    class VisibilityChoices(models.TextChoices):
        public = 'public'
        protected = 'protected'
        private = 'private'

    content = models.CharField(
        verbose_name="content",
        max_length=280
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        verbose_name="user",
        to="users.customUser",
        on_delete=models.CASCADE
    )

    visibility = models.CharField(
        verbose_name="visibility",
        choices=VisibilityChoices.choices,
        default=VisibilityChoices.public,
        max_length=9
    )
