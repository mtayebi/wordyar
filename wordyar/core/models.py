from email.policy import default
from re import M
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


"""
Create core models include Basemodel & custome User models
"""

class BaseManager(models.Manager):
    # return just not logicaly deleted users if admins want to see users
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    # admins can access to all users containing logically deleted users by this function
    def archive(self):
        return super().get_queryset()

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_time=True, verbose_name=_("creat_time"))
    update_time = models.DateTimeField(auto_now=True, verbose_name=_("update_time"))
    delete_time = models.DateTimeField(blank=True, null=True, verbose_name=_("delete_time"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("is_deleted"))

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ["-create_time"]

    def delete_user(self):
        self.is_deleted = True
        self.delete_time = timezone.now()
        self.save()
    