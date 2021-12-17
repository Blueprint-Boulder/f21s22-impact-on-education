from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("user_type", "username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user: CustomUser = super().save(commit=False)
        if commit:
            user.save()  # User has to be saved before giving a group to it
            # The two lines below add the user to the group selected in the form (e.g. applicant, volunteer)
            user_type_group: Group = Group.objects.get(name=user.user_type)
            user.groups.add(user_type_group)
            if user.user_type == "site-admin":
                # Gives the user access to Django's admin site. This line needs to be here because it's seemingly
                #  not covered by the site-admin group having superuser permissions.
                user.is_staff = True
            user.save()
        return user
