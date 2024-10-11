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
    print("----------")
    print(VoteOption.objects.all())
    print(vote_options)
    
        # ---------------------------------

    # On récupère les propositions de repas, d'intendance, de jeu et de logistique
    # pour les afficher dans le formulaire de vote
    # meal_proposals = Meal.objects.all()
    # intendance_proposals = Intendance.objects.all() 
    # game_proposals = Game.objects.all()
    # logistic_proposals = Logistic.objects.all()
    
    # proposals = {
        # 'meal': meal_proposals,
        # 'intendance': intendance_proposals,
        # 'game': game_proposals,
        # 'logistic': logistic_proposals
    # }
    
    # if request.method == 'POST':
        # for proposal in proposals:
        #     response = request.POST.get(f'proposal_{proposal.id}')
        #     if response:
        #         UserVote.objects.create(
        #             user=request.user,
        #             poll=poll,
        #             proposal_id=proposal.id,
        #             response=response
        #         )
        # return redirect('poll_results', poll_id=poll.id)
    
    #.get() permet de récupérer la valeur d'une clé dans un dictionnaire
    #poll.category est la clé, et [] est la valeur par défaut si la clé n'existe pas
    #poll.category sera remplacé par meal, intendance, game ou logistic
    # current_proposals = proposals.get(poll.category, [])
    # ---------------------------------
    #
    
    if request.method == 'POST':
        for option in vote_options:
            response = request.POST.get(f'proposal_{option.id}')
            if response:
                UserVote.objects.create(
                    user=request.user,
                    vote_option=option,
                    response=response
                )
        return redirect('poll_results', poll_id=poll.id)

    return render(request, 'poll_votes.html', {'poll': poll, 'vote_options': vote_options})
    # return render(request, 'poll_votes.html', {'poll': poll, 'proposals': current_proposals})
