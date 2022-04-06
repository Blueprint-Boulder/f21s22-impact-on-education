from django.urls import path

from volunteer import views

app_name = 'volunteer'
urlpatterns = [
    path('', views.home, name='home')
]
