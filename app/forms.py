from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Нікнейм', max_length=150)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'password1', 'password2')