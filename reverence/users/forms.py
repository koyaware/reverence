import os

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', '<PASSWORD1>', '<PASSWORD2>')


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1 and len(password1) < 8:
            self.add_error('password1', 'Passwords must have at least 8 characters')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        return password2


class UserLoginForm(AuthenticationForm):
    class Meta(AuthenticationForm.Meta):
        model = User
        fields = ('email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name',
                  'city', 'street', 'house_number',
                  'apartment_number', 'postal_code',
        ]