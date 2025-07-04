from rest_framework import serializers

from interactions.models.bookmark import Bookmark
from movies.serializers.movie_serializer import MovieSerializer


__all__ = [
    'BookmarkSerializer',
]

class BookmarkSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    
    class Meta:
        model = Bookmark
        fields = ['id', 'movie']
        read_only_fields = ['id', 'movie', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['movie'] = self.context['movie']
        return super().create(validated_data)
