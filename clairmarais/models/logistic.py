# logistic.py
from django.db import models
from .item_to_bring import ItemToBring

class Logistic(ItemToBring):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name