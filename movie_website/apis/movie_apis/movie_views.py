from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from relations.models.category import Category
from movies.models import Movie
from utils.pagination import CustomPagination


class MovieListAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request):
        movies = Movie