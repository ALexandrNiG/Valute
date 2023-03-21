from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Applicant
from parserHHapp.models import Area, Schedule


class RegForm(UserCreationForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), widget=forms.CheckboxSelectMultiple())
    schedules = forms.ModelMultipleChoiceField(queryset=Schedule.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Applicant
        fields = ['username', 'password1', 'password2', 'email']
