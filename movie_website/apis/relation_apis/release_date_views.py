from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Response
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.release_date import ReleaseDate
from relations.serializers.release_date_serializer import ReleaseDateSerializer


__all__ = [
    'ReleaseDateListAPIView',
    'MoviesByReleaseDateAPIView'
]

class ReleaseDateListAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request):
        release_date = ReleaseDate.objects.all()
        serializer = ReleaseDateSerializer(release_date, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByReleaseDateAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, release_date_id):
        release_date = get_object_or_404(ReleaseDate, id=release_date_id)
        movies = Movie.objects.filter(release_date=release_date, is_active=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)