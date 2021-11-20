from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django_root.views import is_in_group
from applicant.models import Application


def is_applicant(user: get_user_model()):
    return user.groups.filter(name="applicant").exists()


# View to create application
# Uses the template application_form.html for editing the application
# Goes to the URL specified in Application.get_absolute_url() (located in applicant/models.py) when the
# application has been saved
class ApplicationCreateView(CreateView):
    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application
    fields = ['text']

    def form_valid(self, form):
        """ If the applicant is not yet associated with a user
        (i.e. if this is a new application), associate it with
        the current user
        """
        if not form.instance.author:
            form.instance.author = self.request.user
        return super().form_valid(form)


# View to edit application
# Uses the template application_form.html for editing the application
# Goes to the URL specified in Application.get_absolute_url() (located in applicant/models.py) when the
# application has been saved
# TODO (medium priority): Make it impossible to edit application once submitted
# TODO (medium priority): Only let user edit their own applications
class ApplicationUpdateView(UpdateView):
    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application
    fields = ['text']


# View to delete application
# Uses the template application_confirm_delete.html
# TODO (medium priority): Make it impossible to delete application once submitted
# TODO (medium priority): Only let user delete their own applications
class ApplicationDeleteView(DeleteView):
    # Stops view from running if user is not an applicant
    @method_decorator(user_passes_test(is_applicant))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Application
    success_url = reverse_lazy('applicant:view-apps')


# TODO (low priority): There's probably a better way to do this than spamming @user_passes_test; find it if possible
@user_passes_test(is_applicant)
def home(request):
    return render(request, "applicant/applicant_home.html", {'user': request.user})


@user_passes_test(is_applicant)
def view_application(request, pk: int):
    application = Application.objects.get(pk=pk)
    return HttpResponse(application.text)  # TODO (medium priority): Make into actual page


# View of all the user's applications
@user_passes_test(is_applicant)
def view_applications(request):
    applications = Application.objects.filter(author=request.user)
    return render(request, "applicant/applications_list.html", {'applications': applications})


# TODO (medium priority): Make this inaccessible by users who don't own the application
@user_passes_test(is_applicant)
def confirm_submit_application(request, pk: int):
    application = Application.objects.get(pk=pk)
    return render(request, "applicant/application_confirm_submit.html", {'application': application})


# TODO (medium priority): Make this inaccessible except after submit confirmation,
#  and inaccessible by users who don't own the application
@user_passes_test(is_applicant)
def submit_application(request, pk: int):
    # Attempt at doing the above, not sure if it fully works
    if ('pk' not in request.POST) or (request.POST['pk'] != str(pk)):
        raise Http404("No associated application to submit")
    application = Application.objects.get(pk=pk)
    application.submitted = True
    application.save()
    return redirect(reverse("applicant:home"))
