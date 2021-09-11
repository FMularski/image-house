from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from . import models


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(label='Password', 
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control hover-scale'}))
    password2 = forms.CharField(label='Confirm password', 
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control hover-scale'}))

    class Meta:
        model = get_user_model()
        fields = 'username', 'first_name', 'last_name', 'email'

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control hover-scale'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control hover-scale'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control hover-scale'}),
            'email': forms.EmailInput(attrs={'class': 'form-control hover-scale'}),
        }


class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=255, 
        widget=forms.TextInput(attrs={'class': 'form-control hover-scale'}))
    password = forms.CharField(max_length=255, 
        widget=forms.PasswordInput(attrs={'class': 'form-control hover-scale'}))


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = 'img', 'title', 'category'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }