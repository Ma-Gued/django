from django.shortcuts import redirect

def logout(request):
    print(request.user)
    # Supprimer les informations de l'utilisateur de la session,
    # cela revient à déconnecter l'utilisateur
    request.session.flush()
    # Rediriger vers la page de connexion ou d'accueil
    print("APRES", request.user)
    return redirect('login')