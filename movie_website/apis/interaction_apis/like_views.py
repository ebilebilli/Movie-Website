from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import  IsAuthenticated

from interactions.models import Comment
from interactions.models.like import Like
from interactions.serializers.like_serializer import LikeSerializer


__all__ = [
    'CommentListByMovieAPIView',
    'AddCommentAPIView',
    'CommentDetailAPIView',
]

class AddLikeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request, comment_id):
        user = request.user
        comment = get_object_or_404(Comment, id=comment_id)
        if Like.objects.filter(comment=comment, user=user).first():
            return Response({'error': 'You are already liked this comment'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LikeSerializer(data=request.data, context={
            'request': request,
            'comment': comment
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteLikeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete']

    def delete(self, request, like_id):
        user = request.user
        like = get_object_or_404(Like.objects.filter(user=user), id=like_id)
        like.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
