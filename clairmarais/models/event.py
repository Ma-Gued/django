from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField(default=None) #format actuel : 2021-06-01 12:00:00
    #TODO: Ajouter date de début, date de fin
    #TODO: Ajuster le format de la date    
    description = models.TextField()
    address = models.CharField(max_length=255, default="", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
