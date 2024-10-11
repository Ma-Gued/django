from django.db.models.signals import post_save
from django.dispatch import receiver
from items.models import Meal, VoteOption, Poll

@receiver(post_save, sender=Meal)
def create_vote_option_for_meal(sender, instance, created, **kwargs):
    if created:
        # Récupérer le poll correspondant
        poll = Poll.objects.filter(category='meal').first()
        if poll:
            VoteOption.objects.create(poll=poll, meal=instance)