from django.shortcuts import render, redirect, get_object_or_404
from clairmarais.models import Game, Poll 
from django.contrib.auth.models import User


def add_game(request):
    if request.method == 'POST':
        game_name = request.POST.get('game_name')
        poll_id = request.POST.get('poll_id')
        print("---------------------------", poll_id)
        user_id = request.session.get('user_id')
        poll = get_object_or_404(Poll, id=poll_id)
        user = User.objects.get(id=user_id)
        Game.objects.create(name=game_name, user=user)
        # Redirige vers la page de votes du sondage
        return redirect('poll_votes', poll_id=poll_id)
    # Affiche le formulaire d'ajout de jeu  
    poll_id = request.GET.get('poll_id')
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'add_game.html', {'poll': poll})