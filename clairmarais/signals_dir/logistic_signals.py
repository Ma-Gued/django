from django.db.models.signals import post_save
from django.dispatch import receiver
from clairmarais.models import Logistic, VoteOption, Poll

@receiver(post_save, sender=Logistic)
def create_vote_option_for_logistic(sender, instance, created, **kwargs):
    if created:
        # Récupérer le poll correspondant
        poll = Poll.objects.filter(category='logistic').first()
        if poll:
            VoteOption.objects.create(poll=poll, logistic=instance)