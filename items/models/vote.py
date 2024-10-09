from django.db import models
from django.contrib.auth.models import User
from items.models import Poll, Meal

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, null=True, blank=True, on_delete=models.CASCADE)
      
    def __str__(self):
        return f"{self.meal.name} - {self.poll.question}"