from django.db import models
from django.urls import reverse

from base_applicant.models import Application, School


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    SCHOOL0 = 'S0'
    SCHOOL1 = 'S1'
    SCHOOL2 = 'S2'
    SCHOOL3 = 'S3'
    SCHOOL_CHOICES = [
	(SCHOOL0, 'School 0'),
	(SCHOOL1, 'School 1'),
	(SCHOOL2, 'School 2'),
	(SCHOOL3, 'School 3'),
    ]
    first_name = models.CharField(max_length=100,default="No First Name Given")
    last_name = models.CharField(max_length=100,default="No Last Name Given")
    email_address = models.EmailField(max_length=100,default="No Email Given")
    address = models.CharField(max_length=300,default="No Address Given")
    phone_number = models.CharField(max_length=20,default="000-000-0000")
    school_choice = models.CharField(max_length=2,choices=SCHOOL_CHOICES,default="SCHOOL0")
    statement = models.FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})
