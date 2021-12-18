from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.models import CustomUser


def index(request):
    if request.user.is_authenticated:
        return homepage_redirect(request)
    else:
        return redirect(reverse("accounts:login"))


# Helper function of homepage_redirect
def is_in_group(user: User, group: str) -> bool:
    return user.groups.filter(name=group).exists()


# Redirects the user to their appropriate homepage depending on
# whether they're an applicant, volunteer, administrator, or site admin
def homepage_redirect(request):
    # request.user is a CustomUser. It theoretically could be an AnonymousUser if the user is not logged in, but
    #  this view is called right after the user logs in, so it should always be a CustomUser.

    if is_in_group(request.user, "applicant"):
        return redirect(reverse("applicant:home"))
    # TODO (high priority): Make volunteer app
    elif is_in_group(request.user, "volunteer"):
        return HttpResponse("<h1>Volunteer section has not been created yet.</h1>")
    # TODO (high priority): Make rest of administrator app
    elif is_in_group(request.user, "administrator"):
        # TODO (medium priority): Redirect to administrator:home instead once that's created
        return redirect(reverse("administrator:users"))
    elif is_in_group(request.user, "site-admin"):
        # TODO (low priority): Replace string with call to reverse() once /admin is namespaced
        return redirect("/admin")
    else:
        # TODO (low priority): Redirect to error page
        return HttpResponse("<h1>Your user type is not set.</h1>")
