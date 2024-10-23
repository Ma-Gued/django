from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from clairmarais.models import Event

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
