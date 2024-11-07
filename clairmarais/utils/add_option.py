from clairmarais.models import VoteOption

def add_option(request, user, poll):
    new_option_name = request.POST.get('new_option')
    if new_option_name:
        # Créer la nouvelle VoteOption
        vote_option = VoteOption.objects.create(name=new_option_name, user=user)
        # Ajouter la nouvelle VoteOption au sondage
        vote_option.poll = poll
        vote_option.save()
        vote_options = VoteOption.objects.filter(poll=poll)
    should_redirect = True