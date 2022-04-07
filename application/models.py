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

#class WorkExperience(models.Model):
  #  """Represents questions about work experience."""


#class VolunteerExperience(Application):
 #   """Represents questions about work experience."""


#class ClubExperience(Application):
   # """Represents questions about work experience."""


   # work_experience = models.ManyToManyField(to=WorkExperience)
   #volunteer_experience = models.ManyToManyField(to=VolunteerExperience)
   # club_experience = models.ManyToManyField(to=ClubExperience)

class School(models.Model):
    """Represents a school that an applicant is associated with.
    The reason this is a model is so that schools can be entered into the database
     and be used by other models easily."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ScholarshipApplication(Application):
    """Represents a student's application for a scholarship."""
    high_school = models.ForeignKey(School, on_delete=models.CASCADE)
    statement = models.FileField()
    transcript = models.FileField()
    recommendation_letter_1 = models.FileField()
    recommendation_letter_2 = models.FileField()

    acknowledged = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("applicant:view-scholarship-app", kwargs={'pk': self.pk})

class AcademicFundingApplication(Application):
    # TODO (high priority): Make into Enum
    Roles = [('Principal', 'Principal'),
             ('Principal_Assistant', 'Principal Assistant or Main Office Mgr'),
             ('Assistant', 'Assistant Principal'),
             ('Educator', 'Educator')]

    # TODO (high priority): Make into Enum
    Academic_Requests = [('Fees', 'Class Fees'),
                         ('Technology', 'Technology'),
                         ('Supplies', 'Supplies'),
                         ('Transportation', 'Transportation Expenses'),
                         ('Music', 'Music instrument rentals/repair'),
                         ('Material', 'Classroom materials or curriculum'),
                         ('Support', 'Academic Support'),
                         ('Other', 'Other')]

    email = models.EmailField()
    name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Roles)
    department = models.CharField(max_length=50)
    viability_and_usability = models.BooleanField()
    emergency_services = models.BooleanField()
    medical_needs = models.BooleanField()
    internet_needs = models.BooleanField()
    academic_needs = models.CharField(max_length=30, choices=Academic_Requests)
    needs_assistance = models.TextField(max_length=100)
    funding_for = models.TextField(max_length=100)
    funding_need = models.TextField(max_length=100)
    funding_amount = models.CharField(max_length=100)
    students_impacted = models.CharField(max_length=100)
    agreement = models.BooleanField()

class VolunteerApplication(Application):
    #personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    community_service = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100)
    soft_skills = models.CharField(max_length=100)

    def get_absolute_url(self):
            return reverse("applicant:view-volunteer-app", kwargs={'pk': self.pk})

class CollegeApplication(Application):
    #personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    challenge = models.CharField(max_length=100)
    extracurricular = models.CharField(max_length=100)
    passions = models.CharField(max_length=100)

    def get_absolute_url(self):
            return reverse("applicant:view-college-app", kwargs={'pk': self.pk})


