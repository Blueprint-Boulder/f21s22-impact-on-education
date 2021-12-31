from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


def register(request):
    """View of the 'create account' page that the user sees."""
    form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


# TODO (medium priority): Deny access if URL is directly entered; only allow
#  this to be run if it's called from another function. Not sure how to do this.
def save_user(request):
    """Saves the user into the database. Called after account info
    is submitted in the 'create account' page (templates/registration/register.html)."""

    form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
    form.save()

    return HttpResponse("user " + request.POST['username'] + " saved")  # TODO (high priority): Make into full page
