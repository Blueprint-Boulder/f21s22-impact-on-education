import django.contrib.auth.views as django_auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


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


# TODO (low priority): Figure out if changing the template to accounts/profile.html,
#  and overriding get_context_data() to pass in password_changed=True, would break anything.
#  If it wouldn't, do that (and edit accounts/profile.html accordingly).
class PasswordChangeDoneView(django_auth_views.PasswordChangeDoneView):
    """Displays a message indicating that the password has been successfully changed."""
    template_name = "accounts/password_change_done.html"


class PasswordResetView(django_auth_views.PasswordResetView):
    """Displays a form that asks for an email address associated with an account.
    The password reset email will be sent to that address.
    For a user who forgot their password and needs to reset it."""
    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_email_subject.txt"
    success_url = reverse_lazy("accounts:password-reset-email-sent")
    template_name = "accounts/password_reset_form.html"


class PasswordResetEmailSentView(django_auth_views.PasswordResetDoneView):
    """Displays a confirmation message indicating that the password reset email has been sent."""
    template_name = "accounts/password_reset_email_sent.html"


class PasswordResetEnterNewPasswordView(django_auth_views.PasswordResetConfirmView):
    """Displays a form for the user to enter a new password. Used for password resets."""
    success_url = reverse_lazy("accounts:password-reset-complete")
    template_name = "accounts/password_reset_enter_new_password.html"


class PasswordResetCompleteView(django_auth_views.PasswordResetCompleteView):
    """Displays a message indicating that the password has been successfully reset."""
    template_name = "accounts/password_reset_complete.html"


class CustomUserCreateView(CreateView):
    """View for creating a CustomUser."""
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:account-created")


# TODO (low priority): Find out if subclassing DetailView is better for this
@login_required
def profile(request):
    """A read-only view of the user's profile."""
    return render(request, "accounts/profile.html", {'user': request.user})


class ProfileEditView(UpdateView):
    """View for a user to edit their profile."""
    model = CustomUser
    template_name = "accounts/profile_edit.html"
    fields = ("username", "email", "first_name", "last_name")
    # TODO (low priority): Find a way to make success_url "accounts:profile" and pass in the profile_updated context
    success_url = reverse_lazy("accounts:profile-saved")

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def profile_saved(request):
    """A read-only view of the user's profile, which also displays a confirmation message
     indicating the profile has been successfully updated.
     This view should be accessed after a user edits their profile."""
    return render(request, "accounts/profile.html", {'user': request.user, 'profile_updated': True})


def account_created(request):
    """Displays a success message after creating a user."""
    return render(request, "accounts/account_created.html")
