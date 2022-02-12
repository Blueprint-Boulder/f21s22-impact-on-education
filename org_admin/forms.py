from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


class AdminCustomUserCreationForm(CustomUserCreationForm):
    """The visual form used to create a CustomUser. One of these is passed into the account registration page
    (templates/registration/register.html). It creates the fields (e.g. username, password), displays them, and
    saves them to the database when the form is submitted."""

    account_type = forms.ChoiceField(choices=((CustomUser.AccountTypes.VOLUNTEER, "Volunteer"),
                                              (CustomUser.AccountTypes.ORG_ADMIN, "Org Admin")))
