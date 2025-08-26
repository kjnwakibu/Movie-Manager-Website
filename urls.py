from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('movies/', views.movies, name='movies'),
    path('shows/', views.shows, name='shows'),
    path('movie-info/', views.movie_info, name='movie-info'),
    path('list-info/', views.list_info, name='list-info'),
    path('random-media', views.random_picker, name='random-media')
]