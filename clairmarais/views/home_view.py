# clairmarais/views/home.py
from django.shortcuts import render
from clairmarais.models import Poll
from django.contrib.auth.models import User

def home(request):
    polls = Poll.objects.all()
    users = User.objects.all()
    #Etant donné sur le modèle user a un attribut username avec django.contrib.auth.models.User, 
    #on peut récupérer l'objet de l'utilisateur:
    username = User.objects.get(id=request.session.get('user_id'))
    
    #et donc on envoie le username à la page home.html, ainsi que les polls, 
    return render(request, 'home.html', {'polls': polls, 'username': username, 'users': users})