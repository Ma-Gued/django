from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        login(request, user)
        return redirect('home')
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_login(request, user_id):
    user = get_object_or_404(User, id=user_id)
    auth_login(request, user)
    return redirect('home')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


