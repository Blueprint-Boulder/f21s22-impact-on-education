from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.
from applicant.models import Application
from accounts.models import CustomUser


def is_admin(user: CustomUser):
    """Checks whether a user is an admin (site admins don't count)"""
    return user.get_account_type() == CustomUser.AccountTypes.ADMINISTRATOR


# Users table
@user_passes_test(is_admin)
def users(request):
    """A view that is a table of every user on the website, and relevant info about them."""
    return render(request, "administrator/users.html", {'users': get_user_model().objects.all()})
