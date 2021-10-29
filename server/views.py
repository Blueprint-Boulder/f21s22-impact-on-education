from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
# Bugfix from https://stackoverflow.com/questions/39316948/typeerror-login-takes-1-positional-argument-but-2-were-given
from django.contrib.auth import login as auth_login


def home(request):
    return render(request, "accountAccess.html")


def account_access(request):
    return render(request, "accountAccess.html")


def csv_line(*args):
    output = ""
    for item in args:
        output += item
        output += ','
    return output[:len(output)-1]


def create_account(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    user_type = request.POST['user-type']
    # TODO: Add restrictions on creating volunteer/admin accounts
    # Used kwargs to make sure that e.g. the username field is not being assigned to password
    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password,
                                    first_name=first_name,
                                    last_name=last_name)
    group = Group.objects.get_by_natural_key(user_type)
    user.groups.add(group)
    return render(request, "accountAccess.html")


def csv_line_as_list(line):
    output = []
    to_add = ""
    for char in line:
        if char == ',':
            output.append(to_add)
            to_add = ""
        elif char != '\n':  # without this check, it would add \n to every line except the last
            to_add += char
    if to_add != "":
        output.append(to_add)
    return output


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user_type = request.POST['user-type']
    # TODO: If possible, check group membership in authenticate function instead
    user = authenticate(request, username=username, password=password)
    is_user_type = user.groups.filter(name=user_type).exists()
    if user is not None and is_user_type:
        auth_login(request, user)
        return render(request, "loginSuccess.html")
    else:
        return render(request, "loginFail.html")
