from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.director import Director
from relations.serializers.director_serializer import DirectorSerializer


__all__ = [
    'DirectorDetailAPIView',
    'MoviesByDirectorAPIView'
]

class DirectorDetailAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, director_id):
        director = get_object_or_404(Director, id=director_id)
        serializer = DirectorSerializer(director)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByDirectorAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, director_id):
        director = get_object_or_404(Director, id=director_id)
        movies = Movie.objects.filter(director=director, is_active=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)