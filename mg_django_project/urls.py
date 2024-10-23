from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from clairmarais.views import home_view
from clairmarais.views.poll_votes_view import poll_votes
from clairmarais.views.poll_details_view import poll_details
from clairmarais.views.login_view import login
from clairmarais.views.custom_login_view import CustomLoginView
from clairmarais.views.custom_logout_view import CustomLogoutView
from clairmarais.views.login_view import user_login, user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('login/<int:user_id>/', user_login, name='user_login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('user_list/', user_list, name='user_list'),
    path('home/', home_view.home, name='home'),
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_details, name='poll_details'),
            

    ]

