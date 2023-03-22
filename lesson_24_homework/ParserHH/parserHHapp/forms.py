from django import forms
from django.forms import BaseFormSet

from parserHHapp.models import Area, Schedule


class ReqForm(forms.Form):
    vacancy = forms.CharField(label='Строка поиска ', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Введите вакансию'}))
    where = forms.ChoiceField(label='Где искать ', choices=[('all', "Везде"),
                                                            ('company', 'В названии компании'),
                                                            ('name', 'В названии вакансии')],
                              widget=forms.Select(attrs={'class': 'form-control'}))
    pages = forms.IntegerField(label='Количество анализируемых страниц ', initial=3,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserReqForm(forms.Form):
    vacancy = forms.CharField(label='Строка поиска ', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Введите вакансию'}))
    where = forms.ChoiceField(label='Где искать ', choices=[('all', "Везде"),
                                                            ('company', 'В названии компании'),
                                                            ('name', 'В названии вакансии')],
                              widget=forms.Select(attrs={'class': 'form-control'}))
    pages = forms.IntegerField(label='Количество анализируемых страниц ', initial=3,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


class AuthUserReqForm(UserReqForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(),
                                           widget=forms.CheckboxSelectMultiple(
                                               attrs={'class': 'form-check-inline'}), label='Регион')
    schedules = forms.ModelMultipleChoiceField(queryset=Schedule.objects.all(),
                                               widget=forms.CheckboxSelectMultiple(
                                                   attrs={'class': 'form-check-inline'}), label='Занятость')
