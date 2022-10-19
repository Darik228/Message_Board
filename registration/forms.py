from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import NewUser
from django import forms
from django.forms import PasswordInput, EmailInput


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=EmailInput)
    password1 = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)

    class Meta:
        model = NewUser
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=PasswordInput)