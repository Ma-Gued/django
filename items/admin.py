from django.contrib import admin
from items.models.meal import Meal
from items.models.logistic import Logistic
from items.models.game import Game
from items.models.item_to_bring import ItemToBring

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass 