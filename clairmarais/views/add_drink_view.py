from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from clairmarais.models import Drink, Poll, VoteOption, UserVote
from django.contrib.auth.decorators import login_required

@login_required
def add_drink(request):

    if request.method == 'POST':
        drink_name = request.POST.get('drink_name')
        poll_id = request.POST.get('poll_id')
        user_id = request.POST.get('user_id')
        poll = get_object_or_404(Poll, id=poll_id)
        user = request.user
        drink = Drink.objects.create(name=drink_name, user=user)
        # Redirige vers la page de votes du sondage
        return redirect('poll_details', poll_id=poll_id)
    # Affiche le formulaire d'ajout de jeu  
    poll_id = request.GET.get('poll_id')
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'add_drink.html', {'poll': poll}, {'user': user})