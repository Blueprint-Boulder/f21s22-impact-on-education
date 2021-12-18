from django.contrib.auth.models import AbstractUser
from django.db import models


# This is the class that will represent each user on the website, instead of Django's default User model
class CustomUser(AbstractUser):
    def get_user_type(self) -> str:
        possible_user_types = ["applicant", "volunteer", "administrator", "site-admin"]
        for possible_user_type in possible_user_types:
            if self.groups.filter(name=possible_user_type).exists():
                return possible_user_type
        return None
