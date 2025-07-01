from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status, Response
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from movies.serializers.movie_serializer import MovieSerializer
from relations.models.actor import Actor
from relations.serializers.actor_serializer import ActorSerializer


__all__ = [
    'ActorDetailAPIView',
    'MoviesByActorAPIView'
]

class ActorDetailAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, actor_id):
        actor = get_object_or_404(Actor, id=actor_id)
        serializer = ActorSerializer(actor)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesByActorAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, actor_id):
        actor = get_object_or_404(Actor, id=actor_id)
        movies = Movie.objects.filter(actors=actor, is_active=True)
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)