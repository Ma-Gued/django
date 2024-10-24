from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from clairmarais.models import Event
from clairmarais.forms.event_create_form import EventCreationForm

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'event/event_creation_form.html'
    success_url = reverse_lazy('event_list')
    # success_url = reverse_lazy('')  # Redirige vers la liste des événements après la création
    #! je viens d'ajouter success url. 
    #! à la création de l'event, on veut rediriger l'utilisateur vers la liste des events.
    #! et vérifier qu'il s'ajoute à la bdd 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        print(form.instance.created_by)
        print(form)
        return super().form_valid(form)