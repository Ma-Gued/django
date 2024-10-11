# items/views/home.py
from django.shortcuts import render
from items.models import Poll

def home(request):
    polls = Poll.objects.all()
    #pour utiliser polls dans un template, on doit le passer en contexte:
    return render(request, 'home.html', {'polls': polls})
    # return render(request, 'home.html') 