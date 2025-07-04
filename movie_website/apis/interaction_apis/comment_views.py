from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from movies.models import Movie
from users.models import CustomerUser
from interactions.models.comment import Comment
from interactions.serializers.comment_serializer import CommentSerializer
from utils.pagination import CustomPagination


__all__ = [
    'CommentListByMovieAPIView',
    'CommentListByUserAPIView',
    'AddCommentAPIView',
    'CommentDetailAPIView',
]

class CommentListByMovieAPIView(APIView):
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    http_method_names = ['get']

    def get(self, request, slug):
        pagination = self.pagination_class()
        movie = get_object_or_404(Movie.objects.filter(is_active=True), slug=slug)
        comments = Comment.objects.filter(movie=movie)
        paginator = pagination.paginate_queryset(comments, request)
        serializer = CommentSerializer(paginator, many=True)

        return pagination.get_paginated_response(serializer.data)


class CommentListByUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    http_method_names = ['get']

    def get(self, request):
        user = request.user
        pagination = self.pagination_class()
        comments = Comment.objects.filter(user=user)
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


class CommentDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete', 'patch']

    def patch(self, request, comment_id):
        comment = get_object_or_404(Comment.objects.filter(user=request.user), id=comment_id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, comment_id):
        user = request.user
        comment = get_object_or_404(Comment.objects.filter(user=user).first(), id=comment_id)
        comment.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    

