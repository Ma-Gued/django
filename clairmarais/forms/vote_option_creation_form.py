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

# VoteOptionFormSet est un formset de VoteOptionForm, càd un ensemble de formulaires VoteOptionForm
# Il permet de gérer plusieurs formulaires VoteOptionForm dans un seul formulaire
# extra=1 signifie qu'il y a un formulaire vide supplémentaire (en plus des formulaires remplis)
# Quand on ajoute unv vote_option, on clique sur un bouton pour ajouter un formulaire vide
# Ce bouton doit être traité dans la vue pour ajouter un formulaire VoteOptionForm, 
# en particulier dans la méthode get_context_data
# quand on clique sur le bouton, on envoie une requête POST avec un paramètre supplémentaire
# qui indique qu'on veut ajouter un formulaire vide
# Les voteoption seront enregistrés dans la bdd quand on cliquera sur le bouton submit du formulaire, 
# qui par rapport au bouton d'ajout de voteoption, n'a pas de paramètre supplémentaire
VoteOptionFormSet = inlineformset_factory(Poll, VoteOption, form=VoteOptionForm, extra=1, can_delete=True)