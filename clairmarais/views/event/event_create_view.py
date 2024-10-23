from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from clairmarais.models import Event
from clairmarais.forms.event_create_form import EventCreationForm

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'events/event_creation_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)