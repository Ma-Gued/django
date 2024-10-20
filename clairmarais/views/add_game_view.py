from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from clairmarais.models import Game, Poll, VoteOption, UserVote
# login required 
from django.contrib.auth.decorators import login_required

@login_required
def add_game(request):

    if request.method == 'POST':
        game_name = request.POST.get('game_name')
        poll_id = request.POST.get('poll_id')
        user_id = request.POST.get('user_id')
        poll = get_object_or_404(Poll, id=poll_id)
        user = request.user
        game = Game.objects.create(name=game_name, user=user)
        vote_option = VoteOption.objects.create(poll=poll, game=game)
        UserVote.objects.create(user=user, vote_option=vote_option)
        # Redirige vers la page de votes du sondage
        return redirect('poll_votes', poll_id=poll_id)
    # Affiche le formulaire d'ajout de jeu  
    poll_id = request.GET.get('poll_id')
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'add_game.html', {'poll': poll})