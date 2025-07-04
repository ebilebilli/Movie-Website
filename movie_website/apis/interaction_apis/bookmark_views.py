from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from interactions.models.bookmark import Bookmark
from interactions.serializers.bookmark_serializer import BookmarkSerializer
from utils.pagination import CustomPagination


__all__ = [
    'BookmarkListByUserAPIView',
    'AddBookmarkAPIView',
    'DeleteBookmarkAPIView'
]


class BookmarkListByUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get']

    def get(self, request):
        pagination = self.pagination_class()
        bookmarks = Bookmark.objects.filter(user=request.user)
        paginator = pagination.paginate_queryset(bookmarks, request)
        serializer = BookmarkSerializer(paginator, many=True)

        return pagination.get_paginated_response(serializer.data)


class AddBookmarkAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie.objects.filter(is_active=True), id=movie_id)
        serializer = BookmarkSerializer(data=request.data, context={
            'request': request,
            'movie': movie
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBookmarkAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete']

    def delete(self, request, bookmark_id):
        bookmark = get_object_or_404(Bookmark.objects.filter(user=request.user), id=bookmark_id)
        bookmark.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)