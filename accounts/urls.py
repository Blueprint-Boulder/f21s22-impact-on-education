from django.urls import include, path
from accounts import views

app_name = "accounts"
urlpatterns = [
    # See https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.views
    path('', include('django.contrib.auth.urls')),  # TODO (medium priority): Implement the templates for this
    path('register/', views.register, name="register"),
    path('save-user/', views.save_user, name="save-user"),
]
