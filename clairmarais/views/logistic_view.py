from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from clairmarais.models import Poll, VoteOption, UserVote
from django.contrib.auth.models import User

@login_required
def logistic(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    user = request.user
    
    # Récupérer les options de vote pour la catégorie logistic
    logistic_vote_options = VoteOption.objects.filter(poll__category='logistic')

    # Récupérer les votes de tous les utilisateurs pour ce poll
    logistic_user_votes = UserVote.objects.filter(user=user, vote_option__in=logistic_vote_options)
    
    # Séparer les options de vote non sélectionnées et sélectionnées
    selected_options = {vote.vote_option.id: vote.user.username for vote in logistic_user_votes}
    # dans le template, on récupèrera le name de 'logistic' de cette façon: logistic_user_votes.0.vote_option.name
    unselected_options = [option for option in logistic_vote_options if option.id not in selected_options]
    
    if request.method == 'POST':
        vote_option_id = request.POST.get('vote_option_id')
        vote_option = get_object_or_404(VoteOption, id=vote_option_id)
        
        action = request.POST.get('action', 'add')

        if action == 'add':
            UserVote.objects.create(user=user, vote_option=vote_option, response="Je ramène")
        elif action == 'remove':
            UserVote.objects.filter(user=user, vote_option=vote_option).delete()
        
        return redirect('poll_details', poll_id=poll.id)

    return render(request, 'poll_votes/logistic.html', {
        'poll': poll, 
        'selected_options': selected_options,
        'unselected_options': unselected_options,
        'logistic_vote_options': {option.id: option for option in logistic_vote_options}, 
        'user': user
        })