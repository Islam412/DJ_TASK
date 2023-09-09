from django import forms
from .models import Answer


class AnswerForms(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']