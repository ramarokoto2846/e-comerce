from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import NumberInput

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Mot de passe",
        strip = False,
        widget = forms.PasswordInput(attrs={'autocomplete':'new-password'})
    )

    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")