"""living_dongbang_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import token_verify, token_refresh

from .apps.sample_app import views
from .apps.auth import views as auth_views
from .apps.seat import views as seat_views

import environ
env = environ.Env()

urlpatterns = [
    path('auth/login', auth_views.try_login, name='login'),
    path('auth/logout', auth_views.try_logout, name='logout'),
    path('seat/getList', seat_views.get_list, name='get_seat_list'),
    path('admin/', admin.site.urls),
    path('api/token/verify', token_verify, name='verify_jwt_token'),
    path('api/token/refresh', token_refresh, name='refresh_jwt_token'),
    path('frontend/', RedirectView.as_view(url=env('FRONTEND_BASE_URL')), name='frontend'),
    path('', views.index, name='index'),
]
