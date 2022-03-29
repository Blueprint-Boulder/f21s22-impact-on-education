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


class School(models.Model):
    """Represents a school that an applicant is associated with.
    The reason this is a model is so that schools can be entered into the database
     and be used by other models easily."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""

    email = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    degree = models.CharField(max_length=5)
    field_of_study = models.CharField(max_length=20)
    minors = models.CharField(max_length=20)
    grad_year = models.CharField(max_length=20)
    prompt1 = models.TextField(max_length=100)
    prompt2 = models.TextField(max_length=100)

    def get_absolute_url(self):
        return reverse("applicant:view-scholarship-app", kwargs={'pk': self.pk})


class AcademicFundingApplication(Application):
    # TODO (high priority): Make into Enum

    email = models.EmailField()
    name = models.CharField(max_length=20)
    institution = models.ForeignKey(School, on_delete=models.CASCADE)
    degree = models.CharField(max_length=20)
    field_of_study = models.CharField(max_length=20)
    minors = models.TextField(max_length=50)
    date = models.DateField()
    prompt1 = models.TextField(max_length=100)
    prompt2 = models.TextField(max_length=100)
    prompt3 = models.TextField(max_length=100)
    prompt4 = models.TextField(max_length=100)

    def get_absolute_url(self):
        return reverse("applicant:view-academic-funding-app", kwargs={'pk': self.pk})