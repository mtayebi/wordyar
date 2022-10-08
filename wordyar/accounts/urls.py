from argparse import Namespace
from unicodedata import name
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
]