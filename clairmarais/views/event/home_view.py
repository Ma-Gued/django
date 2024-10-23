from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clairmarais.models import Poll
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from .calculate_countdown_view import calculate_countdown

@login_required
def home(request):
    polls = Poll.objects.all()
    users = User.objects.all()
    #Le modèle user a un attribut username avec django.contrib.auth.models.User, 
    username = User.objects.get(id=request.user.id).username

    countdown = calculate_countdown()

    context = {
        'days': countdown['days'],
        'hours': countdown['hours'],
        'minutes': countdown['minutes'],
        'seconds': countdown['seconds'],
        'polls': polls,
        'users': users,
        'username': username,
    }

    return render(request, 'home.html', context)