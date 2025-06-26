from rest_framework import serializers

from models.comment import Comment


__all__ = [
    'CommentSerializer',
]

class CommentSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)

    class Meta:
        model = Comment
        fields = '__all__'
