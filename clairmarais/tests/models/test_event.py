from django.test import TestCase
from django.contrib.auth.models import User
from clairmarais.models import Event

class EventModelTest(TestCase):
    def setUp(self):
        # Cette méthode est appelée avant chaque test. 
        # Elle est utilisée pour configurer l'environnement de test.
        # Créez un utilisateur pour l'associer à l'événement
        self.user = User.objects.create_user(username='testuser',)
    
    def test_event_creation(self):
        # Créez un événement avec les détails spécifiés
        event = Event.objects.create(
            name="Conférence Django",  # Nom de l'événement
            description="Une conférence sur Django",  # Description de l'événement
            created_by=self.user,  # Utilisateur qui a créé l'événement
            date="2025-12-31",  # Date de l'événement
            address="Rue de la Paix, Paris"  # Adresse de l'événement
        )
        # Vérifiez que l'événement a été créé avec le nom spécifié
        self.assertEqual(event.name, "Conférence Django")
        # Vérifiez que l'événement a été créé avec la description spécifiée
        self.assertEqual(event.description, "Une conférence sur Django")
        # Vérifiez que l'événement a été créé par l'utilisateur spécifié
        self.assertEqual(event.created_by.username, 'testuser')
        # Vérifiez que l'événement a été créé avec la date spécifiée
        self.assertEqual(event.date, "2025-12-31")
        # Vérifiez que l'événement a été créé avec l'adresse spécifiée
        self.assertEqual(event.address, "Rue de la Paix, Paris")
    
        # Supprimez l'événement
        event.delete()
        # Vérifiez que l'événement a été supprimé de la base de données
        self.assertEqual(Event.objects.count(), 0)