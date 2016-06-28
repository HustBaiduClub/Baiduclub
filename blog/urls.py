__author__ = 'david'
from django.conf.urls import include, url
from django.views.generic import *
from django.conf import settings
from django.conf.urls.static import static
from .models import Post# , Comment
from member.models import UserProfile
from django.core.paginator import Paginator
from . import views

urlpatterns = [
    url(r'^$', views.listing),
    url(r'^(?P<pk>\d+)$', views.Blogsingle.as_view(), name='my_detail_view_url'),
    url('^my_form/$', views.MyFormView.as_view(), name='my_form_view_url'),
    url(r'^comment', views.handle_comment)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''DetailView.as_view(
        # queryset=Comment.objects.all(),
        model=Post,
        template_name='blogshow.html',))
'''
