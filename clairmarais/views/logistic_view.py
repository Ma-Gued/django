from django.shortcuts import render, get_object_or_404, redirect
from clairmarais.models import Poll, VoteOption, UserVote

def logistic(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    user = request.user
    
    # Récupérer les options de vote pour la catégorie logistic
    logistic_vote_options = VoteOption.objects.filter(poll=poll, poll__category='logistic')

    # Récupérer les votes de tous les utilisateurs pour ce poll
    logistic_user_votes = UserVote.objects.filter(vote_option__in=logistic_vote_options)
    
    # Séparer les options de vote non sélectionnées et sélectionnées
    selected_options = {vote.vote_option.id: vote.user.username for vote in logistic_user_votes}
    unselected_options = [option for option in logistic_vote_options if option.id not in selected_options]
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action:
            action_parts = action.split('_')
            if len(action_parts) == 2:
                action_type, vote_option_id = action_parts
                if action_type == 'add':
                    vote_option = get_object_or_404(VoteOption, id=vote_option_id)
                    UserVote.objects.create(user=user, vote_option=vote_option, response="Je ramène")
                elif action_type == 'remove':
                    vote_option = get_object_or_404(VoteOption, id=vote_option_id)
                    UserVote.objects.filter(user=user, vote_option=vote_option).delete()
        
        # Rediriger après le traitement du formulaire POST
        return redirect('logistic', poll_id=poll.id)

    context = {
        'poll': poll,
        'selected_options': selected_options,
        'unselected_options': unselected_options,
        'logistic_vote_options': {option.id: option for option in logistic_vote_options},
        'user': user
    }
    return render(request, 'poll_votes/logistic.html', context)