from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clairmarais.models import Poll, Event

@login_required
def home(request):
    polls = Poll.objects.all()
    users = User.objects.all()
    events = Event.objects.all()
    username = User.objects.get(id=request.user.id).username

    context = {
        'polls': polls,
        'users': users,
        'events': events,
        'username': username,
        
    }

    return render(request, 'home.html', context)