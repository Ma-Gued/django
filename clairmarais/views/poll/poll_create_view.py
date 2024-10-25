from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from clairmarais.models import Poll
from clairmarais.forms.poll_creation_form import PollCreationForm
from clairmarais.forms.vote_option_creation_form import VoteOptionFormSet

class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollCreationForm
    template_name = 'polls/poll_creation_form.html'

    def get_context_data(self, **kwargs):
        # Obtenir le contexte de la vue parent
        data = super().get_context_data(**kwargs)
        
        # Initialiser le formset des options de vote
        if self.request.POST:
            data['vote_option_formset'] = VoteOptionFormSet(self.request.POST, instance=self.object)
        else:
            data['vote_option_formset'] = VoteOptionFormSet(instance=self.object)
        
        # Ajouter l'ID de l'événement au contexte
        data['event_id'] = self.kwargs['event_id']
        
        # Debug: Afficher le contexte dans le terminal
        print("Context Data:", data)
        
        return data

    def form_valid(self, form):
        # Obtenir le contexte de la vue
        context = self.get_context_data()
        vote_option_formset = context['vote_option_formset']
        
        # Assigner l'utilisateur et l'événement au sondage
        form.instance.created_by = self.request.user
        form.instance.event_id = self.kwargs['event_id']
        
        # Sauvegarder le sondage
        self.object = form.save()
        
        # Debug: Afficher le sondage dans le terminal
        print("Poll Object:", self.object)
        
        # Si le formset des options de vote est valide, sauvegarder les options de vote
        if vote_option_formset.is_valid():
            vote_option_formset.instance = self.object
            vote_option_formset.save()
            
            # Debug: Afficher les options de vote dans le terminal
            print("Vote Options:", vote_option_formset.cleaned_data)
        
        # Rediriger vers la page de détail de l'événement
        return redirect(self.get_success_url())

    def get_success_url(self):
        # Rediriger vers la page de détail de l'événement
        return reverse('event_details', args=[self.kwargs['event_id']])