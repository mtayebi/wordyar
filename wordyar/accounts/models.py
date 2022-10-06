from email.policy import default
import imp
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from core.models import BaseModel
from core.models import BaseUser
from exams.models import Exam
from django.utils.translation import gettext as _

# Create account model according to ERD

class Account(BaseModel):
    User = models.OneToOneField(BaseUser, models.CASCADE)
    level = models.Choices(["starter", "intermediate", "advanced", "legend"])
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE)
    paid_user = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural, verbose_name = _("account"), _("accounts")
    