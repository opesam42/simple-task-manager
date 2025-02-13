from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import CustomUser
from .models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'profileImage']

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))