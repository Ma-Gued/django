from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clairmarais.models import Event, Poll
from .calculate_countdown_view import calculate_countdown

@login_required
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    polls = Poll.objects.filter(event_id=event_id)
    countdown = calculate_countdown(event.date)

    context = {
        'event': event,
        'days': countdown['days'],
        'hours': countdown['hours'],
        'minutes': countdown['minutes'],
        'seconds': countdown['seconds'],
    }
    return render(request, "event/event_details.html", context)