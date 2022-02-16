from typing import Final
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models import QuerySet
from accounts.models import CustomUser
from django.urls import reverse

from base_applicant.models import Application, School
# Create your models here.

class ScholarshipCreation(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = models.FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("org_admin:view-app", kwargs={'pk': self.pk})