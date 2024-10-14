# clairmarais/views.py

from django.shortcuts import render, redirect
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def login(request, user_id):
    user = User.objects.get(id=user_id)
    request.session['user_id'] = user.id
    request.session['user_name'] = user.first_name
    return redirect('home')

def home(request):
    user_name = request.session.get('user_name')
    return render(request, 'home.html', {'user_name': user_name})