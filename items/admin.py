from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Affiche ces champs dans la liste
    search_fields = ('name',)  # Ajoute une barre de recherche pour le champ 'name'
    ordering = ('name',)  # Trie les éléments par 'name' par défaut
    list_filter = ('description',)  # Ajoute un filtre pour le champ 'description'

    # Si tu veux ajouter des fonctionnalités supplémentaires, comme des champs personnalisés dans le formulaire
    fieldsets = (
        (None, {
            'fields': ('name', 'description'),
        }),
    )
