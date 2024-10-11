from django.contrib import admin
from django.urls import path
from clairmarais.views import home_view

home = home_view.home
from clairmarais.views.poll_votes_view import poll_votes
from clairmarais.views.poll_details_view import poll_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_details, name='poll_details'),     
    ]


