from django.db import models
from .item_to_bring import ItemToBring

class Meal(ItemToBring):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#La classe Meal est une sous-classe de ItemToBring, elle hérite de ses attributs et méthodes, et peut en redéfinir ou en ajouter de nouveaux.
#Dans ce projet, les utilisateurs vont pouvoir voter pour les repas qu'ils préfèrent, et les repas les plus populaires seront préparés.
#Des propositions de repas seront créées via l'admin de Django 
#Pour cela, nous allons ajouter un attribut votes à la classe Meal, qui contiendra le nombre de votes pour chaque repas.
#Une classe "VoteOption" 
