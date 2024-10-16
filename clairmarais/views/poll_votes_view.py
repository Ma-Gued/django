from django.shortcuts import render, redirect, get_object_or_404
from clairmarais.models import Poll, VoteOption, Meal, Intendance, Game

# Cette méthode permet de gérer les options (choix) pour un sondage donné
def poll_votes(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    voteoptions = VoteOption.objects.filter(poll=poll)
    games = Game.objects.all()

    # Si le formulaire est soumis, on enregistre les réponses
    if request.method == 'POST':
        # Les options sont stockées dans un champ de formulaire nommé response_<id>
        for vote in voteoptions:
            response = request.POST.get(f'response_{vote.id}')
            if response:
                vote.response = response
                vote.save()
        return redirect('poll_success')

    return render(request, 'poll_votes.html', {'poll': poll, 'votes': voteoptions, 'games': games})
