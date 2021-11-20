from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from administrator.models import CustomUser


# This determines how CustomUsers are displayed in the official Django admin site
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = list(CustomUser.fields_to_display)


admin.site.register(CustomUser, CustomUserAdmin)
