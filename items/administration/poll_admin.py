from django.contrib import admin
from items.models import Poll, VoteOption

# Administration du modèle Poll
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'category') 
    fields = ('question', 'category')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        VoteOption.populate_vote_options(obj)


