from django.contrib import admin
from django.urls import path
from items.views import home_view

home = home_view.home
from items.views.poll_votes_view import poll_votes
from items.views.poll_details_view import poll_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_details, name='poll_details'),     
    ]


