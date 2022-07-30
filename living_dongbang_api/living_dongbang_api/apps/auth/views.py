from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
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
            result = {'result': 'success'}
            result['username'] = username
            return JsonResponse(result, status=200)
        else:
            return JsonResponse({'result': 'failure'}, status=400)
    except:
        return JsonResponse({'result': 'failure'}, status=400)

def try_logout(request):
    logout(request)
    return JsonResponse({'result': 'success'})
