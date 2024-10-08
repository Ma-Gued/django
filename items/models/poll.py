from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=255)
    meals = models.ManyToManyField('Meal', through='Vote')

    def __str__(self):
        return self.question