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


# Redirects the user to their appropriate homepage depending on
# whether they're an applicant, volunteer, administrator, or site admin
def homepage_redirect(request):
    # request.user is a CustomUser. It theoretically could be an AnonymousUser if the user is not logged in, but
    #  this view is called right after the user logs in, so it should always be a CustomUser.

    # This assertion is needed for IDEs to recognize that request.user is a CustomUser. It gives a runtime error if
    #  request.user is not a CustomUser.
    assert isinstance(request.user, CustomUser), "homepage_redirect() was called while the user was not logged in"

    def do_if_applicant():
        return redirect(reverse("applicant:index"))

    def do_if_volunteer():
        # TODO (high priority): Make volunteer app
        return HttpResponse("<h1>Volunteer section has not been created yet.</h1>")

    def do_if_admin():
        # TODO (high priority): Make rest of administrator app
        # TODO (medium priority): Redirect to administrator:home instead once that's created
        return redirect(reverse("administrator:users"))

    def do_if_site_admin():
        return redirect(reverse("admin:index"))

    cases = {
        CustomUser.AccountTypes.APPLICANT: do_if_applicant,
        CustomUser.AccountTypes.VOLUNTEER: do_if_volunteer,
        CustomUser.AccountTypes.ADMINISTRATOR: do_if_admin,
        CustomUser.AccountTypes.SITE_ADMIN: do_if_site_admin,
    }

    return cases[request.user.get_account_type()]()
