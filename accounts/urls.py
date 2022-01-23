from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView, PasswordChangeDoneView
from django.urls import include, path, reverse_lazy
from accounts import views

app_name = "accounts"
urlpatterns = [
    # Most URLs here are copied from django.contrib.auth.urls, with minor differences.

    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='login'),

    # Doesn't use a template.
    # After logging out, sends the user to the URL specified by LOGOUT_REDIRECT_URL in django_root/settings.py
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/',
         # The reason this view is different from the others: By default, PasswordChangeView's success_url is simply
         #  reverse_lazy('password_change_done'). But in our case, password_change_done is namespaced under "accounts",
         #  because it's in the "accounts" app, so we have to specify it as
         #  reverse_lazy('accounts:password_change_done').
         PasswordChangeView.as_view(
             template_name="accounts/password_change_form.html",
             success_url=reverse_lazy('accounts:password_change_done')
         ),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name="accounts/password_change_done.html"
         ),
         name='password_change_done'),

    path('register/', views.register, name="register"),
    path('save-user/', views.save_user, name="save-user"),

    # TODO (low priority): Move the homepage-redirect URL from django_root to here (along with its view)
]