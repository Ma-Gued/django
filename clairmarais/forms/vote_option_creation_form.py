from django import forms
from clairmarais.models import Poll, VoteOption

class VoteOptionForm(forms.ModelForm):
    class Meta:
        model = VoteOption
        fields = ['name']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
