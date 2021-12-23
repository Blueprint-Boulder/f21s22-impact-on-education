from django.urls import path

from . import views

# org_admin refers to admins of the Impact on Education organization
#  (as opposed to site admins, i.e. the people that administer the website itself)
app_name = 'org_admin'
urlpatterns = [
    path('users', views.users, name='users')
]
