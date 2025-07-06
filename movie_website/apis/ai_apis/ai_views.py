from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from movies.models.movie import Movie
from users.models.user import CustomerUser
from ai.tasks import generate_ai_response_task


class MovieQueryRequestToAIAPIView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request):
        question = request.data.get('question', '')
        if not question:
            return Response({'error': 'There is no any question'})
        
        find_movie = Movie.objects.filter(title__icontains=question, is_active=True).values_list('title', flat=True).first()
        if find_movie:
            message = f'{find_movie} is active on our website'
        
        else:
            message = f'Sorry, there is not such movie on our website'

        ai_response = generate_ai_response_task(question=question, message=message)
        return Response(ai_response, status=status.HTTP_200_OK)