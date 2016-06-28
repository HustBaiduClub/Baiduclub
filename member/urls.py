__author__ = 'david'
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import *
from django.conf import settings
from .models import UserProfile

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=UserProfile.objects.all()[:5],
        template_name='member.html')),
]