from django.db.models.signals import post_save
from django.dispatch import receiver
from items.models import Intendance, VoteOption, Poll
from items.signals_dir.meal_signals import create_vote_option_for_meal
from items.signals_dir.intendance_signals import create_vote_option_for_intendance
