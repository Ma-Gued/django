from django.contrib import admin
from clairmarais.models import Payment, UserVote

# Administration du modèle Payment
class PaymentAdmin(admin.ModelAdmin):
        list_display = ('name', 'get_dislike_count', 'get_neutral_count', 'get_like_count')

        def get_dislike_count(self, obj):
            return UserVote.objects.filter(vote_option__payment=obj, response='❌').count()
        get_dislike_count.short_description = 'Dislike Votes'

        def get_neutral_count(self, obj):
            return UserVote.objects.filter(vote_option__payment=obj, response='🤐').count()
        get_neutral_count.short_description = 'Neutral Votes'

        def get_like_count(self, obj):
            return UserVote.objects.filter(vote_option__payment=obj, response='✅').count()
        get_like_count.short_description = 'Like Votes'