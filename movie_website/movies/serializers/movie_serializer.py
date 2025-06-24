from rest_framework import serializers

from models.movie import Movie


__all__ = [
    'MovieSerializer',
]

class MovieSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    poster = serializers.ImageField(use_url=True)

    class Meta:
        model = Movie
        fields = '__all__'