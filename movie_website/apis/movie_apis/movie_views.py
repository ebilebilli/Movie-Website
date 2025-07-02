from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models import Movie
from movies.serializers.movie_serializer import *
from utils.pagination import CustomPagination


__all__ = [
    'MovieListAPIView',
    'MovieDetailAPIView'
]

class MovieListAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']
    pagination_class = CustomPagination

    def get(self, request):
        movies = Movie.objects.filter(is_active=True)
        pagination = self.pagination_class()
        paginated_movies = pagination.paginate_queryset(movies, request)
        serializer = MovieSerializer(paginated_movies, many=True)

        return pagination.get_paginated_response(serializer.data)


class MovieDetailAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, slug):
        movie = get_object_or_404(Movie.objects.filter(is_active=True), slug=slug)
        serializer = MovieDetailSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)


    
    