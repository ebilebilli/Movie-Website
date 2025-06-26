from rest_framework import serializers

from models.like import Like


__all__ = [
    'LikeSerializer',
]

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
