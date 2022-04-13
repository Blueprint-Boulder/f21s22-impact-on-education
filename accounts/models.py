from typing import Final

from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomUser(AbstractUser):
    """Represents each user on the website, instead of Django's default "User" model.
    CustomUser inherits from AbstractUser, so it has all the functionality of the default User model,
    plus some extra."""

    class AccountTypes:
        """
        The constants in this class are strings that are generally used to represent
        a user's account type (as in, whether a user is an applicant, org admin, etc).
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

        ORG_ADMIN: Final[str] = "org_admin"
        """Refers to the admins of the organization that's hiring people"""

        SITE_ADMIN: Final[str] = "site_admin"
        """Refers to the admins of the website itself"""

        ALL: Final[tuple[str, ...]] = (APPLICANT, ORG_ADMIN, SITE_ADMIN)
        """A tuple of all possible account types that a user could be. 
        Each element is a string used to represent an account type."""

    account_type = models.CharField(max_length=20, choices=((AccountTypes.APPLICANT, "Student"),
                                                            (AccountTypes.ORG_ADMIN, "Org Admin"),
                                                            (AccountTypes.SITE_ADMIN, "Site Admin")))

    class NoSuchAccountType(Exception):
        pass

    def in_database(self):
        # TODO (low priority): Make this cleaner somehow? This feels a little sketchy because self.pk could be None.
        return CustomUser.objects.filter(pk=self.pk).exists()

    def save(self, *args, **kwargs):
        """Saves the user to the database. Adds the user to the group that corresponds to its account_type.
        Removes the user from groups that were added by an older account_type.
        """

        # 1) Raises an exception if account_type is set to an invalid value.
        #    Doesn't raise an exception if account_type is an empty string, so that Django's createsuperuser command
        #    (which only sets username, password, and email, and leaves every other string attribute as an empty string)
        #    works.
        if self.account_type and (self.account_type not in self.AccountTypes.ALL):
            raise CustomUser.NoSuchAccountType(
                f"""self.account_type ("{self.account_type}") is not set to a valid value.
                It should be in CustomUser.AccountTypes.ALL, or be an empty string.""")

        # self.AccountTypes.ALL is just CustomUser.AccountTypes.ALL, but can't be written like the latter
        #  because it would be circular (referencing the CustomUser class in the definition of the CustomUser class).
        #  It's misleading to think of self.AccountTypes.ALL as an attribute of "self".
        possible_account_types = self.AccountTypes.ALL

        # 2) Checks if the user already has an account type.
        #    If it does, sets old_account_type_group to the group corresponding to that account type.
        #    If not, sets old_account_type_group to None.
        if self.in_database():
            user_account_types = [account_type for account_type in possible_account_types
                                  if self.groups.filter(name=account_type).exists()]
            if len(user_account_types) == 0:
                old_account_type_group = None
            elif len(user_account_types) == 1:
                old_account_type_group = self.groups.get(name=user_account_types[0])
            else:
                raise CustomUser.MultipleObjectsReturned(
                    "User appears to have multiple account types. A user can only have one account type.")
        else:
            old_account_type_group = None

        # 3) Saves the user to the database.
        #    This does everything we need, except handling the group stuff for account_type.
        #    This step is necessary because in order to add or remove groups
        #    (which will be done in the following steps), the user needs to be in the database.
        super().save(*args, **kwargs)

        # 4) Fairly self-explanatory: Removes the user from their old account type group, if they have one.
        if old_account_type_group is not None:
            self.groups.remove(old_account_type_group)

        # 5) Adds the user to the group corresponding to their new account type.
        if self.account_type:
            new_account_type_group = Group.objects.get(name=self.account_type)
            self.groups.add(new_account_type_group)

        # 6) Self-explanatory. Needs to be here because is_staff is seemingly not given to the site admin group,
        #     even though the group was granted all permissions.
        if self.account_type == self.AccountTypes.SITE_ADMIN:
            self.is_staff = True

        # 7) Finally, saves the user to the database again, in order to save the changes that were made in steps 4-6.
        super().save(*args, **kwargs)
