from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from interactions.models.comment import Comment
from interactions.serializers.comment_serializer import CommentSerializer
from utils.pagination import CustomPagination


__all__ = [
    'CommentListByMovieAPIView',
    'AddCommentAPIView',
    'DeleteCommentAPIView'
]

class CommentListByMovieAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get']

    def get(self, request, slug):
        pagination = self.pagination_class()
        movie = get_object_or_404(Movie.objects.filter(is_active=True), slug=slug)
        comments = Comment.objects.filter(movie=movie)
        paginator = pagination.paginate_queryset(comments, request)
        serializer = CommentSerializer(paginator, many=True)

        return pagination.get_paginated_response(serializer.data)


class AddCommentAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request, slug):
        movie = get_object_or_404(Movie.objects.filter(is_active=True), slug=slug)
        parent = None
        parent_id = request.data.get('parent')  

        if parent_id:  
            parent = get_object_or_404(Comment, id=parent_id, movie=movie)  

        serializer = CommentSerializer(data=request.data, context={
            'request': request,
            'movie': movie,
            'parent': parent
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommentAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete']

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment.objects.filter(user=request.user), id=comment_id)
        comment.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

