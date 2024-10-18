from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clairmarais.models import Poll
from django.contrib.auth.models import User

def home(request):
    polls = Poll.objects.all()
    users = User.objects.all()
    #Le modèle user a un attribut username avec django.contrib.auth.models.User, 
    username = User.objects.get(id=request.user.id).username

    return render(request, 'home.html', {'polls': polls, 'username': username, 'users': users})