from django.shortcuts import render, get_object_or_404, redirect
from clairmarais.models import Poll, VoteOption, UserVote, Game
from django.contrib.auth.models import User
from django.db import IntegrityError

def poll_details(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

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

    games = Game.objects.filter(user=request.user)
    alert = None

    # Récupérer l'utilisateur connecté à partir de la session
    user_id = request.session.get('user_id')
    if not user_id:
        # Rediriger vers la liste des utilisateurs si aucun utilisateur n'est connecté
        return redirect('user_list')  

    user = get_object_or_404(User, id=user_id)

    # Récupérer les votes existants de l'utilisateur pour ce sondage
    user_votes = UserVote.objects.filter(user=user, vote_option__in=vote_options)
    user_votes_dict = {vote.vote_option.id: vote.response for vote in user_votes}

    return render(request, 'poll_votes.html', {
        'poll': poll,
        'vote_options': vote_options,
        'user_votes_dict': user_votes_dict,
        'games': games,
        'alert': alert
    })