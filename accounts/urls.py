from django.urls import include, path
from accounts import views

urlpatterns = [
    #  TODO (medium priority): Namespace all django.contrib.auth.urls if possible
    # See https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.views
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register_page),
    path('create-account/', views.create_account),
]