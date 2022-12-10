"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import (
    path,
    include,
)

from content.views import (
    index,
    detail,
    content_likes
)

from accounts.views import (
    signin_view,
    signup_view,
    signout_view,
)

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    path('sign-in/', signin_view, name='sign-in'),
    path('sign-up/', signup_view, name='sign-up'),
    path('sign-out/', signout_view, name='sign-out'),


    path('about/', TemplateView.as_view(template_name='about.html')),

    path('home/', index,name='content-home'),
    path('detail/<str:slug>/', detail,name='content-detail'),
    path('content/likes/<str:slug>/', content_likes, name='content-like'),
]
