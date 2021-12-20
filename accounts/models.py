from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


# This is the class that will represent each user on the website, instead of Django's default User model
from django.utils.crypto import constant_time_compare


class CustomUser(AbstractUser):

    class AccountTypes:
        """
        Each variable in the AccountTypes class corresponds to an account type:
        applicant, volunteer, admin, or site admin. The variable represents the name of the account type's group.
        This exists so that typos in group names become compile-time errors instead of
        runtime errors. For example, without AccountTypes, you would check if a user is a site admin like so:
            user.get_account_type() == "site-admin"
        If "site-admin" was mistyped as, say, "site_admin", this could only be caught at runtime, so it would be a pain
        to debug. This is how you would check if a user is a site admin, with AccountTypes:
            user.get_account_type() == CustomUser.AccountTypes.SITE_ADMIN
        If this was mistyped as, say, "SITE-ADMIN", it would be caught at compile time, and IDEs would catch the error.

        AccountTypes doesn't inherit from Enum because then, to get the strings, you would have to do:
           CustomUser.AccountTypes.APPLICANT.value
        which would be kind of ridiculous.
        """
        APPLICANT: str = "applicant"
        VOLUNTEER: str = "volunteer"
        ADMINISTRATOR: str = "administrator"
        SITE_ADMIN: str = "site-admin"
        ALL: tuple[str, ...] = (APPLICANT, VOLUNTEER, ADMINISTRATOR, SITE_ADMIN)

    def get_account_type(self) -> str | None:
        # TODO (medium priority): Handle edge cases (no groups, multiple groups, etc)
        result = self.groups.get().name
        valid = False
        for account_type in CustomUser.AccountTypes.ALL:
            if constant_time_compare(result, account_type):
                valid = True
        if valid:
            return result
        else:
            return None
