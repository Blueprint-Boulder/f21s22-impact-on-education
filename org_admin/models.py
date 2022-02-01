from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from base_applicant.models import Application, School
# Create your models here.



class ScholarshipCreation(Application):
    """Represents an org admin's creation of a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = models.FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()
    acknowledged = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("student:orghome", kwargs={'pk': self.pk})
