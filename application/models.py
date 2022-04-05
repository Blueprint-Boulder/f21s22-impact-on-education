from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django_root import settings
from accounts.models import CustomUser


class Application(models.Model):
    """Represents all applications for any type of funding or scholarship."""
    address = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               null=True)
    submitted = models.BooleanField(default=False)


class CustomizableApplicationType(models.Model):
    num_text_fields = models.IntegerField()


class CustomizableApplication(models.Model):
    MAX_TEXT_FIELDS = 5
    text0 = models.TextField(max_length=5000, null=True)
    text1 = models.TextField(max_length=5000, null=True)
    text2 = models.TextField(max_length=5000, null=True)
    text3 = models.TextField(max_length=5000, null=True)
    text4 = models.TextField(max_length=5000, null=True)
    type = models.ForeignKey(to=CustomizableApplicationType, on_delete=models.CASCADE, null=True)


class School(models.Model):
    """Represents a school that an applicant is associated with.
    The reason this is a model is so that schools can be entered into the database
     and be used by other models easily."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = models.FileField()
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()

    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("applicant:view-scholarship-app", kwargs={'pk': self.pk})


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
    school = models.ForeignKey(School, on_delete=models.CASCADE)
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

    def get_absolute_url(self):
        return reverse("applicant:view-academic-funding-app", kwargs={'pk': self.pk})