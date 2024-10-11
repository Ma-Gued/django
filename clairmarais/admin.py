from django.contrib import admin
from clairmarais.models import Meal, Poll, VoteOption, Intendance, Game, Logistic, UserVote
from clairmarais.forms.forms import PollForm
from django import forms
from .administration.poll_admin import PollAdmin
from .administration.meal_admin import MealAdmin
from .administration.vote_admin import VoteAdmin
from .administration.game_admin import GameAdmin
# from .administration.logistic_admin import LogisticAdmin
from .administration.user_vote_admin import UserVoteAdmin
from .administration.intendance_admin import IntendanceAdmin

class VoteOptionInline(admin.TabularInline):
    model = VoteOption
    form = PollForm
    extra = 1

admin.site.register(Poll, PollAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(VoteOption, VoteAdmin)
admin.site.register(Intendance, IntendanceAdmin)
admin.site.register(Game)
admin.site.register(Logistic)
admin.site.register(UserVote, UserVoteAdmin)