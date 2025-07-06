from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.actor import Actor
from relations.serializers.actor_serializer import ActorSerializer
from utils.timeout import ONE_DAY, TWELVE_HOURS


__all__ = [
    'ActorDetailAPIView',
    'MoviesByActorAPIView'
]

class ActorDetailAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, actor_id):
        cache_key = f'Actor_detail_{actor_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        actor = get_object_or_404(Actor, id=actor_id)
        serializer = ActorSerializer(actor)
        cache.set(cache_key, serializer.data, timeout=ONE_DAY)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByActorAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, actor_id):
        cache_key = f'Movies_by_actor_{actor_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        actor = get_object_or_404(Actor, id=actor_id)
        movies = Movie.objects.filter(actors=actor, is_active=True)
        serializer = MovieSerializer(movies, many=True)
        cache.set(cache_key, serializer.data, timeout=TWELVE_HOURS)

        return Response(serializer.data, status=status.HTTP_200_OK)