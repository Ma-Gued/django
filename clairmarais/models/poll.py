from django.db import models
from clairmarais.constants import FORM_TYPES
from clairmarais.models import Event

class Poll(models.Model):
    event = models.ForeignKey(Event, related_name='polls', on_delete=models.CASCADE, null=False)
    question = models.CharField(max_length=255)
    form_type = models.CharField(max_length=20, choices=FORM_TYPES, default='emoji')
    vote_options = models.ManyToManyField('VoteOption', related_name='polls')

    def __str__(self):
        return self.question
