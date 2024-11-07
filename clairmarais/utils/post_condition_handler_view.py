from django.shortcuts import redirect
from django.urls import reverse
from django.db import IntegrityError
from clairmarais.models import VoteOption, UserVote

def post_condition_handler(request, poll_id, user, poll, vote_options):
    alert = None
    should_redirect = False

    if request.method == 'POST':
        if 'add_option' in request.POST:
            new_option_name = request.POST.get('new_option')
            if new_option_name:
                # Créer la nouvelle VoteOption
                vote_option = VoteOption.objects.create(name=new_option_name, user=user)
                # Ajouter la nouvelle VoteOption au sondage
                vote_option.poll = poll
                vote_option.save()
                vote_options = VoteOption.objects.filter(poll=poll)
                should_redirect = True

        elif 'delete_option' in request.POST:
            option_id = request.POST.get('delete_option')
            VoteOption.objects.filter(id=option_id, user=user).delete()
            should_redirect = True
        
        else:
            for option in vote_options:
                response = request.POST.get(f'proposal_{option.id}')
                if response:
                    try:
                        user_vote, created = UserVote.objects.get_or_create(
                            user=user,
                            vote_option=option,
                            defaults={'response': response}
                        )
                        if not created:
                            user_vote.response = response
                            user_vote.save()
                        should_redirect = True
                    except IntegrityError:
                        alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'

    return alert, should_redirect