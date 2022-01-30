from django.db import models
from django.urls import reverse

from base_applicant.models import Application, School, First_Name, Last_Name


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    SCHOOL1 = 'S1'
    SCHOOL2 = 'S2'
    SCHOOL3 = 'S3'
    SCHOOL_CHOICES = [
	(SCHOOL1, 'School 1'),
	(SCHOOL2, 'School 2'),
	(SCHOOL3, 'School 3'),
    ]
    first_name = models.ForeignKey(First_Name, on_delete=models.CASCADE)
    last_name = models.ForeignKey(Last_Name, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    school_choice = models.CharField(max_length=2,choices=SCHOOL_CHOICES)
    statement = models.FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})
