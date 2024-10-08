from django.db import models
from django.contrib.auth.models import User
from .poll import Poll
from .meal import Meal
from .game import Game
from .logistic import Logistic

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, null=True, blank=True, on_delete=models.CASCADE)
    # game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE)
    # logistic = models.ForeignKey(Logistic, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        # Pour éviter que le même utilisateur vote plusieurs fois sur le même sondage
        unique_together = (('poll', 'user'),)  

    def __str__(self):
        # Cette def permet de retourner un message lorsqu'on fait un print de l'objet, uniquement pour le debug
        return f"{self.user} voted in {self.poll}"
