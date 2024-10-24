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
    # success_url = reverse_lazy('event_list') est utilisé pour rediriger l'utilisateur
    # vers la liste des événements après la création d'un événement.
    # reverse_lazy est utilisé ici car il est évalué à l'exécution, 
    # ce qui permet de retarder la résolution de l'URL jusqu'à ce que l'objet Event soit créé.
    # Cela évite les problèmes de redirection prématurée.
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        print(form)
        return super().form_valid(form)