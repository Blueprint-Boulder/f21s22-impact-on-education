import os

from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import FileField, QuerySet
from django.db.models.fields.files import FieldFile
from django.urls import reverse
from django.utils.functional import cached_property

from accounts.models import CustomUser
from base_applicant.models import Application, School
from django_root import settings


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = FileField()  # TODO: figure out what happens when upload_to=None (which is the default)
    transcript = FileField()
    recommendation_letter_1 = FileField()
    recommendation_letter_2 = FileField()
    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("student:view-app", kwargs={'pk': self.pk})
