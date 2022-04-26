from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django_root import settings
from accounts.models import CustomUser


class Application(models.Model):
    """Represents all applications for any type of funding or scholarship."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               null=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    institution = models.CharField(max_length=20)
    degree = models.CharField(max_length=5)
    field_of_study = models.CharField(max_length=20)
    minors = models.CharField(max_length=20)
    grad_year = models.CharField(max_length=20)
    work_employer = models.CharField(max_length=100)
    work_position = models.CharField(max_length=20)
    work_description = models.TextField(max_length=100)
    work_years = models.CharField(max_length=20)
    work_hours = models.CharField(max_length=20)

    volunteer_employer = models.CharField(max_length=100)
    volunteer_position = models.CharField(max_length=20)
    volunteer_description = models.TextField(max_length=100)
    volunteer_years = models.CharField(max_length=20)
    volunteer_hours = models.CharField(max_length=20)

    org_name = models.CharField(max_length=100)
    org_role = models.CharField(max_length=20)
    org_description = models.TextField(max_length=100)
    org_years = models.CharField(max_length=20)
    org_hours = models.CharField(max_length=20)

    submitted = models.BooleanField(default=False)


class CustomizableApplicationType(models.Model):
    num_text_fields = models.IntegerField()


class CustomizableApplication(models.Model):
    MAX_TEXT_FIELDS = 5
    text0 = models.TextField(max_length=5000, null=True)
    text1 = models.TextField(max_length=5000, null=True)
    text2 = models.TextField(max_length=5000, null=True)
    text3 = models.TextField(max_length=5000, null=True)
    text4 = models.TextField(max_length=5000, null=True)
    type = models.ForeignKey(to=CustomizableApplicationType, on_delete=models.CASCADE, null=True)


class School(models.Model):
    """Represents a school that an applicant is associated with.
    The reason this is a model is so that schools can be entered into the database
     and be used by other models easily."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ScholarshipApplication(Application):
    """Represents a scholarship's application for a scholarship."""
    prompt1 = models.TextField(max_length=100)
    prompt2 = models.TextField(max_length=100)

    def get_absolute_url(self):
        return reverse("applicant:view-scholarship-app", kwargs={'pk': self.pk})


class InternshipApplication(Application):
    # TODO (high priority): Make into Enum

    intprompt1 = models.TextField(max_length=100)
    intprompt2 = models.TextField(max_length=100)
    intprompt3 = models.TextField(max_length=100)
    intprompt4 = models.TextField(max_length=100)

    def get_absolute_url(self):
        return reverse("applicant:view-internship-app", kwargs={'pk': self.pk})


class VolunteerApplication(Application):
    # personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    community_service = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100)
    soft_skills = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("applicant:view-volunteer-app", kwargs={'pk': self.pk})


class CollegeApplication(Application):
    # personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    challenge = models.CharField(max_length=100)
    extracurricular = models.CharField(max_length=100)
    passions = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("applicant:view-college-app", kwargs={'pk': self.pk})
