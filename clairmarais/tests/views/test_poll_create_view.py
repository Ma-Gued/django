from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from clairmarais.models import Event, Poll, VoteOption
from clairmarais.forms.vote_option_creation_form import VoteOptionFormSet
from django.utils.timezone import make_aware 
from datetime import datetime

class PollCreateViewTest(TestCase):
    #TODO: Refacto avec setUpTestData(cls) pour configurer des données de test partagées
    def setUp(self):
        # On met dans le setup les éléments qui sont communs à tous les tests
        # Le client est utilisé pour envoyer des requêtes HTTP aux vues
        # Il représente un utilisateur qui navigue sur le site
        self.client = Client()
        self.user = User.objects.create_user(username='testuser')
        self.client.login(username='testuser')
        self.event = Event.objects.create(
            name="Conférence Django",
            description="Une conférence sur Django",
            created_by=self.user,
            date=make_aware(datetime(2025, 12, 31)),
            address="Rue de la Paix, Paris"
        )
        
        # Test sur la vue PollCreateView (création de sondage)
        def test_post_poll_create_view(self):
            # Définir l'URL de la vue PollCreateView avec l'ID de l'événement
            url = reverse('poll_create', args=[self.event.id])
            
            # Définir les données du formulaire
            data = {
                'question': 'Quel est votre langage de programmation préféré?'
            }
            # Vérifier que le form_type n'est pas 'free_input' (pas de vote_option prédéfinies)
            if 'form_type' != 'free_input':
                data.update({
                    #TODO: explications des lignes suivantes
                    'voteoption_set-TOTAL_FORMS': '1',
                    'voteoption_set-INITIAL_FORMS': '0',
                    'voteoption_set-MIN_NUM_FORMS': '0',
                    'voteoption_set-MAX_NUM_FORMS': '1000',
                    'voteoption_set-0-name': 'Python',
                })
            
            # Envoyer une requête POST à la vue PollCreateView 
            # avec les données du formulaire
            response = self.client.post(url, data)
            
            # Imprimer les erreurs du formulaire et du formset
            if response.status_code == 200:
                print("Form errors:", response.context['form'].errors)
                print("Formset errors:", response.context['vote_option_formset'].errors)


            self.assertEqual(response.status_code, 302)  # Redirection après la création
            self.assertTrue(Poll.objects.filter(question='Quel est votre langage de programmation préféré?').exists())
            self.assertTrue(VoteOption.objects.filter(name='Python').exists())
            print("💪POST request to PollCreateView passed"), VoteOptionFormSet