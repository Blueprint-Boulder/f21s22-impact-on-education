from django.db import models

from django.urls import reverse

from accounts.models import CustomUser
from base_applicant.models import Application, School


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = models.FileField()
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()

    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})


class AcademicFundingApplication(Application):
    # TODO (high priority): Make into Enum
    Roles = [('Principal', 'Principal'),
             ('Principal_Assistant', 'Principal Assistant or Main Office Mgr'),
             ('Assistant', 'Assistant Principal'),
             ('Educator', 'Educator')]

    # TODO (high priority): Make into Enum
    Academic_Requests = [('Fees', 'Class Fees'),
                         ('Technology', 'Technology'),
                         ('Supplies', 'Supplies'),
                         ('Transportation', 'Transportation Expenses'),
                         ('Music', 'Music instrument rentals/repair'),
                         ('Material', 'Classroom materials or curriculum'),
                         ('Support', 'Academic Support'),
                         ('Other', 'Other')]

    email = models.EmailField()
    name = models.CharField(max_length=20)
    school = models.CharField(max_length=40)
    role = models.CharField(max_length=20, choices=Roles)
    department = models.CharField(max_length=50)
    viability_and_usability = models.BooleanField()
    emergency_services = models.BooleanField()
    medical_needs = models.BooleanField()
    internet_needs = models.BooleanField()
    academic_needs = models.CharField(max_length=30, choices=Academic_Requests)
    needs_assistance = models.TextField(max_length=100)
    funding_for = models.TextField(max_length=100)
    funding_need = models.TextField(max_length=100)
    funding_amount = models.CharField(max_length=100)
    students_impacted = models.CharField(max_length=100)
    agreement = models.BooleanField()
