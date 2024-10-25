from django import forms
from clairmarais.models import Poll, VoteOption
from clairmarais.constants import FORM_TYPES
from django.forms.models import inlineformset_factory
from clairmarais.forms.vote_option_creation_form import VoteOptionFormSet

class PollCreationForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'form_type']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'form_type': forms.Select(choices=FORM_TYPES, attrs={'class': 'form-control'}),
        }

