from rest_framework import serializers

from movies.models.movie import Movie


__all__ = [
    'MovieSerializer',
    'MovieDetailSerializer'
]

class MovieSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(use_url=True)

    class Meta:
        model = Movie
        fields = ['title', 'categories',  'rating', 'poster']


class MovieDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    poster = serializers.ImageField(use_url=True)

    class Meta:
        model = Movie
        fields = '__all__'