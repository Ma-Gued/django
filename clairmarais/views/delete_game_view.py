from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from clairmarais.models import Game

@login_required

def delete_game(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, id=game_id)
        poll_id = request.GET.get('poll_id')
        print("---------------------------", poll_id)
        if game.user == request.user:
            game.delete()
            return redirect('poll_votes', poll_id=poll_id)
    return redirect('poll_votes', poll_id=poll_id)