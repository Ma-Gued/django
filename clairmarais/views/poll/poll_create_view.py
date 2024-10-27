from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from clairmarais.models import Poll, VoteOption
from clairmarais.forms.poll_creation_form import PollCreationForm
from clairmarais.forms.vote_option_creation_form import VoteOptionFormSet

class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollCreationForm
    template_name = 'polls/poll_creation_form.html'

    def get_context_data(self, **kwargs):
        self.object = None
        context = super().get_context_data(**kwargs)
        
        if self.request.method == 'POST':
            context['vote_option_formset'] = VoteOptionFormSet(self.request.POST)
        else:
            if 'add_vote_option' in self.request.GET:
                #TODO: A revoir, ne fonctionne pas 
                #! en fait le problème c'est peut être qu'on ne crée pas le poll avant le submit
                #! donc il n'y a pas de poll_id pour ajouter les voteoptions
                #! il faudrait peut être créer le poll avant de créer les voteoptions
                #! ou alors il faudrait ajouter les voteoptions dans le formulaire de création de poll
                #! et ne pas les ajouter dans un formulaire à part
                formset = VoteOptionFormSet(queryset=VoteOption.objects.none())
                formset.extra += 1  # Ajouter un formulaire supplémentaire
                context['vote_option_formset'] = formset
                # Conserver les données du formulaire principal
                initial_data = {'question': self.request.GET.get('question', '')}
                context['form'] = PollCreationForm(initial=initial_data)
                #rester sur la page de création de poll: 
                return context
            else:
                context['vote_option_formset'] = VoteOptionFormSet()
                context['form'] = PollCreationForm()
        context['event_id'] = self.kwargs['event_id']
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        vote_option_formset = context['vote_option_formset']
        self.object = form.save()
        # Vérifier que les deux formulaires sont valides
        if form.is_valid() and vote_option_formset.is_valid():
            # Enregistrer le poll
            self.object = form.save()
            # Associer les voteoptions au poll
            vote_option_formset.instance = self.object
            # Enregistrer les voteoptions
            vote_option_formset.save()
            
            # Debug: Afficher le poll et les voteoptions dans le terminal
            print("**********POLL*****************")
            print(self.object)
            print("**********voteoptions*****************")
            print(self.object.voteoption_set.all())
            
            # Rediriger vers la page de succès
            return redirect(self.get_success_url())
        else:
            # Si un des deux formulaires n'est pas valide, rediriger vers la page de création de poll
            return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        context = self.get_context_data()
        vote_option_formset = context['vote_option_formset']
        
        if 'add_vote_option' in request.POST:
            # Si le bouton "Ajouter une option de vote" est cliqué
            # On ajoute un formulaire supplémentaire au formset
            vote_option_formset = VoteOptionFormSet(request.POST)
            context['vote_option_formset'] = vote_option_formset
            return self.render_to_response(context)
        
        if form.is_valid() and vote_option_formset.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('event_details', args=[self.kwargs['event_id']])