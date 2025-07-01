from rest_framework import serializers

from relations.models.release_date import ReleaseDate


__all__ = [
    'ReleaseDateSerializer',
]

class ReleaseDateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReleaseDate
        fields = '__all__'
