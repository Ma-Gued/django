from django.contrib import admin
from items.models import Poll, VoteOption
from items.forms.forms import PollForm

# Administration des VoteOptions

class VoteAdmin(admin.ModelAdmin):
    form = PollForm