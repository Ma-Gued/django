from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from clairmarais.models import Poll, VoteOption
from clairmarais.forms.poll_creation_form import PollCreationForm
from clairmarais.forms.vote_option_creation_form import VoteOptionForm

class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollCreationForm
    template_name = 'polls/poll_creation_form.html'

    def get_context_data(self, **kwargs):
        # Obtenir le contexte de la vue parent 
        data = super().get_context_data(**kwargs)
        
        # Initialiser le formulaire d'option de vote
        if self.request.POST:
            data['vote_option_form'] = VoteOptionForm(self.request.POST)
        else:
            data['vote_option_form'] = VoteOptionForm()
        
        # Ajouter l'ID de l'événement au contexte
        data['event_id'] = self.kwargs['event_id']
        
        # Si un sondage existe déjà, ajouter les options de vote existantes au contexte
        if 'poll_id' in self.kwargs:
            poll = get_object_or_404(Poll, id=self.kwargs['poll_id'])
            data['poll'] = poll
            data['vote_options'] = poll.vote_options.all()
        else:
            data['vote_options'] = []
        
        # Debug: Afficher le contexte dans le terminal
        print("Context Data:", data)
        
        return data
    
    # Fonction pour ajouter un sondage et une option de vote
    def form_valid(self, form):
        # Obtenir le contexte de la vue
        context = self.get_context_data()
        vote_option_form = context['vote_option_form']
        print("Vote Option Form:", vote_option_form)
        
        # Assigner l'utilisateur et l'événement au sondage
        form.instance.created_by = self.request.user
        form.instance.event_id = self.kwargs['event_id']
        
        # Si un sondage existe déjà, le récupérer, sinon le créer
        if 'poll_id' in self.kwargs:
            self.object = get_object_or_404(Poll, id=self.kwargs['poll_id'])
            print("Poll Object:", self.object)
        else:
            self.object = form.save()
        
        # Debug: Afficher le sondage dans le terminal
        print("Poll Object:", self.object)
        
        # Si le formulaire d'option de vote est valide, créer l'option de vote
        if vote_option_form.is_valid():
            vote_option = vote_option_form.save(commit=False)
            vote_option.poll = self.object
            vote_option.user = self.request.user
            vote_option.save()
            
            # Debug: Afficher l'option de vote dans le terminal
            print("Vote Option:", vote_option)
            
            # Effacer le contenu de l'input pour ajouter un nouveau vote option
            vote_option_form = VoteOptionForm()
        
        # Recharger la page avec les nouvelles données
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        # Rediriger vers la page de création du sondage avec l'ID de l'événement et du sondage
        return reverse('poll_create', args=[self.kwargs['event_id'], self.object.id])
    
    #!OBJECTIF : comprendre le fonctionnement de la création de sondage et d'option de vote
    #! Vérifier l'enregistrement en base de données de la création du poll, ainsi que des vote_options