from django.db.models import TextField
from django.forms import ModelForm, CharField, Textarea, HiddenInput
from django.forms.models import ModelFormMetaclass
from django.forms.utils import ErrorList

from application.models import AcademicFundingApplication, ScholarshipApplication, CustomizableApplication, \
    CustomizableApplicationType
from application.models import Application


class CustomizableApplicationForm(ModelForm):
    class Meta:
        model = CustomizableApplication
        fields = ["text0", "text1", "text2", "text3", "text4"]

    def __init__(self, *args, app_type: CustomizableApplicationType = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_type = app_type
        field_names_to_display: list[str] = [f"text{i}" for i in range(0, app_type.num_text_fields)]
        for field_name, field in self.fields.items():
            if field_name not in field_names_to_display:
                self.fields[field_name] = CharField(max_length=5000, widget=HiddenInput, required=False)

    def save(self, commit=True):
        self.instance.type = self.app_type
        return super().save(commit)


class ApplicationForm(ModelForm):

    class Meta:
        model = Application
        fields = []  # TODO (high priority): Add relevant fields (not sure what yet)


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


class ScholarshipApplicationForm(ApplicationForm):
    class Meta:
        model = ScholarshipApplication
        # TODO (low priority): Make this a call to super() somehow instead of explicitly referencing ApplicationForm
        fields = ApplicationForm.Meta.fields + ["high_school", "statement", "transcript", "recommendation_letter_1",
                                                "recommendation_letter_2", "acknowledged"]
