from django.urls import include, path
from accounts import views

urlpatterns = [
    # See https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.views
    #  TODO (medium priority): Namespace all django.contrib.auth.urls if possible
    path('', include('django.contrib.auth.urls')), # TODO (medium priority): Implement the templates for this
    path('register/', views.register_page),
    path('create-account/', views.create_account),
]