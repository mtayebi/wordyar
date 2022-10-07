from argparse import Namespace
from unicodedata import name
from django.urls import path
from .views import UserRegister

app_name = "accounts"

urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
]