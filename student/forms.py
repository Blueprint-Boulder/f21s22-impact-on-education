from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group

from students.models import ScholarshipApplication

class ScholarshipForm(forms.Form):
    
    class Meta:
        model = ScholarshipApplication
        fields = ("first_name","last_name","email_address","address","phone_number","school_choice","statement","transcript","recommendation_letter_1","recommendation_letter_2","acknowledged")
    
    def save(self, commit=True):
        user: CustomUser = super().save(commit=False)
        if commit:
            user.save()
            user.account_type = self.cleaned_data["account_type"]
            user.save()
        return user
