import hashlib
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

from movies.models import Movie
from movies.serializers.movie_serializer import *
from utils.pagination import CustomPagination


__all__ = [
    'MovieListAPIView',
    'MovieDetailAPIView',
    'SearchAPIView'
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


class SearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        query_params = request.GET.urlencode()
        cache_key = f'search_{hashlib.md5(query_params.encode()).hexdigest()}'
        cached_data = cache.get(cache_key)

        if cached_data:
            if isinstance(cached_data, dict):
                return Response(cached_data, status=status.HTTP_200_OK)
            else:
                cache.delete(cache_key)

        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            cache.set(cache_key, paginated_response.data, timeout=250)
            return paginated_response

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        request = self.request
        search_query = request.query_params.get('search', '')
        category_id = request.query_params.get('category_id')
        release_date_id = request.query_params.get('release_date_id')
        ordering = request.query_params.get('ordering', '-id')

        allowed_ordering_fields = ['id', 'created_at', 'rating']
        if ordering.lstrip('-') not in allowed_ordering_fields:
            ordering = '-id'

        queryset = Movie.objects.filter(is_active=True)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if release_date_id:
            queryset = queryset.filter(release_date_id=release_date_id)
        
        return queryset.order_by(ordering)

    