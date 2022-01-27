from django.urls import path

from org_admin import views

# org_admin refers to admins of the Impact on Education organization
#  (as opposed to site admins, i.e. the people that administer the website itself)
app_name = 'org_admin'
urlpatterns = [
    path('users', views.users, name='users'),
    path('apps', views.view_applications, name='apps'),
    path('adduser', views.view_adduser, name='adduser'),
    path('save_user/', views.save_user, name="save_user")
]
