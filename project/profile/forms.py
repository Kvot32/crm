from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreateForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'phone', 'email']
