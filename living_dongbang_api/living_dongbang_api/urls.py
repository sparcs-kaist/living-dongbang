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

from .apps.sample_app import views
from .apps.auth import views as auth_views

import environ
env = environ.Env()

urlpatterns = [
    path('auth/login', auth_views.try_login, name='login'),
    path('auth/logout', auth_views.try_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('frontend/', RedirectView.as_view(url=env('FRONTEND_BASE_URL')), name='frontend'),
    path('', views.index, name='index'),
]
