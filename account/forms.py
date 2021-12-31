from django import forms
from account.models import University, Team


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'symbol_name', 'logo']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'university']
