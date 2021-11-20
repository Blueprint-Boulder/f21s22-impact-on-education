from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render
from django_root.views import is_in_group

# Create your views here.
from applicant.models import Application
from administrator.models import CustomUser


def is_admin(user: get_user_model()):
    return user.groups.filter(name='administrator').exists()


@user_passes_test(is_admin)
def user_info(request):
    return render(request, "administrator/userInfo.html", {'users': get_user_model().objects.all()})