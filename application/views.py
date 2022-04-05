from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from application.models import ScholarshipApplication, AcademicFundingApplication, CustomizableApplication, \
    CustomizableApplicationType
from application.forms import ApplicationForm, ScholarshipApplicationForm, AcademicFundingApplicationForm, \
    CustomizableApplicationForm
from application.models import Application


class CustomizableApplicationCreateView(CreateView):
    model = CustomizableApplication
    form_class = CustomizableApplicationForm
    success_url = reverse_lazy("applicant:home")
    template_name = "application/custom/application_form.html"

    def get_form_kwargs(self):
        form_kwargs = super(CustomizableApplicationCreateView, self).get_form_kwargs()
        form_kwargs["app_type"] = CustomizableApplicationType.objects.get(pk=self.kwargs["app_type_pk"])
        return form_kwargs


class CustomizableApplicationTypeCreateView(CreateView):
    model = CustomizableApplicationType
    fields = "__all__"
    success_url = reverse_lazy("applicant:home")  # TODO (high priority): Move to override in org_admin
    template_name = "application/custom/application_type_form.html"


class ApplicationCreateView(CreateView):
    """Base view for anyone to create an application."""

    model = Application
    """The model to represent the application. Make sure to override this in subclasses."""

    form_class = ApplicationForm
    """The form sent to the template used for editing the application. Make sure to override this in subclasses."""

    template_name = "application/base/application_form.html"
    """The template used for editing the application. Make sure to override this in subclasses."""

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
    """The model to represent the application. Make sure to override this in subclasses."""

    form_class = ApplicationForm
    """The form sent to the template used for editing the application. Make sure to override this in subclasses."""

    template_name = "application/base/application_form.html"
    """The template used for editing the application. Make sure to override this in subclasses."""


# TODO (medium priority): Make it impossible to delete application once submitted
# TODO (medium priority): Only let user delete their own applications
class ApplicationDeleteView(DeleteView):
    """Base view for deleting an application.
    template_name is the confirmation page (e.g. "are you sure you want to delete this?")"""

    model = Application

    template_name = "application/base/application_confirm_delete.html"
    """The delete confirmation page ("are you sure you want to delete this?").
    Make sure to override this in subclasses."""


class ApplicationDetailView(DetailView):
    """Read-only view for applicants to view a single application."""

    context_object_name = "application"
    """Don't override this in subclasses"""

    model = Application
    """Make sure to override this in subclasses with the appropriate Application model (e.g. ScholarshipApplication)"""

    template_name = "application/base/application_detail.html"
    """Make sure to override this in subclasses"""


class ScholarshipApplicationCreateView(ApplicationCreateView):
    form_class = ScholarshipApplicationForm
    template_name = "application/scholarship/application_form.html"


class ScholarshipApplicationUpdateView(ApplicationUpdateView):
    form_class = ScholarshipApplicationForm
    template_name = "application/scholarship/application_form.html"


class ScholarshipApplicationDeleteView(ApplicationDeleteView):
    model = ScholarshipApplication
    template_name = "application/scholarship/application_confirm_delete.html"


class ScholarshipApplicationDetailView(ApplicationDetailView):
    model = ScholarshipApplication
    template_name = "application/scholarship/application_detail.html"


class AcademicFundingApplicationCreateView(ApplicationCreateView):
    model = AcademicFundingApplication
    form_class = AcademicFundingApplicationForm
    template_name = "application/academic_funding/application_form.html"


class AcademicFundingApplicationUpdateView(ApplicationUpdateView):
    model = AcademicFundingApplication
    form_class = AcademicFundingApplicationForm
    template_name = "application/academic_funding/application_form.html"


class AcademicFundingApplicationDeleteView(ApplicationDeleteView):
    model = AcademicFundingApplication
    template_name = "application/academic_funding/application_confirm_delete.html"


class AcademicFundingApplicationDetailView(ApplicationDetailView):
    model = AcademicFundingApplication
    template_name = "application/academic_funding/application_detail.html"


def base_view_applications(request, application_class: type[Application], template_name: str):
    """Base view for applicants to see all of their applications, in a read-only format."""
    applications: QuerySet = application_class.objects.filter(author=request.user)
    return render(request, template_name, {'applications': applications})


def base_confirm_submit_application(request, pk: int, application_class: type[Application], template_name: str):
    """Base page for confirming whether to submit an application."""
    application: application_class = application_class.objects.get(pk=pk)
    return render(request, template_name, {'application': application})


# TODO (medium priority): Make this function inaccessible except after submit confirmation
def base_submit_application(request, pk: int, application_class: type[Application], success_url: str):
    """Base function that submits the application corresponding to pk.
    Goes to success_url after the application is submitted.
    This function is called after the user confirms they want to submit it."""

    application: application_class = application_class.objects.get(pk=pk)
    application.submitted = True
    application.save()
    return redirect(success_url)
