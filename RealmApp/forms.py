from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=70, required=True, help_text='*')
    email = forms.CharField(max_length=150, required=True, help_text='*')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('content', 'images')


