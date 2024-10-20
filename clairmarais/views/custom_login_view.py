from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import redirect
# CustomLoginView hérite de LoginView (de django.contrib.auth.views)
class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
    