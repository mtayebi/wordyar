from dataclasses import fields
from tkinter.ttk import Widget
from django import forms
from core.models import BaseUser


class AccountForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='ایمیل', widget=forms.EmailInput(attrs={'class':'form-control', 'Lable':'ایمیل'}))
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    


