from django.forms import ModelForm

from application.models import AcademicFundingApplication, ScholarshipApplication
from application.models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['address', 'phone_number', 'author', 'submitted']
        # TODO (high priority): Add relevant fields (not sure what yet)


class AcademicFundingApplicationForm(ApplicationForm):
    class Meta:
        model = AcademicFundingApplication
        fields = ApplicationForm.Meta.fields + ['email', 'name', 'institution', 'degree',
                                                'field_of_study', 'minors', 'date', 'prompt1',
                                                'prompt2', 'prompt3', 'prompt4']
        labels = {
            'email': 'Enter Your Email',
            'name': 'Enter Your Name',
            'institution': 'Name of Institution',
            'degree': 'Enter Degree Type',
            'field_of_study': 'Enter Your Field of Study',
            'minors': 'Enter Your Minors',
            'date': 'Enter Your Expected Year of Graduation',
            'prompt1': 'Describe a time when you worked on a team, and had a struggle. '
                    'How did you overcome this, and what would you do if you faced the same situation again?' ,
            'prompt2': 'Describe a time you worked on a team, and it went smoothly. What aspects of your teamwork made'
                      'this group successful?',
            'prompt3': 'Describe one of your strengths and one of your weaknesses.',
            'prompt4': 'Why are you interested in this company and position?'
        }


class ScholarshipApplicationForm(ApplicationForm):
    class Meta:
        model = ScholarshipApplication
        # TODO (low priority): Make this a call to super() somehow instead of explicitly referencing ApplicationForm
        fields = ApplicationForm.Meta.fields + ["email", "institution", "degree",
                                                "field_of_study", "minors", "grad_year", "prompt1", "prompt2"]
        labels = {
            'institution': 'Name of institution',
            'degree': 'Degree Type',
            'grad_year': 'Expected Graduation Year',
            'prompt1': 'What is a struggle you have recently overcome or are dealing with now? What steps did you'
                       ' take/are you taking to handle this issue?',
            'prompt2': 'Are you involved in any activities in school or in your community? If so, please describe them'
                       ' and what your role in them looks like.'
        }

