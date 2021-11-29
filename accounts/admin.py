from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


# This determines how CustomUsers are displayed in the official Django admin site
class CustomUserAdmin(UserAdmin):
    list_display = list(CustomUser.fields_to_display)


admin.site.register(CustomUser, CustomUserAdmin)
