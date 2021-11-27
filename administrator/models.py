from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO (low priority): Consider moving the CustomUser class somewhere else, such as in accounts
#  (be VERY careful to refactor everything relevant if you decide to do this)
# This is the class that will represent each user on the website, instead of Django's default User model
class CustomUser(AbstractUser):
    user_type = models.CharField(choices=(("applicant", "Applicant"),
                                           ("volunteer", "Volunteer"),
                                           ("administrator", "Admin"),
                                           ("site-admin", "Site Admin")),
                                 max_length=13, null=True)
    # fields_to_display isn't an official Django thing, just makes refactoring easier
    fields_to_display: tuple = ('username', 'email', 'last_name', 'first_name',)
