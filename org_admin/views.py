from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from base_applicant.models import Application
from accounts.models import CustomUser


def is_admin(user: CustomUser):
    """Checks whether a user is an org admin"""
    return user.account_type == CustomUser.AccountTypes.ORG_ADMIN


# Users table
@user_passes_test(is_admin)
def users(request):
    """A view that is a table of every user on the website, and relevant info about them."""
    return render(request, "org_admin/users.html", {'users': CustomUser.objects.all()})
