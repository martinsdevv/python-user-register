from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
