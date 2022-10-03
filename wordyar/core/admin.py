from dataclasses import field
from django.contrib import admin
from .models import BaseUser
from django.contrib.auth.admin import UserAdmin

# Register core models in admin panel
admin.site.register(BaseUser, UserAdmin)


# @admin.register(BaseUser)
# class UserAdmin(admin.ModelAdmin):
#     fields = ['username', 'email', 'phone', 'password']
#     list_display = ('username', 'email', 'phone')
