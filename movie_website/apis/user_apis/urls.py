from django.urls import path
from apis.user_apis.google_views import *


app_name = 'user_apis'

urlpatterns = [
    path('sign-in', sign_in, name='sign_in'),
    path('sign-out', sign_out, name='sign_out'),
    path('auth-receiver', auth_receiver, name='auth_receiver'),
]