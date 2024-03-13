from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile 


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User  
        fields = ['username', 'email', 'password1', 'password2'] 

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
        'class': 'input',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address', 
        'class': 'input',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', 
        'class': 'input',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password', 
        'class': 'input',
    })) 


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email'] 


class ProfileUpdateForm(forms.ModelForm): 
    class Meta:
        model = Profile 
        fields = ['image'] 