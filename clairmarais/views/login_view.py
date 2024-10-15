from django.shortcuts import render, redirect
from django.contrib.auth.models import User

#D'abord, on crée une vue pour afficher la liste des utilisateurs
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# Puis 
def login(request, user_id):
    user = User.objects.get(id=user_id)
    request.session['user_id'] = user.id
    request.session['user_name'] = user.first_name
    # vérifier que l'utilisateur choisi est connecté : 
    return redirect('home')