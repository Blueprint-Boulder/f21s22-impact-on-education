from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Represents each user on the website, instead of Django's default "User" model."""

    class AccountTypes:
        """
        The constants in this class are generally used to represent
        a user's account type (as in, whether a user is an applicant, volunteer, etc).
        For example, the instance method get_account_type() of CustomUser will return one of these values.

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

        APPLICANT: str = "applicant"
        VOLUNTEER: str = "volunteer"

        ORG_ADMIN: str = "org_admin"
        """Refers to the admins of the Impact on Education organization"""

        SITE_ADMIN: str = "site_admin"
        """Refers to the admins of the website itself"""

        ALL: tuple[str, ...] = (APPLICANT, VOLUNTEER, ORG_ADMIN, SITE_ADMIN)

    def get_account_type(self) -> str | None:
        """Returns the account type (applicant, volunteer, org_admin, or site_admin) of a user as a string.
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
                indicate the user's account type (applicant, volunteer, org_admin, or site_admin)"""
            )
        for possible_account_type in CustomUser.AccountTypes.ALL:
            if account_type == possible_account_type:
                return account_type
