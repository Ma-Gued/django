from django.contrib import admin
from clairmarais.models import Drink, UserVote

# Administration du modèle Drink
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_dislike_count', 'get_neutral_count', 'get_like_count')

    def get_dislike_count(self, obj):
        return UserVote.objects.filter(vote_option__drink=obj, response='🤮').count()
    get_dislike_count.short_description = 'Dislike Votes'

    def get_neutral_count(self, obj):
        return UserVote.objects.filter(vote_option__drink=obj, response='🤐').count()
    get_neutral_count.short_description = 'Neutral Votes'

    def get_like_count(self, obj):
        return UserVote.objects.filter(vote_option__drink=obj, response='😋').count()
    get_like_count.short_description = 'Like Votes'