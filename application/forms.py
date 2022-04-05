from django.forms import ModelForm

from application.models import AcademicFundingApplication, ScholarshipApplication, VolunteerApplication, \
    CollegeApplication, PersonalInfo
from application.models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = []

class PersonalInfo(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ApplicationForm.Meta.fields + ['work_employer', 'work_position', 'work_description', 'work_years',
                  'work_hours', 'volunteer_employer', 'volunteer_position', 'volunteer_description',
                  'volunteer_years', 'volunteer_hours', 'org_name', 'org_role', 'org_description',
                  'org_years', 'org_hours']
        labels = {
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
        fields = ApplicationForm.Meta.fields + ['email', 'name', 'school', 'role', 'department',
                                                'viability_and_usability', 'emergency_services', 'medical_needs',
                                                'internet_needs', 'academic_needs', 'needs_assistance', 'funding_for',
                                                'funding_need', 'funding_amount', 'students_impacted', 'agreement']
        labels = {
            'email': 'Enter Your Email',
            'name': 'Enter Your Name',
            'school': 'Enter Your School',
            'role': 'What is your role in your BVSD school?',
            'department': 'If you answered Educator or Other in the previous question, what department and/or grade level are you a member of?',
            'viability_and_usability': 'If you answered "Educator" or "Other" in the previous question, have you confirmed the viability and usability of your request with your supervisor or principal?',
            'emergency_services': 'If your student(s) need involves emergency services, such as food, housing, clothing, or health, have you already reviewed the English Community Resources document here: https://www.bvsd.org/parents-students/student-help/mckinney-vento/community-resources? And, if appropriate, have you reached out to the most aligned organizations on that document?',
            'medical_needs': 'If your student(s) need is medical in nature, have you contacted Kristina Hyde at 720-561-5571 or kristina.hyde@bvsd.org or Maggie Salgado at 720-561-5474 or maggie.salgado@bvsd.org with the BVSD Medicaid Health Program?',
            'internet_needs': 'If your student(s) need involves internet access, technology or computers, have you contacted BVSD IT for assistance?',
            'academic_needs': 'What area of academic need does your request involve?',
            'needs_assistance': 'Who needs the assistance you are requesting (no student names please)?',
            # TODO (high priority): Handle "uploading any documentation" for 'funding_for'
            'funding_for': 'What are you requesting funding for? Please be as specific as you can, and if you need to upload any documentation, please do so. If a purchase is being made, please include a link to the item being purchased.',
            'funding_need': 'What is the need your request is addressing? Why is the funding needed?',
            'funding_amount': 'How much funding are you requesting?',
            'students_impacted': 'Approximately how many students does your request impact?',
            'agreement': 'Do you agree to provide quantitative, qualitative, and/or anecdotal post-data should your Academic Opportunity Fund request be approved?'
        }

class VolunteerApplicationForm(ApplicationForm):
    class Meta:
        model = VolunteerApplication
        fields = ApplicationForm.Meta.fields + ['position', 'availability', 'community_service', 'alignment', 'soft_skills']
        labels = {
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
        labels = {
            'major': 'Enter the major you are applying for.',
            'challenge': 'Describe a time where you had to try and overcome a challenge. Were you successful? What did you gain from the experience?',
            'extracurricular': 'Describe any extracurricular activities you have been involved with during high school. Please describe your role and the hours spent per week.',
            'passions': 'Describe one of your passions.'
        }


class ScholarshipApplicationForm(ApplicationForm):
    class Meta:
        model = ScholarshipApplication
        # TODO (low priority): Make this a call to super() somehow instead of explicitly referencing ApplicationForm
        fields = ApplicationForm.Meta.fields + ["high_school", "statement", "transcript", "recommendation_letter_1",
                                                "recommendation_letter_2", "acknowledged"]
