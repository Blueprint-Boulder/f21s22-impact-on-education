from typing import Final

from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models import QuerySet


class CustomUser(AbstractUser):
    """Represents each user on the website, instead of Django's default "User" model.
    CustomUser inherits from AbstractUser, so it has all the functionality of the default User model,
    plus some extra."""

    account_type = models.CharField(max_length=20)

    class AccountTypes:
        """
        The constants in this class are strings that are generally used to represent
        a user's account type (as in, whether a user is an base_applicant, volunteer, etc).
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

        STUDENT: Final[str] = "student"

        VOLUNTEER: Final[str] = "volunteer"

        ORG_ADMIN: Final[str] = "org_admin"
        """Refers to the admins of the Impact on Education organization"""

        SITE_ADMIN: Final[str] = "site_admin"
        """Refers to the admins of the website itself"""

        ALL: Final[tuple[str, ...]] = (STUDENT, VOLUNTEER, ORG_ADMIN, SITE_ADMIN)

    class NoSuchAccountType(Exception):
        pass

    def in_database(self):
        # TODO (low priority): Make this cleaner somehow? This feels a little sketchy because self.pk could be None.
        return CustomUser.objects.filter(pk=self.pk).exists()

    def save(self, *args, **kwargs):
        if (self.account_type not in self.AccountTypes.ALL) and (self.account_type != ""):
            raise CustomUser.NoSuchAccountType(
                f"""self.account_type ("{self.account_type}") is not set to a valid value.
                It should be in CustomUser.AccountTypes.ALL, or be an empty string.""")

        found_old_account_type = False
        old_account_type_group = None
        # TODO (low priority): Make this more readable
        if self.in_database():
            for possible_account_type in self.AccountTypes.ALL:
                if self.groups.filter(name=possible_account_type).exists() and not found_old_account_type:
                    found_old_account_type = True
                    old_account_type_group = self.groups.get(name=possible_account_type)
                elif self.groups.filter(name=possible_account_type).exists():
                    raise CustomUser.MultipleObjectsReturned(
                        "User appears to have multiple account types. A user can only have one account type.")

        super().save(*args, **kwargs)

        if found_old_account_type:
            self.groups.remove(old_account_type_group)
        if self.account_type != "":
            new_account_type_group = Group.objects.get(name=self.account_type)
            self.groups.add(new_account_type_group)

        if self.account_type == self.AccountTypes.SITE_ADMIN:
            # This line needs to be here because is_staff is seemingly not given to the site admin group,
            #  even though the group was granted all permissions
            self.is_staff = True

        super().save(*args, **kwargs)

