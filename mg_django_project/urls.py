"""
URL configuration for mg_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from items.views.home import home
from items.views.polls import poll_votes, poll_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    #Explication du path ci-dessous:
    # 1. On commence par 'polls/' pour indiquer que l'URL commence par 'polls/'.
    # 2. Ensuite, on utilise <int:poll_id> pour indiquer que l'URL doit contenir un entier (l'identifiant du sondage).
    # 3. Enfin, on termine par 'votes/' pour indiquer que l'URL se termine par 'votes/'.
    path('polls/<int:poll_id>/votes/', poll_votes, name='poll_votes'),
    path('polls/<int:poll_id>/', poll_detail, name='poll_detail'),     
    ]


