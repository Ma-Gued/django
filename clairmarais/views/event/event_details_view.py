from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from clairmarais.models import Event

class EventDetailsView(LoginRequiredMixin, DetailView):
    model = Event
    print(model)

    template_name = 'event/event_details.html'
    context_object_name = 'event'
