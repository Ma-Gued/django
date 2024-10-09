from django.db import models
from django.contrib.auth.models import User
from .poll import Poll
from .meal import Meal
from .game import Game
from .logistic import Logistic

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, null=True, blank=True, on_delete=models.CASCADE)
      
    # def __str__(self):
        # Cette def permet de retourner un message lorsqu'on fait un print de l'objet, uniquement pour le debug
        # return f"{self.user} voted {self.rating} for {self.meal} in {self.poll}"

