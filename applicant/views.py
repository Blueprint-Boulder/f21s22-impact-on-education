from django.contrib.auth.decorators import user_passes_test
from django.db.models import QuerySet
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.models import CustomUser
from applicant.models import Application


def is_applicant(user: CustomUser):
    """Checks whether a user is an applicant."""
    return user.account_type == CustomUser.AccountTypes.APPLICANT


class ApplicationCreateView(CreateView):
    """View for applicants to create an application. Uses the template application_form.html
    for editing the application. Goes to the URL specified in Application.get_absoulte_url() when
    the application has been saved."""

    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application
    fields = ['text']

    def form_valid(self, form):
        # If the applicant is not yet associated with a user
        #  (i.e. if this is a new application), associate it with
        #  the current user
        if not form.instance.author:
            form.instance.author = self.request.user
        return super().form_valid(form)


# TODO (medium priority): Make it impossible to edit application once submitted
# TODO (medium priority): Only let user edit their own applications
class ApplicationUpdateView(UpdateView):
    """View for applicants to edit an application. Uses the template application_form.html
    for editing the application. Goes to the URL specified in Application.get_absolute_url()
    when the application has been saved."""

    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application
    fields = ['text']


# TODO (medium priority): Make it impossible to delete application once submitted
# TODO (medium priority): Only let user delete their own applications
class ApplicationDeleteView(DeleteView):
    """View for applicants to delete an application. Uses the template
    application_confirm_delete.html."""

    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application
    success_url = reverse_lazy('applicant:view-apps')


# TODO (low priority): There's probably a better way to do this than spamming @user_passes_test; find it if possible
@user_passes_test(is_applicant)
def home(request):
    """View for the applicant homepage."""
    return render(request, "applicant/applicant_home.html", {'user': request.user})


# TODO (medium priority): Only let user view their own applications
@user_passes_test(is_applicant)
def view_application(request, pk: int):
    """View for applicants to see one of their applications, in a read-only format."""
    application: Application = Application.objects.get(pk=pk)
    return HttpResponse(application.text)  # TODO (medium priority): Make into actual page


@user_passes_test(is_applicant)
def view_applications(request):
    """View for applicants to see all of their applications, in a read-only format."""
    applications: QuerySet = Application.objects.filter(author=request.user)
    return render(request, "applicant/applications_list.html", {'applications': applications})


# TODO (medium priority): Make this inaccessible by users who don't own the application
@user_passes_test(is_applicant)
def confirm_submit_application(request, pk: int):
    """Confirmation page before submitting an application."""
    application: Application = Application.objects.get(pk=pk)
    return render(request, "applicant/application_confirm_submit.html", {'application': application})


@user_passes_test(is_applicant)
def submit_application(request, pk: int):
    """Submits the application. This function is called after the user confirms
    they want to submit it."""

    # TODO (medium priority): Make this function inaccessible except after submit confirmation,
    #  and inaccessible by users who don't own the application
    # Attempt at doing this, not sure if it fully works
    if ('pk' not in request.POST) or (request.POST['pk'] != str(pk)):
        raise Http404("No associated application to submit")

    application: Application = Application.objects.get(pk=pk)
    application.submitted = True
    application.save()
    return redirect(reverse("applicant:home"))
