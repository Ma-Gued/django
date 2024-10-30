from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from clairmarais.views.utils import handle_poll_interactions
from clairmarais.models import Poll, VoteOption
from clairmarais.forms.vote_option_creation_form import VoteOptionFormSet
from clairmarais.utils.vote_choices import get_vote_choices

# Vue pour afficher les détails d'un sondage et gérer les votes des utilisateurs
@login_required
def poll_details(request, event_id, poll_id):
    poll = get_object_or_404(Poll, id=poll_id, event_id=event_id)
    vote_option_formset = VoteOptionFormSet(queryset=VoteOption.objects.filter(poll=poll))
    form_type = poll.form_type
    vote_options = VoteOption.objects.filter(poll=poll)
    vote_choices = get_vote_choices(poll)

    context = {
        'event_id': event_id,
        'poll': poll,
        'vote_options': vote_options,
        'vote_option_formset': vote_option_formset,
        'form_type': form_type,
        'vote_choices': vote_choices,
        'poll_id': poll_id,
        'event_id': event_id,
    }
    return render(request, "polls/poll_structure.html", context)