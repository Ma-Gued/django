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
       
    
    return render(request, 'poll_votes.html', {'poll': poll, 'meal_proposals': meal_proposals})
