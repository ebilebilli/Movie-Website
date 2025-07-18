from rest_framework import serializers

from relations.models.category import Category


__all__ = [
    'CategorySerializer',
]


class CategorySerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_movie_count(self, obj):
        return obj.movies.count()