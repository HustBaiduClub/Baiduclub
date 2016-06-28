__author__ = 'david'
from django.conf.urls import patterns, include, url, static
from django.views.generic import DetailView, TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.handle),                                             # handle the post request
]