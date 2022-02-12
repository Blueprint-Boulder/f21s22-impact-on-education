from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from accounts.views import CustomUserCreateView
from base_applicant.models import Application
from org_admin.forms import AdminCustomUserCreationForm
from accounts.models import CustomUser


from base_applicant.views import base_submit_application, base_confirm_submit_application
from student.models import ScholarshipApplication

from student.views import ScholarshipApplicationCreateView, ScholarshipApplicationUpdateView, \
    ScholarshipApplicationDeleteView, ScholarshipApplicationDetailView

# TODO (high priority): Implement actual namespacing instead of these weird long names
#  (e.g. refer to ScholarshipApplicationCreateViewAdmin as org_admin.ScholarshipApplicationCreateView)


class ScholarshipApplicationCreateViewAdmin(ScholarshipApplicationCreateView):
    template_name = "org_admin/application_form.html"


class ScholarshipApplicationUpdateViewAdmin(ScholarshipApplicationUpdateView):
    template_name = "org_admin/application_form.html"


class ScholarshipApplicationDeleteViewAdmin(ScholarshipApplicationDeleteView):
    success_url = reverse_lazy('org_admin:view-apps')
    template_name = "org_admin/application_confirm_delete.html"


def is_org_admin(user: CustomUser):
    """Checks whether a user is an org admin"""
    return user.account_type == CustomUser.AccountTypes.ORG_ADMIN


# Users table
@user_passes_test(is_org_admin)
def users(request):
    """A view that is a table of every user on the website, and relevant info about them."""
    return render(request, "org_admin/users.html", {'users': CustomUser.objects.all()})


class AdminCustomUserCreateView(CustomUserCreateView):
    form_class = AdminCustomUserCreationForm
    success_url = reverse_lazy("org-admin:account-created")


def account_created(request):
    return render(request, "org_admin/account_created.html")


def home(request):
    """View for the org admin homepage."""
    return render(request, "org_admin/org_admin_home.html", {'user': request.user})


class ScholarshipApplicationDetailViewAdmin(ScholarshipApplicationDetailView):
    pass


def all_apps(request, application_class: type[Application], template_name: str):
    """View for org admins to see every application by anyone, in a read-only format."""
    return render(request, template_name, {'applications': application_class.objects.all()})


def all_scholarship_apps(request):
    return all_apps(request,
                    application_class=ScholarshipApplication,
                    template_name="org_admin/scholarship_apps_list.html")


# TODO (high priority): Add all_academic_funding_apps()


def confirm_submit_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=ScholarshipApplication,
                                           template_name="org_admin/application_confirm_submit.html")


def submit_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=ScholarshipApplication,
                                   success_url=reverse("org_admin:view-apps"))
