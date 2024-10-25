from django import forms
from clairmarais.models import Poll, VoteOption
from django.forms.models import inlineformset_factory

class VoteOptionForm(forms.ModelForm):
    class Meta:
        model = VoteOption
        fields = ['name']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

VoteOptionFormSet = inlineformset_factory(Poll, VoteOption, form=VoteOptionForm, extra=1, can_delete=True)