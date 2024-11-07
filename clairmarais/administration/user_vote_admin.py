from django.contrib import admin
from clairmarais.models import UserVote

# Administration du modèle UserVote
class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_vote_option', 'response')
    search_fields = ('user__username', 'vote_option__name', 'response')

    def get_vote_option(self, obj):
        return obj.vote_option.name 
    get_vote_option.short_description = 'Vote Option'
