import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings

from users.models.user import CustomerUser


@csrf_exempt
def sign_in(request):
    context = {
        'google_client_id': settings.GOOGLE_OAUTH_CLIENT_ID,
    }
    return render(request, 'sign_in.html', context)


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    user, created = CustomerUser.objects.get_or_create(
        email=user_data.get('email'),
        defaults={
            'username': user_data.get('name'),
        }
    )
    request.session['user_data'] = user_data

    return redirect('user_apis:sign_in')


def sign_out(request):
    del request.session['user_data']
    return redirect('user_apis:sign_in')