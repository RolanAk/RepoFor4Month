from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(
        required=True
    )
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean(self):
       cleaned_data = super().clean()
       password = cleaned_data.get("password")
       password_confirm = cleaned_data.get("password_confirm")

       if (password and password_confirm) and (password != password_confirm):
           raise forms.ValidationError("passwords is different ")
       return cleaned_data
       

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        