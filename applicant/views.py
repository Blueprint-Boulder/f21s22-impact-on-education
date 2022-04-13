from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

import application.views
from accounts.models import CustomUser
from application.views import base_submit_application, base_confirm_submit_application, base_view_applications, \
    base_create_customizable_application, base_edit_customizable_application, base_new_customizable_application_field

from application.models import ScholarshipApplication, AcademicFundingApplication, Application


def is_applicant(user: CustomUser):
    """Checks whether a user is an applicant."""
    return user.account_type == CustomUser.AccountTypes.APPLICANT


def create_application(request):
    return render(request, "applicant/create_application.html")


def create_customizable_application(request, app_type_pk: int):
    return base_create_customizable_application(request, app_type_pk,
                                                template_name="applicant/custom/application_form.html")


def edit_customizable_application(request, pk: int, num_text_fields: int):
    return base_edit_customizable_application(request, pk, num_text_fields,
                                              template_name="applicant/custom/application_form.html")


def new_customizable_application_field(request):
    return base_new_customizable_application_field(request, edit_app_urlname="applicant:edit-custom-app")


class ScholarshipApplicationCreateView(application.views.ScholarshipApplicationCreateView):
    template_name = "applicant/student/application_form.html"


class ScholarshipApplicationUpdateView(application.views.ScholarshipApplicationUpdateView):
    template_name = "applicant/student/application_form.html"


class ScholarshipApplicationDeleteView(application.views.ScholarshipApplicationDeleteView):
    success_url = reverse_lazy('applicant:my-scholarship-apps')
    template_name = "applicant/student/application_confirm_delete.html"


class ScholarshipApplicationDetailView(application.views.ScholarshipApplicationDetailView):
    template_name = "applicant/student/application_detail.html"


class AcademicFundingApplicationCreateView(application.views.AcademicFundingApplicationCreateView):
    template_name = "applicant/educator/application_form.html"


class AcademicFundingApplicationUpdateView(application.views.AcademicFundingApplicationUpdateView):
    template_name = "applicant/educator/application_form.html"


class AcademicFundingApplicationDeleteView(application.views.AcademicFundingApplicationDeleteView):
    success_url = reverse_lazy('applicant:my-academic-funding-apps')
    template_name = "applicant/educator/application_confirm_delete.html"


class AcademicFundingApplicationDetailView(application.views.AcademicFundingApplicationDetailView):
    template_name = "applicant/educator/application_detail.html"


@user_passes_test(is_applicant)
def home(request):
    """View for the applicant homepage."""
    return render(request, "applicant/home.html", {'user': request.user})


def my_applications(request):
    """View for applicants to see all of their applications, in a read-only format."""
    return render(request, "applicant/my_applications.html")


def my_scholarship_applications(request):
    return base_view_applications(request,
                                  application_class=ScholarshipApplication,
                                  template_name="applicant/student/my_applications.html")


def my_academic_funding_applications(request):
    return base_view_applications(request,
                                  application_class=AcademicFundingApplication,
                                  template_name="applicant/educator/my_applications.html")


# TODO (medium priority): Make this inaccessible by users who don't own the application
def confirm_submit_scholarship_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=ScholarshipApplication,
                                           template_name="applicant/student/application_confirm_submit.html")


def confirm_submit_academic_funding_application(request, pk: int):
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=AcademicFundingApplication,
                                           template_name="applicant/educator/application_confirm_submit.html")


# TODO (medium priority): Make this inaccessible by users who don't own the application
def submit_scholarship_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=ScholarshipApplication,
                                   success_url=reverse("applicant:my-scholarship-apps"))


def submit_academic_funding_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=AcademicFundingApplication,
                                   success_url=reverse("applicant:my-academic-funding-apps"))
