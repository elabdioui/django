from django import forms
from .models import SignUp,SignIn

class SignInForm(forms.ModelForm):
    class Meta:
        model=SignIn
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields='__all__'