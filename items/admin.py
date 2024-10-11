from django.contrib import admin
from items.models import Meal, Poll, Vote, Intendance
from items.forms.forms import PollForm
from django import forms

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass

class VoteInline(admin.TabularInline):
    model = Vote
    form = PollForm
    extra = 1

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')  # Afficher la catégorie dans l'admin
    fields = ('question', 'category')  # Inclure le champ category dans le formulaire


admin.site.register(Poll, PollAdmin)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    form = PollForm

admin.site.register(Intendance)
