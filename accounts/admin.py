from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Determines how CustomUsers are handled in the Django's auto-generated admin site."""

    # Fields that are displayed when viewing a list of CustomUsers
    list_display = ['username', 'email', 'last_name', 'first_name']


admin.site.register(CustomUser, CustomUserAdmin)
