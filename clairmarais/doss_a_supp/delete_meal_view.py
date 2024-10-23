
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from clairmarais.models import Meal

@login_required
def delete_meal(request, meal_id):
    print('delete_meal')
    if request.method == 'POST':
        meal = get_object_or_404(Meal, id=meal_id)
        poll_id = request.GET.get('poll_id')
        if meal.user == request.user:
            print("on arrive dans if meal.user == request.user")
            meal.delete()
            return redirect('poll_details', poll_id=poll_id)
    return redirect('poll_votes', poll_id=poll_id)