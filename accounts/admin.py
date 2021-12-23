from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """This class determines how CustomUsers are handled in the official Django admin site."""

    # Fields that are displayed when viewing each CustomUser as a list
    list_display = ['username', 'email', 'last_name', 'first_name']


admin.site.register(CustomUser, CustomUserAdmin)
