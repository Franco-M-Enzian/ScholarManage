from django.contrib.auth.forms import UserCreationForm

from .models import Account


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

