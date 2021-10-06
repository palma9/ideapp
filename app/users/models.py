from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """ Custom model to manage app users """

    email = models.EmailField(blank=False, unique=True, max_length=254, verbose_name=_('email address'))

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

