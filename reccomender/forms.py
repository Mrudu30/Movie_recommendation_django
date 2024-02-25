# forms.py
from django import forms
from .models import Genre,Language,Movie

class GenreFilterForm(forms.Form):
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class LanguageFilterForm(forms.Form):
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )