from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from clairmarais.models import Event, Poll
from clairmarais.forms.event_create_form import EventCreationForm

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'
