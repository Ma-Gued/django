from django.shortcuts import get_object_or_404, redirect
from django.db import IntegrityError
from clairmarais.models import Poll, VoteOption, UserVote
from django.urls import reverse
from clairmarais.utils.post_condition_handler_view import post_condition_handler
from clairmarais.utils.user_votes_dict import get_user_votes_dict
from clairmarais.utils.option_users_dict import get_option_users_dict
from clairmarais.utils.vote_choices import get_vote_choices

def handle_poll_interactions(request, event_id, poll_id, template_prefix):
    poll = get_object_or_404(Poll, id=poll_id, event_id=event_id)
    user = request.user
    vote_options = VoteOption.objects.filter(poll=poll)
    alert = None
    # Récupérer les votes des utilisateurs
    user_votes_dict = get_user_votes_dict(vote_options)

    # Gérer les interactions de l'utilisateur avec le sondage
    # (Vote, ajout d'une option, suppression d'une option)
    if request.method == 'POST':
        alert, should_redirect = post_condition_handler(request, poll_id, user, poll, vote_options)
        if should_redirect:
            return redirect(reverse('poll_details', args=[event_id, poll_id]))

 
    # Récupérer les utilisateurs ayant voté "oui" ou "non" pour chaque option de vote
    option_users_dict = get_option_users_dict(vote_options)
    # Obtenir les choix de vote en fonction du type de formulaire (emoji, oui/non)
    vote_choices = get_vote_choices(poll)

   # Définir le form (template) à utiliser
    template_name = f'form_types/{poll.form_type}_{template_prefix}.html'
    context = {
        'poll': poll,
        'vote_options': vote_options,
        'user_votes_dict': user_votes_dict,
        'option_users_dict': option_users_dict,
        'vote_choices': vote_choices,
        'alert': alert,
        'template_name': template_name,        
    }
    return context