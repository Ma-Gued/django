from django.contrib import admin
from clairmarais.models import Poll, VoteOption
from clairmarais.forms.forms import PollForm

# Administration des VoteOptions

class VoteAdmin(admin.ModelAdmin):
    form = PollForm