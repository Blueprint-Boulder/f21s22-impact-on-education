from django.core.files import File
from django.db import models
from django.db.models import FileField
from django.db.models.fields.files import FieldFile
from django.urls import reverse

from accounts.models import CustomUser
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


class FileAndPerms(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=255)
    allowed_users = models.ManyToManyField(to=CustomUser)
