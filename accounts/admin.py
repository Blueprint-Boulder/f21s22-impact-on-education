from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Determines how CustomUsers are handled in the Django's auto-generated admin site."""

    # Fields that are displayed when viewing a list of CustomUsers
    list_display = ['username', 'account_type', 'email', 'last_name', 'first_name']

    # TODO (medium priority): Make the detail view (the view when you click on a user in the admin site)
    #  display account_type


admin.site.register(CustomUser, CustomUserAdmin)
