from rest_framework import serializers

from interactions.models.like import Like


__all__ = [
    'LikeSerializer',
]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['comment'] = self.context.get('comment')
        
        return super().create(validated_data)