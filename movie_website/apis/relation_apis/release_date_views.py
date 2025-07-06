from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.release_date import ReleaseDate
from relations.serializers.release_date_serializer import ReleaseDateSerializer
from utils.timeout import ONE_WEEK, ONE_HOUR


__all__ = [
    'ReleaseDateListAPIView',
    'MoviesByReleaseDateAPIView'
]

class ReleaseDateListAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request):
        cache_key = f'Release_dates'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        release_date = ReleaseDate.objects.all()
        serializer = ReleaseDateSerializer(release_date, many=True)
        cache.set(cache_key, serializer.data, timeout=ONE_WEEK)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByReleaseDateAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, release_date_id):
        cache_key = f'Movies_by_release_date_{release_date_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        
        release_date = get_object_or_404(ReleaseDate, id=release_date_id)
        movies = Movie.objects.filter(release_date=release_date, is_active=True)
        serializer = MovieSerializer(movies, many=True)
        cache.set(cache_key, serializer.data, timeout=ONE_HOUR)

        return Response(serializer.data, status=status.HTTP_200_OK)