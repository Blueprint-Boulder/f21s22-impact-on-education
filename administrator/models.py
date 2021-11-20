from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO (low priority): Consider moving CustomUser somewhere else (be VERY careful to refactor everything relevant
#  if you decide to do this)
# This is the class that will represent each user on the website, instead of Django's default User model
class CustomUser(AbstractUser):
    # fields_to_display isn't an official Django thing, just makes refactoring easier
    fields_to_display: tuple = ('username', 'email', 'last_name', 'first_name',)
