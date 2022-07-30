from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def try_login(request):
    # try defualt authentication
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    # 로그인 시도 후 프론트엔드 첫 페이지로 리다이렉트
    return redirect('/frontend')

def try_logout(request):
    logout(request)
    return HttpResponse('success')
