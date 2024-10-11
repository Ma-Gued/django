from django.shortcuts import render, redirect, get_object_or_404
from items.models import Poll, VoteOption, Meal, Intendance, Game, Logistic

def poll_details(request, poll_id):
    # get_object_or_404 est une fonction qui permet de récupérer un objet en fonction de son ID 
    # et de renvoyer une erreur 404 si l'objet n'existe pas
    poll = get_object_or_404(Poll, id=poll_id)
    
    # On récupère les propositions de repas, d'intendance, de jeu et de logistique
    # pour les afficher dans le formulaire de vote
    meal_proposals = Meal.objects.all()
    intendance_proposals = Intendance.objects.all() 
    game_proposals = Game.objects.all()
    logistic_proposals = Logistic.objects.all()
    
    proposals = {
        'meal': meal_proposals,
        'intendance': intendance_proposals,
        'game': game_proposals,
        'logistic': logistic_proposals
    }
    
    #.get() permet de récupérer la valeur d'une clé dans un dictionnaire
    #poll.category est la clé, et [] est la valeur par défaut si la clé n'existe pas
    #poll.category sera remplacé par meal, intendance, game ou logistic
    current_proposals = proposals.get(poll.category, [])
    return render(request, 'poll_votes.html', {'poll': poll, 'proposals': current_proposals})
