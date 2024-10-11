from django.contrib import admin
from items.models import Poll, Vote
from items.forms.forms import PollForm

# Administration des votes

class VoteAdmin(admin.ModelAdmin):
    form = PollForm