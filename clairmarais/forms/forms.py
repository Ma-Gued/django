from django import forms
from clairmarais.models import Poll, VoteOption, Meal, Intendance, Game

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'category']
        

    category = forms.ChoiceField(
        choices=[
            ('meal', 'Meal'),
            ('intendance', 'Intendance'),
            ('game', 'Game'),
            ('logistic', 'Logistic'),
        ],
        label="Choose Category"
    )