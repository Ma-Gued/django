from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from items.models import Poll, VoteOption, Meal, Intendance, Game, Logistic, UserVote

@login_required
def poll_details(request, poll_id):
    # get_object_or_404 est une fonction qui permet de récupérer un objet en fonction de son ID 
    # et de renvoyer une erreur 404 si l'objet n'existe pas
    poll = get_object_or_404(Poll, id=poll_id)
    vote_options = VoteOption.objects.filter(poll=poll)
    alert = ''
    
    if request.method == 'POST':
        for option in vote_options:
            response = request.POST.get(f'proposal_{option.id}')
            if response:
                UserVote.objects.create(
                    user=request.user,
                    vote_option=option,
                    response=response
                )
        alert = 'Votre vote a bien été pris en compte'
        
    return render(request, 'poll_votes.html', {'poll': poll, 'vote_options': vote_options, 'alert': alert})