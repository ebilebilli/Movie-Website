from rest_framework import serializers

from models.actor import Actor


__all__ = [
    'ActorSerializer',
]

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
