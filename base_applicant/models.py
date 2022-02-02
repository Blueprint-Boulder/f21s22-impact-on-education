from enum import Enum

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
    submitted = models.BooleanField(default=False)


class School(models.Model):
    """Represents a school that an applicant is associated with.
    The reason this is a model is so that schools can be entered into the database
     and be used by other models easily."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name