from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from clairmarais.models import Poll
from clairmarais.forms.poll_creation_form import PollCreationForm

class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollCreationForm
    template_name = 'polls/poll_creation_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.event_id = self.kwargs['event_id']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('event_details', args=[self.object.event.id])