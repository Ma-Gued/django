from django.db import models
from .item_to_bring import ItemToBring
from django.contrib.auth.models import User

class Game(ItemToBring):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name