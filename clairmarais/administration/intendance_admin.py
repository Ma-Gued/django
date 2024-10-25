from django.contrib import admin
from clairmarais.models import Intendance, UserVote

# Administration du modèle Intendance
class IntendanceAdmin(admin.ModelAdmin):
        list_display = ('name', 'get_dislike_count', 'get_like_count')

        def get_dislike_count(self, obj):
            return UserVote.objects.filter(vote_option__intendance=obj, response='oui').count()
        get_dislike_count.short_description = 'Dislike Votes'

        def get_like_count(self, obj):
            return UserVote.objects.filter(vote_option__intendance=obj, response='non').count()
        get_like_count.short_description = 'Like Votes'