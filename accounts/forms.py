from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class SelectDateWidget(forms.SelectDateWidget):
    input_type = 'date'


class SignupForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "email",
            "birthday",
            "what_grade",
            "live_with_family",
        )
        widgets = {
            'birthday': SelectDateWidget(years=range(1980, 2030)),
        }

