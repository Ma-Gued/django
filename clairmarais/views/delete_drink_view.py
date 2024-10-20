
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from clairmarais.models import Drink

@login_required
def delete_drink(request, drink_id):
    print('delete_drink')
    if request.method == 'POST':
        drink = get_object_or_404(Drink, id=drink_id)
        poll_id = request.GET.get('poll_id')
        if drink.user == request.user:
            print("on arrive dans if drink.user == request.user")
            drink.delete()
            return redirect('poll_details', poll_id=poll_id)
    return redirect('poll_votes', poll_id=poll_id)