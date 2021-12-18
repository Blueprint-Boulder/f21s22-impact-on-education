from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django_root import settings
from accounts.models import CustomUser


class Application(models.Model):
    author: CustomUser = models.ForeignKey(settings.AUTH_USER_MODEL,
                                           on_delete=models.CASCADE,
                                           null=True)
    text: models.TextField = models.TextField(max_length=5000)
    submitted: models.BooleanField = models.BooleanField(default=False)

    # ApplicationCreateView and ApplicationUpdateView go to this URL after the creation/editing is finished
    def get_absolute_url(self):
        # TODO (high priority): Make this function link to a redirect page
        #  that goes to a different application viewing page depending on
        #  whether the user is an admin, volunteer, or applicant
        return reverse('applicant:view-app', kwargs={'pk': self.pk})
