from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import make_aware
from datetime import datetime
from clairmarais.models import Event, Poll, VoteOption

class ModelRelationsTest(TestCase):
    def setUp(self):
        # Créer un utilisateur pour les tests
        self.user = User.objects.create_user(username='testuser',)
        # Créer un événement
        self.event = Event.objects.create(
            name="Conférence Django",
            description="Une conférence sur Django",
            created_by=self.user,
            date=make_aware(datetime(2025, 12, 31)),
            address="Rue de la Paix, Paris"
        )
        # Créer un sondage lié à l'événement
        self.poll = Poll.objects.create(
            question="Quel est votre langage de programmation préféré?",
            event=self.event,
            # Créer des options de vote liées au sondage et sauvegardez-les
            form_type='emoji',
        )
        # Créer des options de vote pour le sondage
        self.vote_option1 = VoteOption.objects.create(
            name="Python",
            user=self.user,
            poll=self.poll
        )
        # Créer une autre option de vote pour le sondage
        self.vote_option2 = VoteOption.objects.create(
            name="Autre",
            user=self.user,
            poll=self.poll
        )
        

    def test_event_poll_relation(self):
        # Vérifier que le sondage est lié à l'événement
        self.assertEqual(self.poll.event, self.event, "Le sondage n'est pas correctement lié à l'événement.")
        # Vérifier que l'événement contient le sondage
        self.assertIn(self.poll, self.event.polls.all(), "L'événement ne contient pas le sondage.")
    def test_poll_vote_option_relation(self):
        self.assertEqual(self.vote_option1.poll, self.poll, "L'option de vote 'Python' n'est pas correctement liée au sondage.")
        self.assertEqual(self.vote_option2.poll, self.poll, "L'option de vote 'Autre' n'est pas correctement liée au sondage.")
        # Vérifier que le sondage contient les options de vote
        self.assertIn(self.vote_option1, self.poll.poll_vote_options.all(), "Le sondage ne contient pas l'option de vote 'Python'.")
        print("💪test_poll_vote_option_relation passed")