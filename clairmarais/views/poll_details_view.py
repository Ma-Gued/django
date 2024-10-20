from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from clairmarais.models import Poll, VoteOption, UserVote, Game, Meal, Drink
from django.contrib.auth.models import User

@login_required
def poll_details(request, poll_id):
    # Récupérer le sondage
    poll = get_object_or_404(Poll, id=poll_id)
    
    user = request.user
    
    # Récupérer les options de vote en fonction de la catégorie du sondage
    if poll.category == 'intendance':
        vote_options = VoteOption.objects.filter(poll=poll, intendance__isnull=False)
    elif poll.category == 'meal':
        vote_options = VoteOption.objects.filter(poll=poll, meal__isnull=False)
    elif poll.category == 'drink':
        vote_options = VoteOption.objects.filter(poll=poll, drink__isnull=False)
    elif poll.category == 'game':
        vote_options = VoteOption.objects.filter(poll=poll, game__isnull=False)
    elif poll.category == 'logistic':
        return redirect('logistic', poll_id=poll.id)        
    else:
        vote_options = VoteOption.objects.filter(poll=poll)
    
    alert = None

    if request.method == 'POST':
        delete_meal_id = request.POST.get('delete_meal')
        if delete_meal_id:
            try:
                delete_meal_id = int(delete_meal_id)
                meal = get_object_or_404(Meal, id=delete_meal_id)
                if meal.user == user:
                    meal.delete()
                    return redirect('poll_details', poll_id=poll.id)
            except ValueError:
                alert = 'Invalid meal ID.'
                
        delete_drink_id = request.POST.get('delete_drink')
        if delete_drink_id:
            try:
                delete_drink_id = int(delete_drink_id)
                drink = get_object_or_404(Drink, id=delete_drink_id)
                if drink.user == user:
                    drink.delete()
                    return redirect('poll_details', poll_id=poll.id)
            except ValueError:
                alert = 'Invalid drink ID.'

        # Enregistrer les votes pour les options de vote
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
                except IntegrityError:
                    alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'
        
        # Enregistrer les votes pour les repas
        meal_vote_options = VoteOption.objects.filter(poll=poll, meal__isnull=False)
        for meal_vote_option in meal_vote_options:
            response = request.POST.get(f'proposal_{meal_vote_option.meal.id}')
            if response:
                try:
                    user_vote, created = UserVote.objects.get_or_create(
                        user=user,
                        vote_option=meal_vote_option,
                        defaults={'response': response}
                    )
                    if not created:
                        user_vote.response = response
                        user_vote.save()
                except IntegrityError:
                    alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'
        
        # Enregistrer les votes pour les boissons
        drink_vote_options = VoteOption.objects.filter(poll=poll, drink__isnull=False)
        for drink_vote_option in drink_vote_options:
            response = request.POST.get(f'proposal_{drink_vote_option.drink.id}')
            if response:
                try:
                    user_vote, created = UserVote.objects.get_or_create(
                        user=user,
                        vote_option=drink_vote_option,
                        defaults={'response': response}
                    )
                    if not created:
                        user_vote.response = response
                        user_vote.save()
                except IntegrityError:
                    alert = 'Une erreur est survenue lors de la mise à jour de votre vote.'
                    
        return redirect('poll_details', poll_id=poll.id)
    
    # Récupérer les votes de l'utilisateur pour les options de vote
    user_votes = UserVote.objects.filter(user=user, vote_option__in=vote_options)
    user_votes_dict = {vote.vote_option.id: vote.response for vote in user_votes}
    
    # Récupérer les votes de l'utilisateur pour les repas
    meal_vote_options = VoteOption.objects.filter(poll=poll, meal__isnull=False)
    meal_votes = UserVote.objects.filter(user=user, vote_option__in=meal_vote_options)
    meal_votes_dict = {vote.vote_option.id: vote.response for vote in meal_votes}
    
    # print(drink)
    # Récupérer les votes de l'utilisateur pour les boissons
    drink_vote_options = VoteOption.objects.filter(poll=poll, drink__isnull=False)
    drink_votes = UserVote.objects.filter(user=user, vote_option__in=drink_vote_options)
    drink_votes_dict = {vote.vote_option.id: vote.response for vote in drink_votes}
    
    # Récupérer les utilisateurs pour chaque option de vote
    option_users_dict = {}
    for option in vote_options:
        user_votes_for_option = UserVote.objects.filter(vote_option=option)
        option_users_dict[option.id] = {
            'oui': [vote.user.username for vote in user_votes_for_option if vote.response == 'oui'],
            'non': [vote.user.username for vote in user_votes_for_option if vote.response == 'non']
        }

    # Récupérer les jeux associés au sondage
    games = Game.objects.all()
    
    # Récupérer les repas via les options de vote
    meals = [vote_option.meal for vote_option in meal_vote_options]
    drinks = [vote_option.drink for vote_option in drink_vote_options]
    
    return render(request, 'poll_votes.html', {
        'poll': poll,
        'vote_options': vote_options,
        'user_votes_dict': user_votes_dict,
        'option_users_dict': option_users_dict,
        'meal_votes_dict': meal_votes_dict,
        'alert': alert,
        'games': games, 
        'meals': meals,
        'current_user': user,
        'drinks': drinks,
        'drink_votes_dict': drink_votes_dict
    })