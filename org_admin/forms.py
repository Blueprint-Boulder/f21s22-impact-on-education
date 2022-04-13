from django import forms

import accounts.forms
from accounts.models import CustomUser


class CustomUserCreationForm(accounts.forms.CustomUserCreationForm):
    """The form used for Impact on Education admins to create a CustomUser."""

    account_type = forms.ChoiceField(choices=(
        (CustomUser.AccountTypes.ORG_ADMIN, "Org Admin"),))
