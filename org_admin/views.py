from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from base_applicant.models import Application
from accounts.models import CustomUser
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from base_applicant.views import ApplicationCreateViewAdmin, ApplicationUpdateViewAdmin, ApplicationDeleteViewAdmin, \
    base_submit_application, base_confirm_submit_application, base_view_applications
from org_admin.models import ScholarshipCreation


# Below is all Creation of new scholarship application

class ScholarshipApplicationCreateViewAdmin(ApplicationCreateViewAdmin):
    model = ScholarshipCreation
    fields = ApplicationCreateViewAdmin.fields + ['high_school',
                                             'statement',
                                             'transcript',
                                             'recommendation_letter_1', 'recommendation_letter_2',
                                             'acknowledged']
    template_name = "org_admin/application_form.html"


class ScholarshipApplicationUpdateViewAdmin(ApplicationUpdateViewAdmin):
    model = ScholarshipCreation
    fields = ApplicationUpdateViewAdmin.fields + ['high_school',
                                             'statement',
                                             'transcript',
                                             'recommendation_letter_1', 'recommendation_letter_2',
                                             'acknowledged']
    template_name = "org_admin/application_form.html"


class ScholarshipApplicationDeleteViewAdmin(ApplicationDeleteViewAdmin):
    model = ScholarshipCreation
    success_url = reverse_lazy('org_admin:view-apps')  # goes here after confirmation
    template_name = "org_admin/application_confirm_delete.html"  # confirmation page



def is_admin(user: CustomUser):
    """Checks whether a user is an org admin"""
    return user.account_type == CustomUser.AccountTypes.ORG_ADMIN

# Users table
@user_passes_test(is_admin)
def users(request):
    """A view that is a table of every user on the website, and relevant info about them."""
    return render(request, "org_admin/users.html", {'users': CustomUser.objects.all()})

def home(request):
    """View for the student homepage."""
    return render(request, "org_admin/orgadmin_home.html", {'user': request.user})


def view_application(request, pk: int):
    """View for students to see one of their applications, in a read-only format."""
    application: ScholarshipCreation = ScholarshipCreation.objects.get(pk=pk)
    # TODO (high priority): Make into actual page
    return HttpResponse(f"SCHOLARSHIP APPLICATION<br>ID {application.pk}")


def view_applications(request):
    """View for students to see all of their applications, in a read-only format."""
    return base_view_applications(request,
                                  application_class=ScholarshipCreation,
                                  template_name="org_admin/applications_list.html")


def confirm_submit_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=ScholarshipCreation,
                                           template_name="org_admin/application_confirm_submit.html")


def submit_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=ScholarshipCreation,
                                   success_url=reverse("org_admin:view-apps"))