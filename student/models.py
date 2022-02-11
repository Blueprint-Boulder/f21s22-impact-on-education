from django.db import models
from django.db.models import FileField
from django.urls import reverse

from accounts.models import CustomUser
from base_applicant.models import Application, School


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = FileField()
    transcript = FileField()
    recommendation_letter_1 = FileField()
    recommendation_letter_2 = FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})
