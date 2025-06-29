from rest_framework import serializers

from models.watchlist import Watchlist
from movies.serializers.movie_serializer import MovieSerializer


__all__ = [
    'WatchlistSerializer',
]

class WatchlistSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    
    class Meta:
        model = Watchlist
        fields = ['id',]
        read_only_fields = ['id', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['movie'] = self.context['movie']
        return super().create(validated_data)
