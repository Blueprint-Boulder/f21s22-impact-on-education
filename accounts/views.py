from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


# This is the "create account" page that the user sees
def register(request):
    form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


# Saves the user into the database; called after the user submits their account info in register.html
def save_user(request):
    form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
    form.save()
    return HttpResponse("user " + request.POST['username'] + " saved")
