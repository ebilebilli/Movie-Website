from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.category import Category
from relations.serializers.category_serializer import CategorySerializer
from utils.timeout import ONE_WEEK, ONE_HOUR


__all__ = [
    'CategoryListAPIView',
    'MoviesByCategoryAPIView'
]

class CategoryListAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request):
        cache_key = f'Categories'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        cache.set(cache_key, serializer.data, timeout=ONE_WEEK)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, category_id):
        cache_key = f'Movies_by_category_{category_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        category = get_object_or_404(Category, id=category_id)
        movies = Movie.objects.filter(categories=category, is_active=True)
        serializer = MovieSerializer(movies, many=True)
        cache.set(cache_key, serializer.data, timeout=ONE_HOUR)

        return Response(serializer.data, status=status.HTTP_200_OK)