from typing import Final

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models import QuerySet


class CustomUser(AbstractUser):
    """Represents each user on the website, instead of Django's default "User" model."""

    class AccountTypes:
        """
        The constants in this class are strings that are generally used to represent
        a user's account type (as in, whether a user is an applicant, volunteer, etc).
        For example, the account_type property of CustomUser will always be one of these values.

        As for what exactly these values represent:
        For background, users belong to a different group depending on their account type.
        The value of the APPLICANT constant refers to the name of the group that all applicants belong to.
        The value of the SITE_ADMIN constant refers to the name of the group that all site admins belong to.
        Etc.
        If you don't know what groups are, see:
        https://docs.djangoproject.com/en/3.2/topics/auth/default/#groups

        One of the reasons for doing this: It makes typos in group names less likely.
        For example, let's say you accidentally mistyped "site_admin" as "site-admin" at some point.
        Without the AccountTypes class, your IDE would likely not detect this. You would only catch
        the error when trying to, for example, log in as a site admin. With the AccountTypes
        class, your IDE should be able to detect if you mistyped CustomUser.AccountTypes.SITE_ADMIN
        as CustomUser.AccountTypes.SITE-ADMIN, and immediately underline the error. Your IDE can
        also probably autocomplete if you just type "CustomUser.AccountTypes.S", and/or display
        the list of options if you just type "CustomUser.AccountTypes.".
        """

        APPLICANT: Final[str] = "applicant"
        VOLUNTEER: Final[str] = "volunteer"

        ORG_ADMIN: Final[str] = "org_admin"
        """Refers to the admins of the Impact on Education organization"""

        SITE_ADMIN: Final[str] = "site_admin"
        """Refers to the admins of the website itself"""

        ALL: Final[tuple[str, ...]] = (APPLICANT, VOLUNTEER, ORG_ADMIN, SITE_ADMIN)

    class NoSuchAccountType(Exception):
        pass

    @property
    def account_type(self) -> str | None:
        """The user's account type. Its value will be one of the string constants in CustomUser.AccountTypes."""
        if not self.in_database():
            raise CustomUser.DoesNotExist("User must be saved to the database before its account_type can be accessed.")
        try:
            account_type: str = self.groups.get().name
        except Group.DoesNotExist:
            return None
        except Group.MultipleObjectsReturned:
            raise CustomUser.MultipleObjectsReturned(
                """User has multiple groups, but should only have one. The one group would 
                indicate the user's account type (applicant, volunteer, org_admin, or site_admin)"""
            )
        for possible_account_type in CustomUser.AccountTypes.ALL:
            if account_type == possible_account_type:
                return account_type

    @account_type.setter
    def account_type(self, new_account_type: str) -> None:
        """Sets the user's account_type to new_account_type, adds the user to the
         group corresponding to new_account_type, and saves the user. Raises an InvalidAccountType
         exception if new_account_type is not a value in CustomUser.AccountTypes."""

        if new_account_type not in self.AccountTypes.ALL:
            raise self.NoSuchAccountType(
                f"""You tried to set account_type to an invalid value (\"{new_account_type}\").
                The only valid values are the string constants in CustomUser.AccountTypes.
                """
            )

        # This saves the user if it's not already in the database, because a model must be saved to the database
        #  before a group can be added to it.
        # TODO (low priority): If possible, refactor so that the model doesn't have to be saved here
        if not self.in_database():
            self.save()

        if new_account_type == CustomUser.AccountTypes.SITE_ADMIN:
            # This line needs to be here because even though the site_admin group
            #  should already have superuser permissions, is_staff is seemingly
            #  not given as part of those permissions.
            self.is_staff = True
        if self.account_type is None:
            new_account_type_group = Group.objects.get(name=new_account_type)
            self.groups.add(new_account_type_group)
        else:
            del self.account_type
            self.account_type = new_account_type
        self.save()

    @account_type.deleter
    def account_type(self) -> None:
        account_type_group = Group.objects.get(name=self.account_type)
        self.groups.remove(account_type_group)

    def in_database(self):
        try:
            CustomUser.objects.get(pk=self.pk)
            return True
        except CustomUser.DoesNotExist:
            return False
