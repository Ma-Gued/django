from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

# Importations des vues de l'application clairmarais
from clairmarais.views.event import home_view
from clairmarais.views.poll import poll_votes_view, poll_details_view, poll_create_view, vote_option_create_view
from clairmarais.views.login_logout import login_view, custom_login_view, custom_logout_view
from clairmarais.views.event import event_create_view, event_list_view, event_details_view

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # Authentification
    path('', custom_login_view.CustomLoginView.as_view(), name='login'),
    path('login/<int:user_id>/', login_view.user_login, name='user_login'),
    path('logout/', custom_logout_view.CustomLogoutView.as_view(), name='logout'),
    path('user_list/', login_view.user_list, name='user_list'),

    # Page d'accueil
    path('home/', home_view.home, name='home'),

    # Gestion des événements
    path('events/', event_list_view.EventListView.as_view(), name='event_list'),
    path('event/create/', event_create_view.EventCreateView.as_view(), name='event_create'),
    path('events/<int:event_id>/', event_details_view.event_details, name='event_details'),

    #TODO: Revoir les urls pour les polls (ils doivent être liés à un event)
    # Gestion des sondages liés aux événements
    path('event/<int:event_id>/polls/create/', poll_create_view.PollCreateView.as_view(), name='poll_create'),
    path('event/<int:event_id>/polls/create/add_vote_option/', poll_create_view.PollCreateView.as_view(), name='poll_add_vote_option'),
    path('event/polls/<int:poll_id>/options/add/', vote_option_create_view.VoteOptionCreateView.as_view(), name='poll_add_option'),

    # Affichage et gestion des votes des sondages
    path('polls/<int:poll_id>/votes/', poll_votes_view.poll_votes, name='poll_votes'),
    path('events/<int:event_id>/polls/<int:poll_id>/', poll_details_view.poll_details, name='poll_details'),
]