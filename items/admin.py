from django.contrib import admin
from items.models import Meal, Poll, VoteOption, Intendance
from items.forms.forms import PollForm
from django import forms
from .administration.poll_admin import PollAdmin
from .administration.meal_admin import MealAdmin
from .administration.vote_admin import VoteAdmin
from .administration.intendance_admin import IntendanceAdmin

class VoteOptionInline(admin.TabularInline):
    model = VoteOption
    form = PollForm
    extra = 1
# à quoi sert elle ? 

admin.site.register(Poll, PollAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(VoteOption, VoteAdmin)
admin.site.register(Intendance, IntendanceAdmin)