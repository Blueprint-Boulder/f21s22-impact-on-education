from django.db import models
from django import forms
from django.urls import reverse

from base_applicant.models import Application, School


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = models.FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})


class AcademicFundingApplication(Application):

    CHOICES = [('yes', 'yes'),
               ('no', 'no')]

    Options = [('yes', 'yes'),
               ('no', 'no'),
               ('N/A', 'N/A')]

    Academic_Requests = [('Fees', 'Class Fees'),
                         ('Technology', 'Technology'),
                         ('Supplies', 'Supplies'),
                         ('Transportation', 'Transportation Expenses'),
                         ('Music', 'Music instrument rentals/repair'),
                         ('Material', 'Classroom materials or curriculum'),
                         ('Support', 'Academic Support'),
                         ('Other', 'Other')]

    email = models.EmailField()
    name = models.TextField()
    school = models.TextField()
    role = models.BooleanField()
    department = models.TextField()
    viability_and_usability = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    emergency_services = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    medical_needs = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    internet_needs = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    academic_needs = forms.ChoiceField(choices=Academic_Requests, widget=forms.RadioSelect())
    needs_assistance = models.TextField()
    funding_for = models.TextField()
    funding_need = models.TextField()
    funding_amount = models.TextField()
    students_impacted = models.TextField()
    agreement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())



