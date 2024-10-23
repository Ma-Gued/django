from django.shortcuts import get_object_or_404, redirect
from django.db import IntegrityError
from clairmarais.models import Poll, VoteOption, UserVote
from django.urls import reverse


def handle_poll_interactions(request, poll_id, template_prefix):
    poll = get_object_or_404(Poll, id=poll_id)
    user = request.user
    vote_options = VoteOption.objects.filter(poll=poll)
    
    alert = None
    user_votes_dict = {}
    if request.method == 'POST':
        if 'add_option' in request.POST:
            new_option_name = request.POST.get('new_option')
            if new_option_name:
                # Créer la nouvelle VoteOption
                vote_option = VoteOption.objects.create(name=new_option_name, user=user)
                # Ajouter la nouvelle VoteOption au sondage
                vote_option.poll = poll
                vote_option.save()
        elif 'delete_option' in request.POST:
            option_id = request.POST.get('delete_option')
            VoteOption.objects.filter(id=option_id, user=user).delete()
        else:
            for option in vote_options:
                response = request.POST.get(f'proposal_{option.id}')
                if response:
                    try:
                        user_vote, created = UserVote.objects.get_or_create(
                            user=user,
                            vote_option=option,
                            defaults={'response': response}
                        )
                        if not created:
                            user_vote.response = response
                            user_vote.save()
                    except IntegrityError:
                        alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'
        return redirect(reverse('poll_details', args=[poll_id]))
    
    
    # {% if user_votes_dict|get_item:option.id == emoji %}checked{% endif %}>

    user_votes = UserVote.objects.filter(vote_option__in=vote_options)
    user_votes_dict = {option.id: [] for option in vote_options}
    for vote in user_votes:
        user_votes_dict[vote.vote_option.id].append({'user': vote.user.username, 'response': vote.response})
        print(vote.user)  
        
    print("2>>>", user_votes_dict)

    emojis = ['🤮', '🤐', '😋'] if poll.form_type == 'emoji' else []
 
    # Récupérer les utilisateurs pour chaque option de vote
    option_users_dict = {}
    for option in vote_options:
        user_votes_for_option = UserVote.objects.filter(vote_option=option)
        option_users_dict[option.id] = {
            'oui': [vote.user.username for vote in user_votes_for_option if vote.response == 'oui'],
            'non': [vote.user.username for vote in user_votes_for_option if vote.response == 'non']
        }
   
    template_name = f'form_types/{poll.form_type}_{template_prefix}.html'
    # pour utiliser template_name dans un template, on utilise cette syntaxe: 
    
    return {
        'poll': poll,
        'vote_options': vote_options,
        'option_users_dict': option_users_dict,
        'user_votes_dict': user_votes_dict,
        'alert': alert,
        'template_name': template_name,
        'emojis': emojis,
    }