from django.db import models
from .poll import Poll
from .meal import Meal
from .intendance import Intendance
from .game import Game
from .logistic import Logistic
from .drink import Drink

class VoteOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', null=True, blank=True, on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', null=True, blank=True, on_delete=models.CASCADE)
    intendance = models.ForeignKey('Intendance', null=True, blank=True, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', null=True, blank=True, on_delete=models.CASCADE)
    logistic = models.ForeignKey('Logistic', null=True, blank=True, on_delete=models.CASCADE)
      
    def __str__(self):
        if self.meal:
            return self.meal.name
        elif self.drink:
            return self.drink.name
        elif self.intendance:
            return self.intendance.name
        elif self.game:
            return self.game.name
        elif self.logistic:
            return self.logistic.name
        return "Vote Option"
    
    # Création des options de vote pour un sondage
    @staticmethod
    def populate_vote_options(poll):
        if poll.category == 'meal':
            meals = Meal.objects.all()
            for meal in meals:
                VoteOption.objects.create(poll=poll, meal=meal)
        elif poll.category == 'drink':
            drinks = Drink.objects.all()
            for drink in drinks:
                VoteOption.objects.create(poll=poll, drink=drink)
        elif poll.category == 'intendance':
            intendances = Intendance.objects.all()
            for intendance in intendances:
                VoteOption.objects.create(poll=poll, intendance=intendance)
        elif poll.category == 'game':
            games = Game.objects.all()
            for game in games:
                VoteOption.objects.create(poll=poll, game=game)
        elif poll.category == 'logistic':
            logistics = Logistic.objects.all()
            for logistic in logistics:
                VoteOption.objects.create(poll=poll, logistic=logistic)
