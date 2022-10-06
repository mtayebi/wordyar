from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, UserManager


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
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_("creat_time"))
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
    

class MyUserManager(UserManager):
    def create_user(self, username: str, email: str, password:str, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)
    def create_superuser(self, username: str, email: str, password:str, **extra_fields):
        return super().create_superuser(username, email, password, **extra_fields)

class BaseUser(AbstractUser):
    phone = models.CharField(max_length=11, default=None, null=True,verbose_name=_("phone"))


    objects = MyUserManager()
