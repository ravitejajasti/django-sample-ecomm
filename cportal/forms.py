from django import forms
from .models import Director, Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'type']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'email']
