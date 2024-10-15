from django.shortcuts import redirect

def logout(request):
    # Supprimer les informations de l'utilisateur de la session,
    # cela revient à déconnecter l'utilisateur
    request.session.flush()
    # Rediriger vers la page de connexion ou d'accueil
    return redirect('user_list')