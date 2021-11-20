from django.urls import path

from administrator import views

app_name = 'administrator'  # Not "admin" because that conflicts with Django's admin page
urlpatterns = [
    path('users', views.user_info, name='users')
]