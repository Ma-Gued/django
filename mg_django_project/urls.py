from django.contrib import admin
from django.urls import path

from clairmarais.views import home_view
from clairmarais.views.poll_votes_view import poll_votes
from clairmarais.views.poll_details_view import poll_details
from clairmarais.views.login_view import login, user_list
from clairmarais.views.logout_view import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_list, name='user_list'),
    path('login/<int:user_id>/', login, name='login'),
    path('home/', home_view.home, name='home'),
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_details, name='poll_details'),
    path('logout/', logout, name='logout'),
     
    ]

