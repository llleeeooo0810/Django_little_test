from django import forms
from basic_app.models import User
from django.core import validators

def check_names(value):
    if not value[0].isalpha():
        raise forms.ValidationError("PLEASE INPUT A VALID NAME!")


class signUp(forms.Form):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(0), check_names])
    last_name = forms.CharField(validators=[validators.MinLengthValidator(0), check_names])
    email = forms.EmailField(validators=[validators.EmailValidator()])
    # HIDDEN FIELD
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    # attack_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0),])
