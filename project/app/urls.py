from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
   path("", views.home, name='home'),
   path("profile", views.profile, name='profile'),
   path("add", views.add, name='add'),
   path("search", views.search, name='search'),
   path("<username>", views.user, name='user'),
   path("album/<albumid>", views.album, name='album')
]