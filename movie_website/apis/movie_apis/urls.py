from django.urls import path

from apis.movie_apis.movie_views import *


app_name = 'movie_apis'

urlpatterns = [
    path(
        'movies/', 
        MovieListAPIView.as_view(), 
        name='movies'
        ),
    path(
        'movies/<slug:slug>/', 
        MovieDetailAPIView.as_view(), 
        name='movie-detail'
        ),
    path(
        'search/', 
        SearchAPIView.as_view(),
        name='search'
    ),
]