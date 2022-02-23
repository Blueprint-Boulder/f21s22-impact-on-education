from typing import Final
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models import QuerySet
from accounts.models import CustomUser
from django.urls import reverse
from base_applicant.models import Application, School
# Create your models here.
