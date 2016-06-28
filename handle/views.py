from django.shortcuts import render
from django.http import *
from django.forms import Form
from .models import Handle
from django.core.mail import send_mail
from blog.models import Post
from member.models import UserProfile
# Create your views here.
from django.shortcuts import render_to_response


def handle(request):
    user_pro = UserProfile.objects.all()[:4]
    blog_post = Post.objects.all()[:4]
    if request.method == 'POST':
        print('a form is posted')
        form_data = Form(request.POST)
        if form_data.is_valid():
            apply_name = request.POST["contactLname"]
            apply_email = request.POST["contactEmail"]
            apply_group = request.POST["selectList"]
            apply_msg = request.POST["contactMessage"]

        information = Handle(
            name=apply_name,
            email=apply_email,
            group=apply_group,
            intro=apply_msg,
        )
        information.save()
    return HttpResponseRedirect('/')
'''
        title = 'This is mail title.'
        message = 'Hello! This is a message!'
        sender = '123@123.com'
        mail_list = [apply_email, ]
        try:
            send_mail(
                subject=title,
                message=message,
                from_email=sender,
                recipient_list=mail_list,
                fail_silently=False,
                connection=None
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')'''
