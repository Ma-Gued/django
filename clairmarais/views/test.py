from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from clairmarais.models import Poll, VoteOption, UserVote

def add_vote_option(request):

    if request.method == 'POST':
        vote_option_name = request.POST.get('vote_option_name')
        poll_id = request.POST.get('poll_id')
        print("poll_id:", poll_id)
        user_id = request.POST.get('user_id')
        poll = get_object_or_404(Poll, id=poll_id)
        user = request.user
        vote_option = VoteOption.objects.create(poll=poll, name=vote_option_name)
        UserVote.objects.create(user=user, vote_option=vote_option)
        # Redirige au même endroit : 
        return redirect('poll_create_with_id', event_id=poll.event.id, poll_id=poll.id)
    # Affiche le formulaire d'ajout de jeu  
    poll_id = request.GET.get('poll_id')
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll_creation_form.html', {'poll': poll})