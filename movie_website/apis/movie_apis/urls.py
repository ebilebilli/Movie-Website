from django.urls import path

from apis.movie_apis.movie_views import *


urlpatterns = [
    path(
        'movies/', 
        MovieListAPIView.as_view(), 
        name='movies'
        ),
    path(
        'movies/<slug:slug>', 
        MovieDetailAPIView.as_view(), 
        name='movie-detail'
        )  
]