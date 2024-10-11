from django.contrib import admin
from clairmarais.models import UserVote

# Administration du modèle UserVote
class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_vote_option', 'response')
    search_fields = ('user__username', 'vote_option__meal__name', 'vote_option__intendance__name', 'vote_option__game__name', 'vote_option__logistic__name', 'response')

    def get_vote_option(self, obj):
        return str(obj.vote_option)
    get_vote_option.admin_order_field = 'vote_option'
    get_vote_option.short_description = 'Vote Option'
