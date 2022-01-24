import django.contrib.auth.views as django_auth_views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from accounts.forms import CustomUserCreationForm


class LoginView(django_auth_views.LoginView):
    """Displays the login form. Logs the user in when the form is submitted,
    then sends them to the URL specified by LOGIN_REDIRECT_URL in settings.py."""
    template_name = "accounts/login.html"


class LogoutView(django_auth_views.LogoutView):
    """Logs the user out and sends them to the URL specified by LOGOUT_REDIRECT_URL in settings.py.
    Doesn't use a template."""


class PasswordChangeView(django_auth_views.PasswordChangeView):
    """Displays the password change form.
    This is for a logged-in user who knows their password and wants to change it."""
    template_name = "accounts/password_change_form.html"
    success_url = reverse_lazy("accounts:password-change-done")


class PasswordChangeDoneView(django_auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class PasswordResetView(django_auth_views.PasswordResetView):
    """Displays the password reset form.
    This is for a user who forgot their password and needs to reset it."""
    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_subject.txt"
    success_url = reverse_lazy("accounts:password-reset-email-sent")
    template_name = "accounts/password_reset_form.html"


class PasswordResetEmailSentView(django_auth_views.PasswordResetDoneView):
    template_name = "accounts/password_reset_email_sent.html"


class PasswordResetEnterNewPasswordView(django_auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("accounts:password-reset-complete")
    template_name = "accounts/password_reset_enter_new_password.html"


class PasswordResetCompleteView(django_auth_views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


def register(request):
    """View of the 'create account' page that the user sees."""
    form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, "accounts/register.html", {'form': form})


# TODO (medium priority): Deny access if URL is directly entered; only allow
#  this to be run if it's called from another function. Not sure how to do this.
def save_user(request):
    """Saves the user into the database. Called after account info
    is submitted in the "register" view."""

    form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
    form.save()

    return HttpResponse("user " + request.POST['username'] + " saved")  # TODO (high priority): Make into full page
