from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from accounts.models import CustomUser
from base_applicant.views import ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView, \
    base_submit_application, base_confirm_submit_application, base_view_applications, ApplicationDetailView
from student.models import ScholarshipApplication, FileAndPerms


class ScholarshipApplicationCreateView(ApplicationCreateView):
    model = ScholarshipApplication
    fields = ApplicationCreateView.fields + ['high_school',
                                             'statement',
                                             'transcript',
                                             'recommendation_letter_1', 'recommendation_letter_2',
                                             'acknowledged']
    template_name = "student/application_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        assert isinstance(self.object, ScholarshipApplication)
        recommendation_letter_1_and_perms = FileAndPerms(file=self.object.recommendation_letter_1)
        recommendation_letter_1_and_perms.name = self.object.recommendation_letter_1.name
        recommendation_letter_1_and_perms.save()
        recommendation_letter_1_and_perms.allowed_users.set(CustomUser.objects.filter(pk=self.request.user.pk))
        recommendation_letter_1_and_perms.save()
        return response


class ScholarshipApplicationUpdateView(ApplicationUpdateView):
    model = ScholarshipApplication
    fields = ApplicationUpdateView.fields + ['high_school',
                                             'statement',
                                             'transcript',
                                             'recommendation_letter_1', 'recommendation_letter_2',
                                             'acknowledged']
    template_name = "student/application_form.html"


class ScholarshipApplicationDeleteView(ApplicationDeleteView):
    model = ScholarshipApplication
    success_url = reverse_lazy('student:view-apps')  # goes here after confirmation
    template_name = "student/application_confirm_delete.html"  # confirmation page


def home(request):
    """View for the student homepage."""
    return render(request, "student/student_home.html", {'user': request.user})


class ScholarshipApplicationDetailView(ApplicationDetailView):
    model = ScholarshipApplication
    template_name = "student/application_detail.html"


def view_application(request, pk: int):
    """View for students to see one of their applications, in a read-only format."""
    application: ScholarshipApplication = ScholarshipApplication.objects.get(pk=pk)
    # TODO (high priority): Make into actual page
    return HttpResponse(f"SCHOLARSHIP APPLICATION<br>ID {application.pk}")


def view_applications(request):
    """View for students to see all of their applications, in a read-only format."""
    return base_view_applications(request,
                                  application_class=ScholarshipApplication,
                                  template_name="student/applications_list.html")


def confirm_submit_application(request, pk: int):
    """Confirmation page before submitting an application."""
    return base_confirm_submit_application(request, pk=pk,
                                           application_class=ScholarshipApplication,
                                           template_name="student/application_confirm_submit.html")


def submit_application(request, pk: int):
    return base_submit_application(request, pk=pk,
                                   application_class=ScholarshipApplication,
                                   success_url=reverse("student:view-apps"))


def pdf_view_with_perms(request, name: str):
    pdf_and_perms = FileAndPerms.objects.get(name=name)
    if pdf_and_perms.allowed_users.filter(pk=request.user.pk).exists():
        pdf_content = pdf_and_perms.file.read()
        pdf_and_perms.file.close()
        return HttpResponse(pdf_content, content_type="application/pdf")
    else:
        return HttpResponse("<h1>you don't own this file</h1>")
