from typing import Type, Iterator

from django.contrib.auth.decorators import user_passes_test
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.forms import ModelForm
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from accounts.models import CustomUser
from base_applicant.models import Application


def is_applicant(user: CustomUser):
    """Checks whether a user is an applicant."""
    return user.account_type == CustomUser.AccountTypes.STUDENT  # TODO: ...or TEACHER, when that's made


class ApplicationCreateView(CreateView):
    """Base view for applicants to create an application.
    template_name is the template used for editing the application.
    Goes to the URL specified in model.get_absolute_url() when the application has been saved."""

    model = Application

    fields = []
    """The fields that the user can enter into the application.
    Override this in subclasses like so:
    fields = ApplicationCreateView.fields + ['some_field', 'another_field', ...]"""

    template_name = "applicant/base_application_form.html"
    """The template used for editing the application. Make sure to override this in subclasses."""

    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # form_valid means "do this thing if the form is valid", not "return whether the form is valid"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# TODO (medium priority): Make it impossible to edit application once submitted
# TODO (medium priority): Only let user edit their own applications
class ApplicationUpdateView(UpdateView):
    """Base view for applicants to edit an application.
    template_name is the template used for editing the application.
    Goes to the URL specified in model.get_absolute_url() when the application has been saved."""

    model = Application

    fields = []
    """The fields that the user can enter into the application.
        Override this in subclasses like so:
        fields = ApplicationUpdateView.fields + ['some_field', 'another_field', ...]"""

    template_name = "applicant/base_application_form.html"
    """The template used for editing the application. Make sure to override this in subclasses."""

    # This decorator stops the view from running if the user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# TODO (medium priority): Make it impossible to delete application once submitted
# TODO (medium priority): Only let user delete their own applications
class ApplicationDeleteView(DeleteView):
    """Base view for applicants to delete an application.
    template_name is the confirmation page (e.g. "are you sure you want to delete this?")"""

    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application

    template_name = "applicant/base_application_confirm_delete.html"
    """The delete confirmation page ("are you sure you want to delete this?").
    Make sure to override this in subclasses."""


@user_passes_test(is_applicant)
def base_submit_application(request, pk: int, application_class: type[Application], success_url: str):
    """Submits the application. This function is called after the user confirms
    they want to submit it."""

    # TODO (medium priority): Make this function inaccessible except after submit confirmation,
    #  and inaccessible by users who don't own the application
    # Attempt at doing this, not sure if it fully works
    if ('pk' not in request.POST) or (request.POST['pk'] != str(pk)):
        raise Http404("No associated application to submit")

    application: application_class = application_class.objects.get(pk=pk)
    application.submitted = True
    application.save()
    return redirect(success_url)


# TODO (medium priority): Make this inaccessible by users who don't own the application
@user_passes_test(is_applicant)
def base_confirm_submit_application(request, pk: int, application_class: type[Application], template_name: str):
    """Confirmation page before submitting an application."""
    application: application_class = application_class.objects.get(pk=pk)
    return render(request, template_name, {'application': application})


# --------------------------------------------------------------------------------------------------
# Old functions from when there was one app ("app" in the programming sense) for all applicants,
# before it was split into student, educator, etc.
# You can use these as a reference if you're creating a new app for another type of applicant.
# --------------------------------------------------------------------------------------------------

# # T0D0 (low priority): There's probably a better way to do this than spamming @user_passes_test; find it if possible
# @user_passes_test(is_applicant)
# def home(request):
#     """View for the base_applicant homepage."""
#     return render(request, "applicant/base_applicant_home.html", {'user': request.user})
#
#
# # T0D0 (medium priority): Only let user view their own applications
# @user_passes_test(is_applicant)
# def view_application(request, pk: int):
#     """View for applicants to see one of their applications, in a read-only format."""
#     application: Application = Application.objects.get(pk=pk)
#     return HttpResponse(f"ID {application.pk}")  # T0D0 (high priority): Make into actual page
#
#
# @user_passes_test(is_applicant)
# def view_applications(request):
#     """View for applicants to see all of their applications, in a read-only format."""
#     applications: QuerySet = Application.objects.filter(author=request.user)
#     return render(request, "applicant/applications_list.html", {'applications': applications})
#
#
# # T0D0 (medium priority): Make this inaccessible by users who don't own the application
# @user_passes_test(is_applicant)
# def confirm_submit_application(request, pk: int):
#     """Confirmation page before submitting an application."""
#     application: Application = Application.objects.get(pk=pk)
#     return render(request, "applicant/base_application_confirm_submit.html", {'application': application})
