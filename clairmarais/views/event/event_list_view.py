from django.shortcuts import render
from django.views.generic import ListView
from clairmarais.models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'