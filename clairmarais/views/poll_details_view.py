from django.shortcuts import render, get_object_or_404, redirect
from clairmarais.models import Poll, VoteOption, UserVote, User
from django.db import IntegrityError

def poll_details(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    vote_options = VoteOption.objects.filter(poll=poll)
    alert = None

    # Récupérer l'utilisateur connecté à partir de la session
    user_id = request.session.get('user_id')
    if not user_id:
        # Rediriger vers la liste des utilisateurs si aucun utilisateur n'est connecté
        return redirect('user_list')  

    user = get_object_or_404(User, id=user_id)

    # Récupérer les votes existants de l'utilisateur pour ce sondage
    user_votes = UserVote.objects.filter(user=user, vote_option__in=vote_options)
    user_votes_dict = {vote.vote_option.id: vote.response for vote in user_votes}

    # Si le formulaire est soumis, enregistrer les réponses
    if request.method == 'POST':
        for option in vote_options:
            response = request.POST.get(f'proposal_{option.id}')
            if response:
                try:
                    # Vérifier si un vote existe déjà pour cet utilisateur et cette option de vote
                    user_vote, created = UserVote.objects.get_or_create(
                        user=user,
                        vote_option=option,
                        defaults={'response': response}
                    )
                    if not created:
                        # Si le vote existe déjà, mettre à jour la réponse
                        user_vote.response = response
                        user_vote.save()
                except IntegrityError:
                    alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'

        alert = 'Ton vote a bien été pris en compte 👌'

    # Rendu de la page de détails du sondage avec les options de vote
    return render(request, 'poll_votes.html', {
        'poll': poll,
        'vote_options': vote_options,
        'user_votes_dict': user_votes_dict,
        'alert': alert
    })