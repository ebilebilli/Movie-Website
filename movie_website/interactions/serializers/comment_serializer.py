from rest_framework import serializers

from interactions.models.comment import Comment


__all__ = [
    'CommentSerializer',
]

class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'parent', 'created_at', 'updated_at', 'like_count']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['movie'] = self.context['movie']
        return super().create(validated_data)

    def get_like_count(self, obj):
        return obj.like_count
    
