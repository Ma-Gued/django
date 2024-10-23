from django import forms
from clairmarais.models import Poll
from clairmarais.constants import FORM_TYPES

class PollCreationForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'form_type']
        
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'form_type': forms.Select(choices=FORM_TYPES, attrs={'class': 'form-control'}),
        }