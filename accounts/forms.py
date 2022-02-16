from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """The form used to create a CustomUser. One of these is passed into the account registration template
    (accounts/register.html). It creates the fields (e.g. username, password), displays them, and
    saves them to the database when the form is submitted."""

    class Meta:
        model = CustomUser
        fields = ("account_type", "username", "email", "first_name", "last_name", "password1", "password2")

    # TODO (medium priority): Force the email to be unique
