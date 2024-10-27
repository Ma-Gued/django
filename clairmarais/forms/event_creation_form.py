from django import forms
from clairmarais.models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'address']
        #TODO: Ajuster en fonction des modifications apportées au modèle Event