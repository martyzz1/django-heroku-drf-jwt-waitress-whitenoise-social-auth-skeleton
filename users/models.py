from django.db import models
from custom_user.models import AbstractEmailUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class User(AbstractEmailUser):

    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    class Meta(AbstractEmailUser.Meta):
        swappable = 'AUTH_USER_MODEL'
