from rest_framework import serializers

from models.director import Director


__all__ = [
    'DirectorSerializer',
]

class DirectorSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Director
        fields = '__all__'
