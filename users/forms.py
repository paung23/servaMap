from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "user_phone")


class UserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "user_phone")


class LoginForm(ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ["user_phone", "password"]


class PasswordForm(forms.Form):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password Confirm", widget=forms.PasswordInput())

    class Meta:
        fields = ["password1", "password2"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
