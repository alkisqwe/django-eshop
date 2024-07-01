from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "profileimage",
            "certified",
            "type",
            "plan",
        )
        
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email Or Username',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
