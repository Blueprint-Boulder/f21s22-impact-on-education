from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

import application.views
from accounts.models import CustomUser
from application.views import base_submit_application, base_confirm_submit_application, base_view_applications, \
    base_create_customizable_application, base_edit_customizable_application, base_new_customizable_application_field

from application.models import ScholarshipApplication, InternshipApplication, VolunteerApplication, \
    CollegeApplication


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
    template_name = "applicant/scholarship/application_form.html"


class ScholarshipApplicationUpdateView(application.views.ScholarshipApplicationUpdateView):
    template_name = "applicant/scholarship/application_form.html"


class ScholarshipApplicationDeleteView(application.views.ScholarshipApplicationDeleteView):
    success_url = reverse_lazy('applicant:my-scholarship-apps')
    template_name = "applicant/scholarship/application_confirm_delete.html"


class ScholarshipApplicationDetailView(application.views.ScholarshipApplicationDetailView):
    template_name = "applicant/scholarship/application_detail.html"


def my_scholarship_applications(request):
    return base_view_applications(request,
                                  application_class=ScholarshipApplication,
                                  template_name="applicant/scholarship/my_applications.html")


# TODO (medium priority): Make this inaccessible by users who don't own the application
def confirm_submit_scholarship_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=ScholarshipApplication,
                                           template_name="applicant/scholarship/application_confirm_submit.html")


# TODO (medium priority): Make this inaccessible by users who don't own the application
def submit_scholarship_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=ScholarshipApplication,
                                   success_url=reverse("applicant:my-scholarship-apps"))


class InternshipApplicationCreateView(application.views.InternshipApplicationCreateView):
    template_name = "applicant/internship/application_form.html"


class InternshipApplicationUpdateView(application.views.InternshipApplicationUpdateView):
    template_name = "applicant/internship/application_form.html"


class InternshipApplicationDeleteView(application.views.InternshipApplicationDeleteView):
    success_url = reverse_lazy('applicant:my-internship-apps')
    template_name = "applicant/internship/application_confirm_delete.html"


class InternshipApplicationDetailView(application.views.InternshipApplicationDetailView):
    template_name = "applicant/internship/application_detail.html"

def my_internship_applications(request):
    return base_view_applications(request,
                                  application_class=InternshipApplication,
                                  template_name="applicant/internship/my_applications.html")

# TODO (medium priority): Make this inaccessible by users who don't own the application
def confirm_submit_internship_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=InternshipApplication,
                                           template_name="applicant/internship/application_confirm_submit.html")

# TODO (medium priority): Make this inaccessible by users who don't own the application
def submit_internship_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=InternshipApplication,
                                   success_url=reverse("applicant:my-internship-apps"))

#Volunteer Application
class VolunteerApplicationCreateView(application.views.VolunteerApplicationCreateView):
    template_name = "applicant/volunteer/application_form.html"


class VolunteerApplicationUpdateView(application.views.VolunteerApplicationUpdateView):
    template_name = "applicant/volunteer/application_form.html"


class VolunteerApplicationDeleteView(application.views.VolunteerApplicationDeleteView):
    success_url = reverse_lazy('applicant:my-volunteer-apps')
    template_name = "application/volunteer/application_confirm_delete.html"

class VolunteerApplicationDetailView(application.views.VolunteerApplicationDetailView):
    pass

def my_volunteer_applications(request):
    return base_view_applications(request,
                                  application_class=VolunteerApplication,
                                  template_name="applicant/volunteer/my_applications.html")

# TODO (medium priority): Make this inaccessible by users who don't own the application
def confirm_submit_volunteer_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=VolunteerApplication,
                                           template_name="applicant/volunteer/application_confirm_submit.html")

# TODO (medium priority): Make this inaccessible by users who don't own the application
def submit_volunteer_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=VolunteerApplication,
                                   success_url=reverse("applicant:my-volunteer-apps"))

#College Application
class CollegeApplicationCreateView(application.views.CollegeApplicationCreateView):
    template_name = "applicant/college/application_form.html"


class CollegeApplicationUpdateView(application.views.CollegeApplicationUpdateView):
    template_name = "applicant/college/application_form.html"


class CollegeApplicationDeleteView(application.views.CollegeApplicationDeleteView):
    success_url = reverse_lazy('applicant:my-college-apps')
    template_name = "applicant/college/application_confirm_delete.html"


class CollegeApplicationDetailView(application.views.CollegeApplicationDetailView):
    template_name = "applicant/college/application_detail.html"

def my_college_applications(request):
    return base_view_applications(request,
                                  application_class=CollegeApplication,
                                  template_name="applicant/college/my_applications.html")

# TODO (medium priority): Make this inaccessible by users who don't own the application
def confirm_submit_college_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=CollegeApplication,
                                           template_name="applicant/college/application_confirm_submit.html")

# TODO (medium priority): Make this inaccessible by users who don't own the application
def submit_college_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=CollegeApplication,
                                   success_url=reverse("applicant:my-college-apps"))


@user_passes_test(is_applicant)
def home(request):
    """View for the applicant homepage."""
    return render(request, "applicant/home.html", {'user': request.user})


def my_applications(request):
    """View for applicants to see all of their applications, in a read-only format."""
    return render(request, "applicant/my_applications.html")


