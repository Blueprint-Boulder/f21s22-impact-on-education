from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from accounts import views

app_name = "accounts"
urlpatterns = [
    # Most URLs here are copied from the URLs in django.contrib.auth.urls
    #  (see https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.views).
    #  The URLs 'register/' and 'save_user/' are not copied from there.

    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='login'),

    # Doesn't use a template.
    # After logging out, sends the user to the URL specified by LOGOUT_REDIRECT_URL in django_root/settings.py
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password-change/',
         PasswordChangeView.as_view(
             template_name="accounts/password_change_form.html",
             success_url=reverse_lazy('accounts:password-change-done')
         ),
         name='password-change'),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(
             template_name="accounts/password_change_done.html"
         ),
         name='password-change-done'),

    path('register/', views.register, name="register"),
    path('save-user/', views.save_user, name="save-user"),

    # TODO (low priority): Move the homepage-redirect URL from django_root to here (along with its view)
]