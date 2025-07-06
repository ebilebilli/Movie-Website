from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.director import Director
from relations.serializers.director_serializer import DirectorSerializer
from utils.timeout import ONE_DAY, TWELVE_HOURS

__all__ = [
    'DirectorDetailAPIView',
    'MoviesByDirectorAPIView'
]

class DirectorDetailAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, director_id):
        cache_key = f'Director_detail_{director_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        
        director = get_object_or_404(Director, id=director_id)
        serializer = DirectorSerializer(director)
        cache.set(cache_key, serializer.data, timeout=ONE_DAY)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByDirectorAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, director_id):
        cache_key = f'Movies_by_director_{director_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        director = get_object_or_404(Director, id=director_id)
        movies = Movie.objects.filter(director=director, is_active=True)
        serializer = MovieSerializer(movies, many=True)
        cache.set(cache_key, serializer.data, timeout=ONE_DAY)

        return Response(serializer.data, status=status.HTTP_200_OK)