from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from clairmarais.models import Poll, VoteOption, UserVote, Game
from django.contrib.auth.models import User
from django.db import IntegrityError

@login_required
def poll_details(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    
    user = request.user

    # Récupérer les options de vote pour ce sondage
    if poll.category == 'intendance':
        vote_options = VoteOption.objects.filter(poll=poll, intendance__isnull=False)
    elif poll.category == 'meal':
        vote_options = VoteOption.objects.filter(poll=poll, meal__isnull=False)
    elif poll.category == 'game':
        vote_options = VoteOption.objects.filter(poll=poll, game__isnull=False)
    elif poll.category == 'logistic':
        return redirect('logistic', poll_id=poll.id)        
    else:
        vote_options = VoteOption.objects.filter(poll=poll)
    
    alert = None
    
    # Récupérer les votes de l'utilisateur pour les options de vote de ce sondage   
    user_votes = UserVote.objects.filter(vote_option__in=vote_options)

        # Récupérer les utilisateurs pour chaque option de vote
    option_users_dict = {}
    for option in vote_options:
        user_votes_for_option = UserVote.objects.filter(vote_option=option)
        option_users_dict[option.id] = {
            'oui': [vote.user.username for vote in user_votes_for_option if vote.response == 'oui'],
            'non': [vote.user.username for vote in user_votes_for_option if vote.response == 'non']
        }
    # Créer un dictionnaire des votes de l'utilisateur pour chaque option de vote
    user_votes_dict = {vote.vote_option.id: vote.response for vote in user_votes}

    # Enregistrer les votes de l'utilisateur
    if request.method == 'POST':
        for option in vote_options:
            response = request.POST.get(f'proposal_{option.id}')
            if response:
                try:
                    # Vérifier si un vote existe déjà pour cet utilisateur et cette option de vote
                    user_vote, created = UserVote.objects.get_or_create(
                        user=user,
                        vote_option=option,
                        defaults={'response': response}
                    )
                    if not created:
                        # Si le vote existe déjà, mettre à jour la réponse
                        user_vote.response = response
                        user_vote.save()
                except IntegrityError:
                    alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'
        return redirect('poll_details', poll_id=poll.id)
    
    games = Game.objects.all()

    return render(request, 'poll_votes.html', {
        'poll': poll,
        'vote_options': vote_options,
        'user_votes_dict': user_votes_dict,
        'option_users_dict': option_users_dict,
        'alert': alert,
        'games': games, 
        'current_user': user, 
    })