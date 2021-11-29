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
            user.save()
            # This adds the user to the group selected in the form (e.g. applicant, volunteer)
            group: Group = Group.objects.get(name=user.user_type)
            user.groups.add(group)
            if user.user_type == "site-admin":
                user.is_staff = True  # Gives access to Django's admin site
            user.save()
        return user
