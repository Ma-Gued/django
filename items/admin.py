from django.contrib import admin
from items.models.meal import Meal
from items.models.logistic import Logistic
from items.models.game import Game
from items.models.item_to_bring import ItemToBring
from items.models.poll import Poll
from items.models.vote import Vote


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass 

@admin.register(Poll)
class MealAdmin(admin.ModelAdmin):
    pass

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll', 'meal', 'rating')