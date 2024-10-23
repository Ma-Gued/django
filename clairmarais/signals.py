from django.db.models.signals import post_save
from django.dispatch import receiver
from clairmarais.models import VoteOption, Poll

# Fonction générique pour créer des options de vote en fonction du type de formulaire
def create_vote_options(poll):
    pass


# Signal pour créer des options de vote après la création d'un sondage
@receiver(post_save, sender=Poll)
def create_vote_options_for_poll(sender, instance, created, **kwargs):
    if created:
        create_vote_options(instance)