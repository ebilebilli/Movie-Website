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
        read_only_fields = ['id', 'parent', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['movie'] = self.context.get('movie')
        validated_data['parent'] = self.context.get('parent')
        return super().create(validated_data)

    def get_like_count(self, obj):
        return obj.like_count
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return {k: v for k, v in rep.items() if v is not None}