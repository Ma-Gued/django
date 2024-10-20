from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from clairmarais.views import home_view
from clairmarais.views.poll_votes_view import poll_votes
from clairmarais.views.poll_details_view import poll_details
from clairmarais.views.login_view import login
from clairmarais.views.add_game_view import add_game
from clairmarais.views.delete_game_view import delete_game
from clairmarais.views.logistic_view import logistic
from clairmarais.views.add_meal_view import add_meal
from clairmarais.views.delete_meal_view import delete_meal
from clairmarais.views.custom_login_view import CustomLoginView
from clairmarais.views.custom_logout_view import CustomLogoutView
from clairmarais.views.login_view import user_login, user_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('login/<int:user_id>/', user_login, name='user_login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user_list/', user_list, name='user_list'),  # Liste des utilisateurs
    path('home/', home_view.home, name='home'),
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_details, name='poll_details'),
    path('add_game/', add_game, name='add_game'), 
    path('delete_game/<int:game_id>/', delete_game, name='delete_game'),
    path('add_meal/', add_meal, name='add_meal'),
    path('delete_meal/<int:meal_id>/', delete_meal, name='delete_meal'),
    path('poll/<int:poll_id>/logistic/', logistic, name='logistic'),
            

    ]

