from rest_framework import serializers

from relations.models.actor import Actor


__all__ = [
    'ActorSerializer',
]

class ActorSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)

    class Meta:
        model = Actor
        fields = '__all__'
