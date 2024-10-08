from django.shortcuts import render
from items.models import Poll
from items.models import Vote

def poll_view(request):
    # Récupérer le premier sondage
    poll = Poll.objects.first() 
    # Récupérer les propositions de repas du sondage
    meal_proposals = poll.meal_set.all()
    # Renvoyer le sondage à la template
    
    # if request.method == "POST":
    #     # Logique pour gérer le vote
    #     for meal in meal_proposals:
    #         vote_value = request.POST.get(str(meal.id))  # Récupère la valeur du vote
    #         if vote_value:
    #             Vote.objects.create(poll=poll, meal=meal, value=vote_value)
                
    return render(request, 'poll.html', {'poll': poll})