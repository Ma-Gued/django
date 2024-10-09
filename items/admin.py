from django.contrib import admin
from items.models import *


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass 

@admin.register(Poll)
class MealAdmin(admin.ModelAdmin):
    pass

# TabularInline est une classe de Django qui permet de gérer les formulaires de type tabulaire (tableau)
class VoteInline(admin.TabularInline):
    # model permet de définir le modèle sur lequel on va travailler
    #model et extra sont des paramètres de la classe TabularInline
    model = Vote
    # extra permet de définir le nombre de formulaire à afficher
    extra = 1  

class PollAdmin(admin.ModelAdmin):
    # [VoteInline] est une liste d'objets de type VoteInline
    inlines = [VoteInline]
    list_display = ('question',)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass

