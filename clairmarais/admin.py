from django.contrib import admin
from clairmarais.models import Meal, Poll, VoteOption, Intendance, Game, Logistic, UserVote, Drink, Payment
from clairmarais.forms.forms import PollForm
from .administration.poll_admin import PollAdmin
from .administration.meal_admin import MealAdmin
from .administration.vote_admin import VoteAdmin
from .administration.game_admin import GameAdmin
from .administration.drink_admin import DrinkAdmin
from .administration.payment_admin import PaymentAdmin
# from .administration.logistic_admin import LogisticAdmin
from .administration.user_vote_admin import UserVoteAdmin
from .administration.intendance_admin import IntendanceAdmin
from .administration.vote_option_admin import VoteOptionAdmin

class VoteOptionInline(admin.TabularInline):
    model = VoteOption
    form = PollForm
    extra = 1

admin.site.register(Poll, PollAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Intendance, IntendanceAdmin)
admin.site.register(Game)
admin.site.register(Logistic)
admin.site.register(UserVote, UserVoteAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(VoteOption, VoteOptionAdmin)