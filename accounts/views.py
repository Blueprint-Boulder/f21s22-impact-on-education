from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


def register(request):
    form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


def save_user(request):
    form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
    form.save()
    return HttpResponse("user " + request.POST['username'] + " saved")
