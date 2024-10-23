from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clairmarais.views.utils import handle_poll_interactions

# Vue pour afficher les détails d'un sondage et gérer les votes des utilisateurs
@login_required
def poll_details(request, poll_id):
    context = handle_poll_interactions(request, poll_id, 'form')
    return render(request, "poll_structure.html", context)