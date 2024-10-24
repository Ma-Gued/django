from django import forms
from clairmarais.models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description']