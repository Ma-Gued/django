from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.forms import inlineformset_factory
from clairmarais.models import Poll, VoteOption, Event
from django.forms.models import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from clairmarais.forms.poll_creation_form import PollCreationForm
from clairmarais.forms.vote_option_creation_form import VoteOptionForm, VoteOptionFormSet

class PollCreateView(LoginRequiredMixin, CreateView):
    
    model = Poll
    form_class = PollCreationForm
    template_name = 'polls/poll_creation_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll_id'] = self.kwargs['poll_id']
        context['event_id'] = self.kwargs['event_id']
        context['form'] = PollCreationForm()
        context['vote_option_formset'] = VoteOptionFormSet(queryset=VoteOption.objects.none())
        #imprimer le type de request: 
        print(self.request)
        return context

    def post(self, request, *args, **kwargs):
        form = PollCreationForm(self.request.POST)
        VoteOptionFormSet = inlineformset_factory(Poll, VoteOption, form=VoteOptionForm, extra=1, can_delete=True)
        vote_option_formset = VoteOptionFormSet(request.POST)
        
        if 'add_vote_option_formset' in self.request.POST:
            print("KIKOU")
            # Nombre de formulaires d'options de vote supplémentaires à afficher
            extra_forms = vote_option_formset.total_form_count() + 1
            # Créer un nouveau formulaire avec une option de vote supplémentaire: 
            VoteOptionFormSet = inlineformset_factory(Poll, VoteOption, form=VoteOptionForm, extra=extra_forms, can_delete=True)
            vote_option_formset = VoteOptionFormSet(queryset=VoteOption.objects.none())            # print("vote_option_formset---------", vote_option_formset)
            context = {
                'form': form,
                'vote_option_formset': vote_option_formset,
                'event_id': self.kwargs['event_id'],
            }
            return self.render_to_response(context)

        if form.is_valid() and vote_option_formset.is_valid():
            poll = form.save(commit=False)
            # Associer l'événement au sondage
            poll.event = Event.objects.get(id=self.kwargs['event_id']) 
            poll.save()
            vote_options = vote_option_formset.save(commit=False)
            for vote_option in vote_options:
                vote_option.poll = poll
                vote_option.save()
            return redirect(reverse('poll_details', args=[self.kwargs['event_id'], poll.id]))
        context = {
            'form': form,
            'vote_option_formset': vote_option_formset,
            'event_id': self.kwargs['event_id'],
        }
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('event_details', args=[self.kwargs['event_id']])