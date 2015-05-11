from django.db import models
from custom_user.models import AbstractEmailUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractEmailUser):

    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    # You can filter users by User.objects.filter(user_type=User.CLIENT)

    CLIENT = 'C'
    VET = 'V'
    NUTRITIONALIST = 'F'
    GROOMER = 'G'
    NURSE = 'N'

    USER_TYPES = (
        (CLIENT, _('Client')),
        (VET, _('Vet')),
        (NUTRITIONALIST, _('Nutritionalist')),
        (GROOMER, _('Groomer')),
        (NURSE, _('Nurse')),
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=30, blank=False)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, blank=False)

    def is_provider(self):
        return False if self.user_type == self.CLIENT else True

    class Meta(AbstractEmailUser.Meta):
        swappable = 'AUTH_USER_MODEL'
