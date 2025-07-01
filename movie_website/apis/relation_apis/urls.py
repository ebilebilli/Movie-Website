from django.urls import path

from apis.relation_apis.category_views import *
from apis.relation_apis.actor_views import *
from apis.relation_apis.director_views import *
from apis.relation_apis.release_date_views import *


app_name = 'relation_apis'

urlpatterns = [
    # Category endpoints
    path(
        'categories/', 
        CategoryListAPIView.as_view(), 
        name='categories'
        ),
    path(
        'category/<int:category_id>/movies/', 
        MoviesByCategoryAPIView.as_view(), 
        name='movies-by-category'
        ),
    # Actor endpoints
    path(
        'actor/<int:actor_id>/', 
        ActorDetailAPIView.as_view(), 
        name='actor'
        ),
    path(
        'actor/<int:actor_id>/movies/', 
        MoviesByActorAPIView.as_view(), 
        name='movies-by-actor'
        ),
    # Director endpoints
    path(
        'director/<int:director_id>/', 
        DirectorDetailAPIView.as_view(), 
        name='director'
        ),
    path(
        'director/<int:director_id>/movies/', 
        MoviesByDirectorAPIView.as_view(), 
        name='movies-by-director'
        ),
    path(
        'release_dates/', 
        ReleaseDateListAPIView.as_view(), 
        name='release_dates'
        ),
    path(
        'release_date/<int:release_date_id>/movies/', 
        MoviesByReleaseDateAPIView.as_view(), 
        name='movies-by-release_date'
        ),
]   