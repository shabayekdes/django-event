from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'avatar']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name']
