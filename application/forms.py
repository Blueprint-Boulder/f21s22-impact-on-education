from django.db.models import TextField
from django.forms import ModelForm, CharField, Textarea, HiddenInput
from django.forms.utils import ErrorList
from application.redact import core_nlp

from application.models import Application, ScholarshipApplication, VolunteerApplication, CollegeApplication, \
    InternshipApplication, CustomizableApplication, CustomizableApplicationType


class CustomizableApplicationForm(ModelForm):
    class Meta:
        model = CustomizableApplication
        fields = ["text0", "text1", "text2", "text3", "text4"]

    def __init__(self, *args, app_type: CustomizableApplicationType = None, num_text_fields: int = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_text_fields = num_text_fields
        if app_type:
            self.instance.type = app_type
        field_names_to_display: list[str] = [f"text{i}" for i in range(0, num_text_fields)]
        for field_name, field in self.fields.items():
            if field_name not in field_names_to_display:
                self.fields[field_name] = CharField(max_length=5000, widget=HiddenInput, required=False)
            else:
                self.fields[field_name] = CharField(max_length=5000, required=False)


class ApplicationForm(ModelForm):

    class Meta:
        model = Application
        fields = ['author','name','address', 'phone_number', 'email', 'institution', 'degree',
                                                'field_of_study', 'minors', 'grad_year', 'work_employer', 'work_position', 'work_description', 'work_years',
                  'work_hours', 'volunteer_employer', 'volunteer_position', 'volunteer_description',
                  'volunteer_years', 'volunteer_hours', 'org_name', 'org_role', 'org_description',
                  'org_years', 'org_hours']
        labels = {
            'author': 'Input user type.',
            'name': 'Enter your name (First Middle Last).',
            'address': 'Enter your address.',
            'phone_number': 'Enter your phone number.',
            'email': 'Enter your email.',
            'institution': 'Name of Institution',
            'degree': 'Enter Degree Type',
            'field_of_study': 'Enter Your Field of Study',
            'minors': 'Enter Your Minors',
            'grad_year': 'Enter Your Expected Year of Graduation',
            'work_employer': 'Enter the name of the company.',
            'work_position': 'Enter your position at that company.',
            'work_description': 'Enter a description of your work at the company.',
            'work_years': 'Enter your start and end date at that company. (MM/DD/YYYY-MM/DD/YYYY)',
            'work_hours': 'Approximately how many hours did you work at this company each week?',
            'volunteer_employer': 'Enter the name of the organization',
            'volunteer_position': 'Enter your position at this organization.',
            'volunteer_description': 'Describe the club or organization, and how you contributed.',
            'volunteer_years': 'Enter your start and end date at this organization. (MM/DD/YYYY-MM/DD/YYYY)',
            'volunteer_hours': 'Approximately how many hours did you volunteer at this organization each week?'
                               'org_name: Enter the name of the organization',
            'org_role': 'Enter your position at this organization.',
            'org_description': 'Describe the club or organization, and how you contributed.',
            'org_years': 'Enter your start and end date at this organization. (MM/DD/YYYY-MM/DD/YYYY)',
            'org_hours': 'Approximately how many hours did you work for this club or organization each week?',
        }

    def save(self, commit=True):
        for field_name, field in self.fields.items():
            # TODO (high priority): Make fields have a "redact" boolean attribute instead of this length check
            if isinstance(field, CharField) and field.max_length > 50:
                field_data: str = getattr(self.instance, field_name)
                setattr(self.instance, field_name, core_nlp(field_data))
        return super().save(commit)


class InternshipApplicationForm(ApplicationForm):
    class Meta:
        model = InternshipApplication
        fields = ApplicationForm.Meta.fields + ['intprompt1',
                                                'intprompt2', 'intprompt3', 'intprompt4']
        labels = {**ApplicationForm.Meta.labels,
            'intprompt1': 'Describe a time when you worked on a team, and had a struggle. '
                    'How did you overcome this, and what would you do if you faced the same situation again?' ,
            'intprompt2': 'Describe a time you worked on a team, and it went smoothly. What aspects of your teamwork made'
                      'this group successful?',
            'intprompt3': 'Describe one of your strengths and one of your weaknesses.',
            'intprompt4': 'Why are you interested in this company and position?'
        }


class VolunteerApplicationForm(ApplicationForm):
    class Meta:
        model = VolunteerApplication
        fields = ApplicationForm.Meta.fields + ['position', 'availability', 'community_service', 'alignment',
                                                'soft_skills']
        labels = {**ApplicationForm.Meta.labels,
                  # 'personal_info': 'Enter your personal Information',
                  'position': 'What position are you applying for?',
                  'availability': 'Enter your expected weekly availability.',
                  'community_service': 'Are you applying for this position to complete court-ordered community service?',
                  'alignment': 'Describe how volunteering with this organization aligns with your passions, values and/or goals.',
                  'soft_skills': 'Describe the soft skills you possess that apply to this role.'
                  }


class CollegeApplicationForm(ApplicationForm):
    class Meta:
        model = CollegeApplication
        fields = ApplicationForm.Meta.fields + ['major', 'challenge', 'extracurricular', 'passions']
        labels = {**ApplicationForm.Meta.labels,
                  'major': 'Enter the major you are applying for.',
                  'challenge': 'Describe a time when you had to try and overcome a challenge. Were you successful? What did you gain from the experience?',
                  'extracurricular': 'Describe any extracurricular activities you have been involved with during high school. Please describe your role and the hours spent per week.',
                  'passions': 'Describe one of your passions.'
                  }


class ScholarshipApplicationForm(ApplicationForm):
    class Meta:
        model = ScholarshipApplication
        # TODO (low priority): Make this a call to super() somehow instead of explicitly referencing ApplicationForm
        fields = ApplicationForm.Meta.fields + ["prompt1", "prompt2"]
        labels = {**ApplicationForm.Meta.labels,
            'prompt1': 'What is a struggle you have recently overcome or are dealing with now? What steps did you'
                       ' take/are you taking to handle this issue?',
            'prompt2': 'Are you involved in any activities in school or in your community? If so, please describe them'
                       ' and what your role in them looks like.'
        }

