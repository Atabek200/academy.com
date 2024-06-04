from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Request


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description']


class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['status']
