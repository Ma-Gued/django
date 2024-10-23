from django.db import models
from clairmarais.constants import FORM_TYPES

class Poll(models.Model):

    question = models.CharField(max_length=255)
    form_type = models.CharField(max_length=20, choices=FORM_TYPES, default='meal')
    vote_options = models.ManyToManyField('VoteOption', related_name='polls')

    def __str__(self):
        return self.question
