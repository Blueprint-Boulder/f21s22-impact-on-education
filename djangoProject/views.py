from django.http import HttpResponse
from django.shortcuts import render
import bcrypt


def home(request):
    html="<a href=get_data><h1>go</h1></a>"
    return HttpResponse(html)


def get_data(request):
    return render(request, "accountAccess.html")


def csv_line(*args):
    output = ""
    for item in args:
        output += item
        output += ','
    return output[:len(output)-1]


def create_account(request):
    user_type = request.POST['user-type']
    username = request.POST['username']
    password = request.POST['password']
    # bcrypt.hashpw returns bytes, so its result must be decoded to be stored as a string in the .csv
    # similarly, bcrypt.hashpw's arguments must be bytes, so the password string must be encoded
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
    login_data = open("login_data.csv", "a")
    login_data.write(csv_line(user_type, username, hashed_password))
    login_data.write('\n')
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
    user_type = request.POST['user-type']
    username = request.POST['username']
    password = request.POST['password']
    login_data = open("login_data.csv", "r")
    login_data_lines = login_data.readlines()
    del login_data_lines[0]  # removes the header (which is literally the string "user_type, username, hashed_password")
    login_data_as_2d_list = []
    for line in login_data_lines:
        login_data_as_2d_list.append(csv_line_as_list(line))
    for line in login_data_as_2d_list:
        if line[0] == user_type and line[1] == username\
                and bcrypt.checkpw(password.encode('utf8'), line[2].encode('utf8')):
            return render(request, "loginSuccess.html")
    return render(request, "loginFail.html")
