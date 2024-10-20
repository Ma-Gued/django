from django.db.models.signals import post_save
from django.dispatch import receiver
from clairmarais.models import Intendance, Logistic, VoteOption, Poll, Meal, Drink
from clairmarais.signals_dir.meal_signals import create_vote_option_for_meal
from clairmarais.signals_dir.drink_signals import create_vote_option_for_drink
from clairmarais.signals_dir.intendance_signals import create_vote_option_for_intendance
from clairmarais.signals_dir.logistic_signals import create_vote_option_for_logistic