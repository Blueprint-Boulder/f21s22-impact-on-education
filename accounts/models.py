from django.contrib.auth.models import AbstractUser
from django.db import models


# This is the class that will represent each user on the website, instead of Django's default User model
class CustomUser(AbstractUser):
    user_type: models.CharField = models.CharField(choices=(("applicant", "Applicant"),
                                                            ("volunteer", "Volunteer"),
                                                            ("administrator", "Admin"),
                                                            ("site-admin", "Site Admin")),
                                                   max_length=13, null=True)

    """ Represents the fields to display when looking at a brief overview of a user.
    This isn't an official Django thing but makes refactoring easier if we end up having multiple pages that
    list brief overviews of users. Currently only used by CustomUserAdmin (which determines how users are
    displayed in Django's admin site). The fields listed here are inherited from AbstractUser (but the 
    fields_to_display variable itself is not)."""
    fields_to_display: tuple = ('username', 'email', 'last_name', 'first_name',)
