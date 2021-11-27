from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


def register(request):
    form = CustomUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


def save_user(request):
    form = CustomUserCreationForm(request.POST)
    form.save()
    return HttpResponse("user " + request.POST['username'] + " saved")
