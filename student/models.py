from django.db import models
from django.urls import reverse

from base_applicant.models import Application, School


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    SCHOOL0 = 'S0'
    SCHOOL1 = 'S1'
    SCHOOL2 = 'S2'
    SCHOOL3 = 'S3'
    SCHOOL4 = 'S4'
    SCHOOL5 = 'S5'
    SCHOOL6 = 'S6'
    SCHOOL7 = 'S7'
    SCHOOL8 = 'S8'
    SCHOOL9 = 'S9'
    SCHOOL10 = 'S10'
    SCHOOL11 = 'S11'
    SCHOOL12 = 'S12'
    SCHOOL13 = 'S13'
    SCHOOL14 = 'S14'
    SCHOOL15 = 'S15'
    SCHOOL16 = 'S16'
    SCHOOL_CHOICES = [
	(SCHOOL0, 'No school chosen'),
	(SCHOOL1, 'Arapahoe Ridge High School'),
	(SCHOOL2, 'Boulder High School'),
	(SCHOOL3, 'Boulder Prep Charter'),
	(SCHOOL4, 'Boulder TEC'),
	(SCHOOL5, 'Boulder Universal'),
	(SCHOOL6, 'Broomfield High School'),
	(SCHOOL7, 'BVSD Online'),
	(SCHOOL8, 'Centaurus High School'),
	(SCHOOL9, 'Chinnook West'),
	(SCHOOL10, 'Fairview High School'),
	(SCHOOL11, 'Halcyon School'),
	(SCHOOL12, 'Justice High School'),
	(SCHOOL13, 'Monarch High School'),
	(SCHOOL14, 'Nederland Middle-Senior High School'),
	(SCHOOL15, 'New Vista High School'),
	(SCHOOL16, 'Peak to Peak Charter School')
    ]
    first_name = models.CharField(max_length=100,default="First Name")
    last_name = models.CharField(max_length=100,default="Last Name")
    email_address = models.EmailField(max_length=100,default="Email Address")
    address = models.CharField(max_length=300,default="Home Address")
    phone_number = models.CharField(max_length=20,default="000-000-0000")
    school_choice = models.CharField(max_length=3,choices=SCHOOL_CHOICES,default="SCHOOL0")
    statement = models.FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})
