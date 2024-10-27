from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from clairmarais.views.utils import handle_poll_interactions
from clairmarais.models import Poll

# Vue pour afficher les détails d'un sondage et gérer les votes des utilisateurs
@login_required
def poll_details(request, event_id, poll_id):
    poll = get_object_or_404(Poll, id=poll_id, event_id=event_id)
    context = {
        'poll': poll,
        # Ajoutez d'autres contextes nécessaires ici
    }
    return render(request, "poll_structure.html", context)