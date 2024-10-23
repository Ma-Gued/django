from django.contrib import admin
from clairmarais.models import Poll, VoteOption
from clairmarais.administration.vote_option_admin import VoteOptionInline
from clairmarais.forms.forms import PollForm

# Administration du modèle Poll
class PollAdmin(admin.ModelAdmin):
    form = PollForm
    list_display = ('question', 'form_type')
    list_filter = ('form_type',)
    search_fields = ('question',)
    inlines = [VoteOptionInline]  
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if 'vote_options' in form.cleaned_data:
            obj.vote_options.add(*form.cleaned_data['vote_options'])


