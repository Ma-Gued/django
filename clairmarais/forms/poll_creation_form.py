from django import forms
from clairmarais.models import Poll, VoteOption
from clairmarais.constants import FORM_TYPES

class PollCreationForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'form_type']
        #Les widgets dans Django sont utilisés pour définir la façon 
        # dont les champs de formulaire sont affichés.
        # Ils permettent la personnalisations des champs de formulaire, 
        # dans leur apparence et leur comportement.
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'form_type': forms.Select(choices=FORM_TYPES, attrs={'class': 'form-control'}),
        }
        