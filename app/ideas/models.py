from django.db import models
from ideas.defines import VISIBILITY_CHOICES


class Idea(models.Model):
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
        choices=VISIBILITY_CHOICES,
        max_length=9
    )
