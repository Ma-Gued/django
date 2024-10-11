from django.contrib import admin
from items.models import Meal, Poll, Vote, Intendance
from items.forms.forms import PollForm
from django import forms
# à rectifier

class IntendanceAdmin(admin.ModelAdmin):
    pass