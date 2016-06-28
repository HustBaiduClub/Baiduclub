__author__ = 'david'
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect


def account(request):
    if request.method == 'GET':
        return render_to_response('portfolio.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/account/invalid')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def invalid(request):
    return HttpResponseRedirect('/')