from django.contrib import admin
from clairmarais.models import VoteOption, UserVote

class VoteOptionAdmin(admin.ModelAdmin):
    list_display = ('get_name',)

    def get_name(self, obj):
        if obj.meal:
            return obj.meal.name
        elif obj.drink:
            print("DRNK")
            return obj.drink.name
        elif obj.intendance:
            return obj.intendance.name
        elif obj.game:
            return obj.game.name
        elif obj.logistic:
            return obj.logistic.name
        elif obj.payment:
            return obj.payment.name
        return 'Unknown'
    get_name.short_description = 'Name'

