from django.apps import AppConfig

class ClairmaraisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clairmarais'
    
    def ready(self):
        import clairmarais.signals  