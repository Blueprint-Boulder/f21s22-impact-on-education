from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.models import CustomUser


def index(request):
    """The index page for the website. If the user is logged in, redirects them to their
    homepage. Otherwise, sends the user to the login page."""
    if request.user.is_authenticated:
        return homepage_redirect(request)
    else:
        return redirect(reverse("accounts:login"))


def homepage_redirect(request):
    """Redirects the user to their appropriate homepage depending on
    whether they're an applicant, org admin, or site admin"""

    # This assertion is needed for IDEs to recognize that request.user is a CustomUser.
    #  It theoretically could be an AnonymousUser if the user is not logged in, but
    #  this view is called right after the user logs in, so it should always be a CustomUser.
    #  The assert statement gives a runtime error if request.user is not a CustomUser.
    assert isinstance(request.user, CustomUser), "homepage_redirect() was called while the user was not logged in"

    match request.user.account_type:
        case CustomUser.AccountTypes.APPLICANT:
            return redirect(reverse("applicant:home"))
        case CustomUser.AccountTypes.ORG_ADMIN:
            # TODO (high priority): Make rest of org admin app
            # TODO (medium priority): Redirect to org_admin:home instead once that's created
            return redirect(reverse("org_admin:home"))
        case CustomUser.AccountTypes.SITE_ADMIN:
            return redirect(reverse("admin:index"))
        case _:
            # TODO (low priority): Redirect to dedicated error page, and email site admins if this happens
            return HttpResponse("Your account type either is not set, or was not set to a valid value.")
