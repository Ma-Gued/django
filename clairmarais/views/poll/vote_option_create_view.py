from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from clairmarais.models import Poll, VoteOption
from clairmarais.forms.vote_option_creation_form import VoteOptionForm

class VoteOptionCreateView(LoginRequiredMixin, FormView):
    form_class = VoteOptionForm
    template_name = 'polls/vote_option_form.html'

    def form_valid(self, form):
        poll = Poll.objects.get(id=self.kwargs['poll_id'])
        form.instance.poll = poll
        form.instance.user = self.request.user
        form.save()
        return redirect('poll_add_option', poll_id=poll.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = Poll.objects.get(id=self.kwargs['poll_id'])
        context['vote_options'] = VoteOption.objects.filter(poll=context['poll'])
        return context