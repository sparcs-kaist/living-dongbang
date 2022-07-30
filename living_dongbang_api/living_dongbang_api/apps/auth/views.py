from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
import json


# Create your views here.
def try_login(request):
    # try defualt authentication
    try:
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username

            # create refresh token
            refresh = RefreshToken.for_user(user)
            result = {'result': 'success', 'username': username, 'access_token': str(refresh.access_token), 'refresh_token': str(refresh)}
            return JsonResponse(result, status=200)
        else:
            return JsonResponse({'result': 'failure'}, status=400)
    except:
        return JsonResponse({'result': 'failure'}, status=400)

def try_logout(request):
    logout(request)
    return JsonResponse({'result': 'success'})
