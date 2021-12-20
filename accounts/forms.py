from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=((CustomUser.AccountTypes.APPLICANT, "Applicant"),
                                           (CustomUser.AccountTypes.VOLUNTEER, "Volunteer"),
                                           (CustomUser.AccountTypes.ADMINISTRATOR, "Admin"),
                                           (CustomUser.AccountTypes.SITE_ADMIN, "Site Admin")))

    class Meta:
        model = CustomUser
        fields = ("user_type", "username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user: CustomUser = super().save(commit=False)
        if commit:
            user.save()  # User has to be saved before giving a group to it
            user_type: str = self.cleaned_data["user_type"]
            # Adds the user to the group selected in the form (e.g. applicant, volunteer)
            user.groups.add(Group.objects.get(name=user_type))
            if user_type == CustomUser.AccountTypes.SITE_ADMIN:
                # Gives the user access to Django's admin site. This line needs to be here because is_staff is
                #  seemingly not given as part of superuser permissions (which the site-admin group should
                #  already have).
                user.is_staff = True
            user.save()
        return user
