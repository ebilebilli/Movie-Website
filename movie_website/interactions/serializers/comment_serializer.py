from rest_framework import serializers

from models.comment import Comment


__all__ = [
    'CommentSerializer',
]

class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField

    class Meta:
        model = Comment
        fields = '__all__'

    def get_likes(self, obj):
        return obj.like_count