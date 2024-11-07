from django.test import TestCase
from django.contrib.auth.models import User
from clairmarais.models import Event
from django.utils.timezone import make_aware
from datetime import datetime
class EventModelTest(TestCase):
    def setUp(self):
        # Cette méthode est appelée avant chaque test, 
        # pour configurer l'environnement de test.
        # On crée un utilisateur pour l'associer à l'événement
        self.user = User.objects.create_user(username='testuser',)
    
    def test_event_creation(self):
        # Créer un événement avec les détails spécifiés
        event = Event.objects.create(
            name="Conférence Django",  # Nom de l'événement
            description="Une conférence sur Django",  # Description de l'événement
            created_by=self.user,  # Utilisateur qui a créé l'événement
            date=make_aware(datetime(2025, 12, 31)),  # Date de l'événement
            address="Rue de la Paix, Paris"  # Adresse de l'événement
        )
        # Vérifier que l'événement a été créé
        self.assertIsNotNone(event.id, "L'événement n'a pas été créé correctement.")

        
        # Vérifier que l'événement a été créé avec le nom spécifié
        self.assertEqual(event.name, "Conférence Django", "Le nom de l'événement ne correspond pas.")
        # Vérifier que l'événement a été créé avec la description spécifiée
        self.assertEqual(event.description, "Une conférence sur Django", "La description de l'événement ne correspond pas.")
        # Vérifier que l'événement a été créé par l'utilisateur spécifié
        self.assertEqual(event.created_by.username, 'testuser', "L'utilisateur qui a créé l'événement ne correspond pas.")
        # Vérifier que l'événement a été créé avec la date spécifiée
        self.assertEqual(event.date, make_aware(datetime(2025, 12, 31)), "La date de l'événement ne correspond pas.")    
        # Vérifier que l'événement a été créé avec l'adresse spécifiée
        self.assertEqual(event.address, "Rue de la Paix, Paris", "L'adresse de l'événement ne correspond pas.") 
    
        # Supprimez l'événement
        event.delete()
        # Vérifier que l'événement a été supprimé de la base de données
        self.assertEqual(Event.objects.count(), 0)
        
        print("💪 test_event_creation_passed")