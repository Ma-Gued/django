from django.db.models.signals import post_save
from django.dispatch import receiver
from items.models import Intendance, VoteOption, Poll

@receiver(post_save, sender=Intendance)
def create_vote_option_for_intendance(sender, instance, created, **kwargs):
    if created:
        # Récupérer le poll correspondant
        poll = Poll.objects.filter(category='intendance').first()
        if poll:
            VoteOption.objects.create(poll=poll, intendance=instance)