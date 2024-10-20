from django.db.models.signals import post_save
from django.dispatch import receiver
from clairmarais.models import Payment, VoteOption, Poll

@receiver(post_save, sender=Payment)
def create_vote_option_for_payment(sender, instance, created, **kwargs):
    if created:
        # Récupérer le poll correspondant
        poll = Poll.objects.filter(category='payment').first()
        if poll:
            VoteOption.objects.create(poll=poll, payment=instance)