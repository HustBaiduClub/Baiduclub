__author__ = 'david'
from django.conf.urls import patterns, include, url, static
from django.views.generic import DetailView, TemplateView, ListView
from . import views
from .models import Group

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Group.objects.all(),
        template_name='groupall.html',
    )),                                             # handle the post request
    # url(r'^(?P<pk>\d+)$', views.Blogsingle.as_view(), name='my_detail_view_url'),
]
