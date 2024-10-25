from django.shortcuts import render, redirect, get_object_or_404
from clairmarais.models import Poll, VoteOption, Meal, Intendance, Game, UserVote
from django.contrib.auth.decorators import login_required

@login_required
# Cette méthode permet de gérer les options (choix) pour un sondage donné
def poll_votes(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    voteoptions = VoteOption.objects.filter(poll=poll)
    games = Game.objects.all()
    vote_counts = {option.id: UserVote.objects.filter(vote_option=option).count() for option in voteoptions}

    # Si le formulaire est soumis, on enregistre les réponses
    if request.method == 'POST':
        # Les options sont stockées dans un champ de formulaire nommé response_<id>
        for vote in voteoptions:
            response = request.POST.get(f'response_{vote.id}')
            if response:
                vote.response = response
                vote.save()
        return redirect('poll_success')

    # Rendu de la page de détails du sondage avec les options de vote
    return render(request, 'poll_votes.html', {'poll': poll, 'votes': voteoptions, 'games': games})
