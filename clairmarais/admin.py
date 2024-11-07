from django.contrib import admin
from clairmarais.models import Poll, VoteOption, UserVote
from clairmarais.forms.forms import PollCreationForm
from .administration.poll_admin import PollAdmin
from .administration.user_vote_admin import UserVoteAdmin
from .administration.vote_option_admin import VoteOptionInline

admin.site.register(Poll, PollAdmin)
admin.site.register(UserVote, UserVoteAdmin)

