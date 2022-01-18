from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """The visual form used to create a CustomUser. One of these is passed into the account registration page
    (templates/registration/register.html). It creates the fields (e.g. username, password), displays them, and
    saves them to the database when the form is submitted."""

    account_type = forms.ChoiceField(choices=((CustomUser.AccountTypes.STUDENT, "Student"),
                                              (CustomUser.AccountTypes.VOLUNTEER, "Volunteer"),
                                              (CustomUser.AccountTypes.ORG_ADMIN, "Org Admin"),
                                              (CustomUser.AccountTypes.SITE_ADMIN, "Site Admin")))

    class Meta:
        model = CustomUser
        fields = ("account_type", "username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user: CustomUser = super().save(commit=False)
        if commit:
            user.save()
            user.account_type = self.cleaned_data["account_type"]
            user.save()
        return user
