from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Response
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.category import Category
from relations.serializers.category_serializer import CategorySerializer


__all__ = [
    'CategoryListAPIView',
    'MoviesByCategoriesAPIView'
]

class CategoryListAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByCategoriesAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        movies = Movie.objects.filter(categories=category, is_active=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)