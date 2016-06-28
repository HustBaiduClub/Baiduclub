"""Baiduclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import *
from django.conf import settings
from django.conf.urls.static import static
from member.models import UserProfile
from blog.models import Post
from aboutclub.models import ClubIntro
from .views import *
from group.models import Group


def get_data():
    dict1 = []
    dict2 = []
    dict3 = []
    if len(ClubIntro.objects.all()) % 2 == 1:
        dict3.append(ClubIntro.objects.all().order_by('-id')[0])
    for i in ClubIntro.objects.all():
        if i.id % 2 == 1:
            dict1.append(i)
        else:
            dict2.append(i)

    return {
        "post": Post.objects.all().order_by("-date")[:6],
        "user": UserProfile.objects.all(),
        "group": Group.objects.all(),
        "another": dict3,
        "about": [
            dict1,
            dict2,
        ],
    }
urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=get_data(),
        template_name='index.html')),
    url(r'liuqifan/', include(admin.site.urls)),
    # url(r'^account/login/', 'django.contrib.auth.views.login'),
    url(r'member/', include('member.urls')),
    url(r'blog/', include('blog.urls')),
    url(r'join/', include('handle.urls')),
    url(r'group', include('group.urls')),
    # url(r'^account/', account),
    url(r'^account/login', login),
    url(r'^account/logout', logout),
    url(r'^account/auth', auth_view),
    url(r'^account/invalid', invalid),
    url(r'^captcha/', include('captcha.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
