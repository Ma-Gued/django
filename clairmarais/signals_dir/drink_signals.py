from django.db.models.signals import post_save
from django.dispatch import receiver
from clairmarais.models import Drink, VoteOption, Poll

@receiver(post_save, sender=Drink)
def create_vote_option_for_drink(sender, instance, created, **kwargs):
    if created:
        # Récupérer le poll correspondant
        poll = Poll.objects.filter(category='drink').first()
        if poll:
            VoteOption.objects.create(poll=poll, drink=instance)