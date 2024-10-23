from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from clairmarais.views.event import home_view
from clairmarais.views.poll.poll_votes_view import poll_votes
from clairmarais.views.poll.poll_details_view import poll_details
from clairmarais.views.login_logout.login_view import login
from clairmarais.views.login_logout.custom_login_view import CustomLoginView
from clairmarais.views.login_logout.custom_logout_view import CustomLogoutView
from clairmarais.views.login_logout.login_view import user_login, user_list
from clairmarais.views.event.event_create_view import EventCreateView
from clairmarais.views.event.event_list_view import EventListView
from clairmarais.views.event.event_details_view import EventDetailView
from clairmarais.views.poll.poll_create_view import PollCreateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('login/<int:user_id>/', user_login, name='user_login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user_list/', user_list, name='user_list'),
    path('home/', home_view.home, name='home'),
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_details, name='poll_details'),
    
    #creation d'event, branche event
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_details'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('polls/create/', PollCreateView.as_view(), name='poll_create'),
    path('events/<int:event_id>/polls/create/', PollCreateView.as_view(), name='poll_create'),


    ]

