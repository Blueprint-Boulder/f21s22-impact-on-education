from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.
from applicant.models import Application
from accounts.models import CustomUser


def is_admin(user: CustomUser):
    return user.groups.filter(name='administrator').exists()


# Users table
@user_passes_test(is_admin)
def users(request):
    return render(request, "administrator/users.html", {'users': get_user_model().objects.all()})
