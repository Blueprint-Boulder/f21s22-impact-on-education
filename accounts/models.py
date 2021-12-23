from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import QuerySet
from django.core.exceptions import MultipleObjectsReturned

from django.utils.crypto import constant_time_compare


class CustomUser(AbstractUser):
    """Represents each user on the website, instead of Django's default "User" model."""
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
        """Returns the account type (applicant, volunteer, administrator, or site-admin) of a user as a string.
        Returns None if the user does not belong to any groups (meaning they don't have an account type).
        Throws a MultipleObjectsReturned exception if the user belongs to more than one group (meaning it's
        unclear what their account type is; users should not belong to multiple groups)."""
        try:
            account_type: str = self.groups.get().name
        except CustomUser.DoesNotExist:
            return None
        except CustomUser.MultipleObjectsReturned:
            raise CustomUser.MultipleObjectsReturned(
                # Just so you know, this is a multiline string, not a multiline comment
                """User has multiple groups, but should only have one. The one group would 
                indicate the user's account type (applicant, volunteer, administrator, or site-admin)"""
            )
        for possible_account_type in CustomUser.AccountTypes.ALL:
            if account_type == possible_account_type:
                return account_type

