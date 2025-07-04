import openai
from celery import shared_task
from django.conf import settings

openai.api_key = settings.OPENAI_TOKEN

