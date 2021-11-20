from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.shortcuts import render, redirect

from administrator.models import CustomUser


def register_page(request):
    return render(request, "registration/register.html")


# The template registration/register.html sends the account info here
# TODO (high priority): Instead of this function, use Django's UserCreationForm. I couldn't figure
#  the UserCreationForm out so I threw this together so that we have a registration page for testing.
#  This function should DEFINITELY not be used in production, especially considering that anyone
#  can create any type of account with this function.
def create_account(request):
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    user_type = request.POST['user-type']
    password = request.POST['password']
    # Used kwargs to make sure that e.g. the username field is not being assigned to password
    try:
        user = CustomUser.objects.create_user(username=username,
                                              email=email,
                                              first_name=first_name,
                                              last_name=last_name,
                                              password=password,
                                              is_superuser=(user_type == 'site-admin'),
                                              is_staff=(user_type == 'site-admin'))
    except IntegrityError:
        return render(request, "registration/register.html", {'fail': True})
    group = Group.objects.get_by_natural_key(user_type)
    user.groups.add(group)
    return redirect("/accounts/login/")
