from django.apps import AppConfig


class BaseApplicantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_applicant'
