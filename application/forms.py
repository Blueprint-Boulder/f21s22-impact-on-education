from django.forms import ModelForm

from application.models import AcademicFundingApplication, ScholarshipApplication, VolunteerApplication, \
    CollegeApplication  # , PersonalInfo
from application.models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['author','address', 'phone_number', 'work_employer', 'work_position', 'work_description', 'work_years',
                  'work_hours', 'volunteer_employer', 'volunteer_position', 'volunteer_description',
                  'volunteer_years', 'volunteer_hours', 'org_name', 'org_role', 'org_description',
                  'org_years', 'org_hours']
        labels = {
            'author': 'Enter your name (First Middle Last).',
            'address': 'Enter your address.',
            'phone_number': 'Enter your phone number.',
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

