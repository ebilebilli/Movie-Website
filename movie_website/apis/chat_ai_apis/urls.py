from django.urls import path

from apis.chat_ai_apis.chat_ai_views import ChatAIAPIView


app_name = 'chat_ai_apis'

urlpatterns = [
    path(
        'chat-ai/', 
        ChatAIAPIView.as_view(), 
        name='chat-ai'
        )
]