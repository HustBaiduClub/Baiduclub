from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.views.generic import *
from .forms import CaptchaTestForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import datetime
import pytz
from .models import Post, Review
from django.contrib.auth.models import User
from member.models import UserProfile
# Create your views here.


def listing(request):
    blog_list = models.Post.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 5)  # Show 5 blogs per page

    page = request.GET.get('page')
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lists = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lists = paginator.page(paginator.num_pages)

    return render_to_response('bloglist.html', {"lists": lists})

'''
url(r'^$', ListView.as_view(
        queryset=Post.objects.all(),
        template_name="bloglist.html"
    )),
'''


class Blogsingle(DetailView):
    model = models.Post
    template_name = "blogshow.html"

    def get_context_data(self, **kwargs):
        context = super(Blogsingle, self).get_context_data(**kwargs)
        single_object = super(Blogsingle, self).get_object()
        comment_list = []
        for a in Review.objects.all().order_by('-id'):
            if a.blog.id == single_object.id:
                comment_list.append(a)

        context['form'] = CaptchaTestForm
        context['comment'] = comment_list
        context['users'] = UserProfile.objects.all()
        return context


class MyFormView(FormView):
    form_class = CaptchaTestForm
    success_url = '/blog/hehe'


def handle_comment(request):
    if request.method == 'POST':
        form = CaptchaTestForm(request.POST)
        comment_user = request.POST["user"]
        comment_content = request.POST["content"]
        comment_blog = request.POST["blog"]
        comment_email = request.POST["email"]
        if form.is_valid():
            time_now = datetime.utcnow().replace(tzinfo=pytz.utc)
            for a in Post.objects.all():
                if a.title == comment_blog:
                    comment_blog_one = a
            token = 0
            for b in User.objects.all():
                if comment_user == b.username:
                    token = 1
            information = Review(
                blog=comment_blog_one,
                user=comment_user,
                img_url='/templates/images/user-03.png',
                email=comment_email,
                content=comment_content,
                time=time_now,
            )
            if token == 0:
                information.save()
            url = request.POST["id"]
            return HttpResponseRedirect('/blog/'+url)
        else:
            if request.user.is_authenticated():
                time_now = datetime.utcnow().replace(tzinfo=pytz.utc)
            for a in Post.objects.all():
                if a.title == comment_blog:
                    comment_blog_one = a
            for b in UserProfile.objects.all():
                if comment_user == b.user.username:
                    comment_img_url = b.portrait.url
            print(comment_img_url)
            information = Review(
                blog=comment_blog_one,
                user=comment_user,
                img_url='/'+comment_img_url,
                email=comment_email,
                content=comment_content,
                time=time_now,
            )
            information.save()
            return HttpResponseRedirect('/blog/'+request.POST["id"])
    else:
        return render(request, 'index.html')
