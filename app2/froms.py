from django import forms
from django.core import validators

def check_size(value):
    if len(value)<6:
        raise forms.ValidationError("the password is too short")

class SingUp(forms.Form):
    first_name=forms.CharField(initial='First Name')
    last_name=forms.CharField()
    email=forms.EmailField(help_text='write your email')
    Address=forms.CharField(required=False,)
    Technology=forms.CharField(initial='Django',disabled=True,)
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput,validators=[check_size,])
    re_password=forms.CharField(widget=forms.PasswordInput,required=False)

