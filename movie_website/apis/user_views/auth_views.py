from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from users.models.user import CustomerUser
from users.serializers.user_serializers import CustomerUserSerializer
from users.serializers.auth_serializers import *


__all__ = [
    'RegisterAPIView',
]

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            return  Response({
                'message': 'Register completed successfully',
                'tokens': tokens
                },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)