from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from core.models import BaseModel
from core.models import BaseUser
from django.utils.translation import gettext as _


# choices that will pply for define users profeciency 
mychoices = [("0","starter"), ("1", "intermediate"), ("2", "advanced"), ("3", "legend"),]

# Create account model according to ERD

class Account(BaseModel):
    User = models.OneToOneField(BaseUser, models.CASCADE)
    level = models.CharField(choices=mychoices, max_length=1, null=True, default=None)
    paid_user = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural, verbose_name = _("account"), _("accounts")
    