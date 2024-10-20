from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

# CustomLogoutView hérite de LogoutView (django.contrib.auth.views.LogoutView)
class CustomLogoutView(LogoutView):
    # response est un objet HttpResponse
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect('login')