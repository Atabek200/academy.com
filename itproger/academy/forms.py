from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Specialization
from django import forms
from .models import Ticket
from .models import Client, Master


class MasterSignUpForm(UserCreationForm):
    contact_phone = forms.CharField(max_length=15)
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all())
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'contact_phone', 'specialization', 'photo')


class ClientSignUpForm(UserCreationForm):
    contact_phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'contact_phone', 'address')


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'master', 'status']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['address', 'contact_phone']


class MasterRegisterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['specialization', 'contact_phone', 'photo']
