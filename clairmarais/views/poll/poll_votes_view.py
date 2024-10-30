from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clairmarais.views.utils import handle_poll_interactions

# Vue pour gérer les votes sur un sondage
@login_required
def poll_votes(request, event_id, poll_id):
    context = handle_poll_interactions(request, event_id, poll_id, 'form')
    if isinstance(context, dict):
        return render(request, context['template_name'], context)
    return context
