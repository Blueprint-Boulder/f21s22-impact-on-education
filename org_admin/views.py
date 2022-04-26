from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

import accounts.views
from application.models import Application, InternshipApplication
import org_admin.forms
from accounts.models import CustomUser


from application.views import base_submit_application
from application.models import ScholarshipApplication

import application.views


def is_org_admin(user: CustomUser):
    """Checks whether a user is an org admin"""
    return user.account_type == CustomUser.AccountTypes.ORG_ADMIN


@user_passes_test(is_org_admin)
def home(request):
    """View for the org admin homepage."""
    return render(request, "org_admin/home.html", {'user': request.user})


def create_application(request):
    return render(request, "org_admin/create_application.html")


class CustomizableApplicationTypeCreateView(application.views.CustomizableApplicationTypeCreateView):
    success_url = reverse_lazy("org_admin:home")
    template_name = "application/custom/application_type_form.html"


class ScholarshipApplicationCreateView(application.views.ScholarshipApplicationCreateView):
    template_name = "org_admin/scholarship/application_form.html"


class ScholarshipApplicationDeleteView(application.views.ScholarshipApplicationDeleteView):
    success_url = reverse_lazy('org_admin:all-scholarship-apps')
    template_name = "org_admin/scholarship/application_confirm_delete.html"


class ScholarshipApplicationDetailView(application.views.ScholarshipApplicationDetailView):
    template_name = "org_admin/scholarship/application_detail.html"


class AcademicFundingApplicationCreateView(application.views.InternshipApplicationCreateView):
    template_name = "org_admin/academic_funding/application_form.html"


class AcademicFundingApplicationDeleteView(application.views.InternshipApplicationDeleteView):
    success_url = reverse_lazy("org_admin:all-academic-funding-apps")
    template_name = "org_admin/academic_funding/application_confirm_delete.html"


class AcademicFundingApplicationDetailView(application.views.InternshipApplicationDetailView):
    template_name = "org_admin/academic_funding/application_detail.html"


@user_passes_test(is_org_admin)
def users(request):
    """A view that is a table of every user on the website, and relevant info about them."""
    return render(request, "org_admin/users.html", {'users': CustomUser.objects.all()})


class CustomUserCreateView(accounts.views.CustomUserCreateView):
    form_class = org_admin.forms.CustomUserCreationForm
    success_url = reverse_lazy("org_admin:account-created")


def account_created(request):
    return render(request, "org_admin/account_created.html")


def all_apps(request):
    return render(request, "org_admin/all_applications.html")


def all_apps_of_type(request, application_class: type[Application], template_name: str):
    """Base view for org admins to see every submitted application of a certain type, in a read-only format."""
    return render(request, template_name, {'applications': application_class.objects.filter(submitted=True)})


def all_scholarship_apps(request):
    return all_apps_of_type(request,
                            application_class=ScholarshipApplication,
                            template_name="org_admin/scholarship/applications_list.html")
