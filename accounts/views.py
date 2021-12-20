from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


def register(request):
    """The 'create account' page that the user sees."""

    form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


# Saves the user into the database; called after the user submits their account info in register.html
def save_user(request):
    """Saves request.user into the database. Called after account info
    is submitted in the 'create account' page (templates/registration/register.html)."""

    form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
    form.save()
    return HttpResponse("user " + request.POST['username'] + " saved")
